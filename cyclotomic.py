#Cyclotomic Polynomial program. Moving from trying it out in singular to python.

#See Lang and Wolfram
from sympy import *
from sympy.abc import x, y
import numpy as np


def mobius(n):

    #This program returns (-1)^k where k is the number of prime factros for a given n

    k = 0 #Current number of distinct prime factors
    if n == 1: #if n is 1, return 1
        return 1

    for i in range(2,n-1): #for all integers. i,  between 2 and n
        if n % i == 0: #if i divides n
            if n % (i ** 2) == 0: #check that i squared divides n 
                return 0 #if it does, return 0
            else: #if not, add 1 to k
                k+=1
    if k == 0:
        #print("The number", n ,"is prime")
        return -1
    return((-1)**k) #if each i only divides n once, then return -1^k, where k is the number of distinct prime factors


def cyclotomic(m):

    #\Phi_n(x) = \Product _{d | n} (1-x^{n/d})^{\mu(d)}
    #Where \mu(d) is the mobius function
    x = symbols('x')

    for i in range(2,m-1): 
        product = (1 - x**m)
        if m % i == 0: #running through the list of divisors of m
            divisor = ((x**(m//i))-1)**mobius(i) #Creates the polynomial 
            print(divisor, "is divisor")
            product = product * divisor
            print(product, "is product")
            
    print("The", m, "th cyclotomic polynomial is", product)

#cyclotomic(4)


def gcd(a,b):
    if (a ==0):
        return b
    else:
        return gcd(b % a, a)

def totient(d):
    #Euler's Totient function gives the number of relatively prime numbers less than d
    result = 1
    for i in range(2,d):
        if (gcd(i,d) == 1):
            result+=1
    return result

def coefficient(j, n):
   print(j, "this is j")
   total = 0
   if j == 1:
       return 1 
   if j == 0:
       return 1
   else:
       for m in range(0, j):
               total += mobius(gcd(n,j-m)) * totient(gcd(n,j-m)) * coefficient(m,n)
               print(gcd(n,j-m), "gcd(n,j-m)", mobius(gcd(n,j-m)), "mobius gcd(n,j-m)", coefficient(m,n),"coefficient(m,n)")
               print(total, "after recursion in coefficient step", m, "in phase", j)
   anj = (-mobius(n) / j)
   return (anj * total)




def squarefree(r):
    Phinx = 0
    #x = Symbols('x')
    #This defines a way to explicitly produce nth cyclotomic polynomials for squarefree n
    # \Phi_n(x) = \Sum _j=0 ^\phi(n) a_nj z^{\phi(n) - j}
    for j in range(totient(r)+1):
        Phinx += coefficient(j,r) * (x ** (totient(r) - j))
        print (Phinx, "this is phinx at step", j)
    return Phinx

squarefree(10)

# base = np.poly1d([-1,1]) #creates the polynomial x
 #   print(base)
  #  pur = base.polypow(base,m)
   # print(pur)
    #for i in range(2,m-1): 
     #   if m % i == 0: #running through the list of divisors of n
      #      divisior = (1-(base**(m//i)))**mobius(i) #Creates the polynomial 
       #     pur = np.polymul(pur,divisor) #
        #    print(np.poly1d(pur))
  #  print("The", m, "th cyclotomic polynomial is", pur)

   # return pur

