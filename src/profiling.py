import clcLib.mathlib as m
import cProfile, pstats, io
import sys
import random

N = 0

def generateSample(numberOfnumbers):
    afile = open("input.txt", "w" )

    for i in range(numberOfnumbers):
        line = str(random.randint(1, 30)) #numbers between 1-30
        afile.write(line+"\n")

    afile.close()

def profile(fnc):
    #decorator for profiling use @profile

    def inner(*args, **kwargs):

        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr,stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

@profile
def Standard_deviation():
    global N
    sumSX = 0
    sumSX2 = 0
    for line in sys.stdin:
        strip = int(line.rstrip())
        N = m.add(N,1)
        sumSX = m.add(sumSX,strip)
        sumSX2 = m.add(sumSX2,m.power(strip,2))

    x_line = m.multiplication(m.divide(1,N),sumSX)
    multInBracket = m.multiplication(N,m.power(x_line,2))
    bracket = m.subtraction(sumSX2,multInBracket)
    leftSide = m.divide(1,m.subtraction(N,1))
    multOutBracket = m.multiplication(leftSide,bracket)
    result = m.nthRoot(2,multOutBracket)
    return result

#generateSample(100)
print(Standard_deviation())