import matplotlib.pyplot as plt
import numpy as np
import cmath
import math as mt
from sympy import *
from scipy.optimize import fsolve
import scipy as s

x = symbols('x')


print('A / (x * ( pow(x,2) + 2*ζ*np.sqrt(A) * x + A))')
def y(x,a,b):
    return b / (x * (x ** 2 + 2*a*cmath.sqrt(b) * x + b))


""" Create three cases for A = 1000,10,100 ans z = 0.158,0.5,1.58
"""
listz=[0.158, 0.5, 1.58]
listA = [1000, 100, 10]

for (z,A) in zip(listz,listA):
    a=1
    b=2*z*np.sqrt(A)
    c=A
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('The solution are {0:.2f} and {1:.2f}'.format(sol1,sol2))
    s=1
    y1= y(s, z, A)
    c0 = limit( (s*y1 ), s, 0)
    c1 = limit( ( (s -sol1)*y1 ), s, sol1)
    c2 = limit( (s -sol2)*y1 , s, sol2)
    print('Cosntants are C0: ',c0,'C1:',c1,'C2:',c2,'\n')

    t = np.linspace(0,1.1,11)
    def y(w):
        return c0 + c1*cmath.exp(sol1*w) + c2*cmath.exp(sol2*w)
    print(y(t))
fig, ax = plt.subplots()

