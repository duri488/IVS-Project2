#definitions of math functions for calculator
from math import ceil, floor

PI = 3.14159265358979

def add(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Invalid input"
    return a/b

def modulo(a,b):
    return a%b

def power(base,x): #format base^x
    if base == 0 and x < 0:
        return "Invalid input"

    return base**x

def nthRoot(x,base): #format x-th root from base

    if base < 0 and x%2 == 0:
        return "Invalid input"

    if x == 0:
        return"Invalid input"

    if base >= 0:
        return round((base)**(1/x),14)
    elif base < 0:
        return round(-(abs(base)**(1/x)),14)
        
 
    #return round((base)**(1/x),14)
    
#@strict_types
def factorial(n: int) -> int:
    factorial = 1
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 1
    else:
        for i in range(1,n + 1):
            factorial = factorial*i
        return factorial
