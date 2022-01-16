import numpy as np

from scipy import integrate
z = np.linspace(-1, 1, 2551)

def f1(w):
    return 10 * np.exp(-50 * abs(w)) - 0.01 / ((w - 0.5) ** 2 + 0.001) + 5 * np.sin(5 * w)

myf1= f1(z)
print(myf1)
I1 = integrate.simps( myf1, z)
print("Integral I1 using scipy, Simpson 's rule is: ",I1)


#f1= lambda w: 10 * np.exp(-50 * abs(w)) - 0.01 / ((w - 0.5) ** 2 + 0.001) + 5 * np.sin(5 * w)


def simpson(f,a,b,N=50):
    '''Approximate the integral of f(x) from a to b by Simpson's rule.

    Simpson's rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/3) \sum_{k=1}^{N/2} (f(x_{2i-2} + 4f(x_{2i-1}) + f(x_{2i}))
    where x_i = a + i*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : (even) integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using
        Simpson's rule with N subintervals of equal length.

    Examples
    --------
    1.0
    '''
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


I2  = simpson(f1 , -1, 1, 2550)
print("Integral I2 using a function crea"
      "ted with only numpy:",I2)

