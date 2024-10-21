
"""
Solutions to module 4
Review date:
"""

student = "Victoria Åhman"
reviewer = ""

import math as m
import random as r
import numpy 

from time import perf_counter as pc

import concurrent.futures as future

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    
    #List comprehension to create a (nestled) list of all coordinates
    #Inner list: coordinates for each point in d dimensions
    #Outer list: lists of n of these coordinates
    coordinates_lst = [[r.uniform(-1, 1)for i in range (0, d)] for j in range (0, n)]

    #Create a list of the squares for each coordinate using list comprehension
    squared_lst = [[i**2 for i in j] for j in coordinates_lst]

    #Create a list of the distances to the origin for every coordinate with map and lambda 
    distance_lst= list(map(lambda x: m.sqrt(sum(x)), squared_lst))
   
    #Create a list of the distances that is inside the sphere with filter and lambda
    distances_inside = list(filter(lambda d: d <= 1, distance_lst))

    #The number of points inside the circle is the length of the distances_inside list
    n_c = len(distances_inside)

    #The volume is approximated by
    #(2**d) *(n_c)/n

    approx_volume = (2**d) * (n_c/n)

    return approx_volume

def hypersphere_exact(n,d): #Assuming radius = 1
    V_d = m.pi**(d/2) / m.gamma(d/2 + 1)
    return V_d

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    #using multiprocessor to perform 10 iterations of volume function 
    start = pc()

    processes = []
    results = []
    with future.ProcessPoolExecutor() as ex:
        for _ in range(np):
            p = ex.submit(sphere_volume, n, d)
            processes.append(p)

        for process in processes:
            r = process.result()
            results.append(r)

    end = pc()

    print(f"Process with parallelizing the loop took {round(end-start, 2)} seconds")

    result = numpy.mean(results)

    return result

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    start = pc()
    #split data
    n_split = n//np

    processes = []
    results = []
    with future.ProcessPoolExecutor() as ex:
        for _ in range(np):
            p = ex.submit(sphere_volume, n_split, d)
            processes.append(p)

        for process in processes:
            r = process.result()
            results.append(r)

    result = sum(results)

    end = pc()

    print(f"Process with splitting the data took {round(end-start, 2)} seconds")

    return result

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    end = pc()
    print(f"Process with for-loop took {round(end-start, 2)} seconds")

    print(sphere_volume_parallel1(n,d,10))

    #part 2 - parallelize computations by splitting data

    start = pc()
    sphere_volume(n,d)
    end = pc()
    print(f'Proccess without parallelization took {round(end-start, 2)} seconds')

    sphere_volume_parallel2(n,d,10)



if __name__ == '__main__':
	main()
