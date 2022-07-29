from sympy import exp
from sympy.abc import x, y

c = exp (y)
x = (x**2)*(x**(-3))
print(x)
print(c)

#Seems like the abc import of sympy lets us use the variables freely.
