
"""
Solutions to module 4
Review date:
"""

student = "Victoria Åhman"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math

def approximate_pi(n):
    n_c = 0 #Number of points inside the circle
    p_in_x = [] #Used to store x coordinates inside circle
    p_in_y = [] #Used to store y coordinates inside circle
    p_out_x = [] #Used to store x coordinates outside circle
    p_out_y = [] #Used to store y coordinates outside circle

    for i in range (n): #Create coordinates for each point
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)

        if math.sqrt(x**2 + y**2) <= 1:
            n_c += 1
            p_in_x.append(x)
            p_in_y.append(y)
        else:
            p_out_x.append(x)
            p_out_y.append(y)

    pi_approx = 4 * n_c/n
    print(f'Number of points inside the circle with n = {n}: {n_c}')
    print(f'Approximation of pi with n = {n}: {pi_approx}')
    print(f'Pi: {math.pi}')

    #Create figures
    plt.title(f'Monte Carlo approximation of pi with n = {n}')
    plt.scatter(p_in_x, p_in_y, color = 'red')
    plt.scatter(p_out_x, p_out_y, color = 'blue')

    #Save figures as png files
    plt.savefig(f'pi_{n}')
    plt.clf()

    return pi_approx
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
