#!/usr/local/bin/python3.7
import numpy as np
import math 
import cmath 

def quadSolver(equation): #Solves the quadratic equation 
    # ex. equation = np.array([a,b,c]), where ax^2 +/- bx +/- c = 0
    # eqSolvers.quadSolver(equation)
    a = equation[0] 
    b = equation[1]
    c = equation[2]
    if a != 0: 
        discriminant = math.pow(b,2) - (4 * a * c)
        if discriminant > 0.0: #Real solution  
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        elif discriminant == 0.0: #One real solution 
            x1 = -b / (2 * a) 
            x2 = x1
        elif discriminant < 0.0: #Complex solution
            x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
            x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        x = np.array([x1, x2]) 
    else: 
        x = np.array([-b / c]) 
    return x

def gaussElimination(a, b): #Missing testing, 
#Ref: Numerical Methods in Eng. w/ Python 3 by Kiausalaas; pg 2 
#Ax = b; A is matrix and b is the vector
    n = len(b) 
    for k in range(0, n-1):
        for i in range(k+1, n):
            if a[i,k] != 0.0:
                lam = a[i,k] / a[k,k] 
                a[i, k+1:n] = a[i, k+1:n] - lam * a[k, k+1:n]
                b[i] = b[i] - lam * b[k]
        for k in range(n-1, -1, -1):
            b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n])) / a[k, k] 
        return b 


#Testing formula 
eq = np.array([3,6,8])
#b = np.matrix('1 2 3; 2 4 5; 2 5 1')
A = np.array([[1,1,1],[2,2,0],[-1,0,3]]) 
print(gaussElimination(A,eq))
#print(quadSolver(eq)) 

