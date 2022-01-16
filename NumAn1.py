import numpy as np
x_o = 0.3
a,i = 0,0
b = 0
def x_func(x):
    return 0.5*(np.log(3*x+1))
a = x_func(x_o)
print("The value of x0 =",x_o)
#while (abs(b-a) > 0.5*10**(-12)):
for j in range(10):

    print("x_n=",a)
    if i != 0:
        a = b
    b = x_func(a)
    print("x_(n+1)=",b)
    i = i + 1
    print("The number of repetitions is:",i)

print("End")