
"""
Solutions to module 4
Review date:
"""

student = "Victoria Åhman"
reviewer = ""

import math as m
import random as r

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
     
def main():
    n = 100000
    d = 2
    sphere_volume(n,d)

if __name__ == '__main__':
	main()
