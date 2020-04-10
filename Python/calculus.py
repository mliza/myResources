#!/usr/local/bin/python3.7
import numpy as np
import sympy as sp 
import math 

def taylorSeries(function, x, a, n):
#function = the function that you are approximating 
#x = what you are deriving against    
#a = the value at which the series is being evaluated 
#n = the order at which you are evaluating 

#---    Ex. function: sp.Symbol('x')      --- 
#---        function = sp.sin(x)          ---
#--- g = taylorSeries(function, x, 0, 2) --- 
    tayList = [] 
    for i in np.arange(n + 1): 
        taylorApprox = (function.diff(x,i).subs(x,a) / math.factorial(i)) * (x - a)**i
        tayList.append(taylorApprox) #Append approximations to a list 
        tayArray = np.array(tayList) #Convert List to array 
    return tayList

#Example to RUN taylorSeries
x = sp.Symbol('x') 
function = sp.sin(x)
g = taylorSeries(function,x,0,10)
print(g) 
