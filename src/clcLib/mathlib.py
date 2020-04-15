#definitions of math functions for calculator
from math import ceil, floor

PI = 3.14159265358979

def add(a,b):
    
    """
    Funkcia sčíta dve čísla, a+b

    :param a: celé(int) alebo desatinné(float) číslo
    :param b: celé(int) alebo desatínné(float) číslo
    :return: Súčet čísel "a" a "b" (int alebo float)
    """

    return a+b

def subtraction(a,b):

    """
    Funkcia odčíta dve čísla, a-b

    :param a: celé(int) alebo desatinné(float) číslo
    :param b: celé(int) alebo desatínné(float) číslo
    :return: Rozdiel čísel "a" a "b" (int alebo float)
    """

    return a-b

def multiplication(a,b):

    """
    Funkcia na násobenie dvoch čísel, a*b

    :param a: celé(int) alebo desatinné(float) číslo
    :param b: celé(int) alebo desatínné(float) číslo
    :return: Výsledok násobenia čísel "a" a "b" (int alebo float)
    """

    return a*b

def divide(a,b):

    """
    Funkcia na delenie dvoch čísel, a/b

    :param a: celé(int) alebo desatinné(float) číslo
    :param b: celé(int) alebo desatínné(float) číslo
    :return: Výsledok delenia čísel "a" a "b" (float), pri neúspechu "Invalid input" (string)
    """

    if b == 0:
        return "Invalid input"
    return a/b

def modulo(a,b):

    """
    Funkcia modulo medzi dvoma číslami, a mod b

    :param a: celé(int) alebo desatinné(float) číslo
    :param b: celé(int) alebo desatínné(float) číslo
    :return: Modulo medzi číslami "a" a "b" (int alebo float)
    """

    return a%b

def power(base,x): #format base^x

    """
    Funkcia na umocňovanie, base^x

    :param base: celé(int) alebo desatinné(float) číslo
    :param x: celé(int) alebo desatínné(float) číslo
    :return: Výsledok umocnenia base^x (int alebo float), pri neúspechu "Invalid input" (string)
    """

    if base == 0 and x < 0:
        return "Invalid input"

    return base**x

def nthRoot(x,base): #format x-th root from base

    """
    Funkcia na n-tú odmocninu, x-tá odmocnina z base

    :param base: celé(int) alebo desatinné(float) číslo
    :param x: celé(int) alebo desatínné(float) číslo
    :return: Výsledok odmocniny x-tá odmocnina z base (float), pri neúspechu "Invalid input" (string)
    """

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

    """
    Funkcia na výpočet faktoriálu, n!

    :param n: celé(int) číslo
    :return: Výsledok n-tého faktoriálu (int), pri neúspechu "Invalid input" (string)
    """

    factorial = 1
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 1
    else:
        for i in range(1,n + 1):
            factorial = factorial*i
        return factorial
