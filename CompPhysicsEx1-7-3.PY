from pylab import *
def plottrig(f):
    xvalues = linspace(-pi,pi,1000)
    xvalues = ndarray.tolist(xvalues)
    plot(xvalues,f(xvalues))
    xlim(-pi,pi)
    ylim(-2,2)
    
trigfunctions = (sin,cos,tan)

for function in trigfunctions:
    print function(pi/6.0)
    plottrig(function)
show()
