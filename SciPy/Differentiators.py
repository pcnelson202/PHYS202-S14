import numpy
def twoPtForwardDiff(x,y):
    """Calculates dy/dx as a forward finite difference.
    The derivative at a point a is the change in f(a) to f(b),
    divided by (b-a), where b > a"""
    dydxForward = numpy.zeros(y.shape,float)
    dydxForward[0:-1]= numpy.diff(y)/numpy.diff(x)
    dydxForward[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydxForward

def twoPtCenteredDiff(x,y):
    """Calculated dy/dx as a centered finite difference. 
    If a < b < c, the derivative of f at b is f(c) - f(a) divided by (c-a)."""
    dydxCenter = numpy.zeros(y.shape,float)
    dydxCenter[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydxCenter[0] = (y[1]-y[0])/(x[1]-x[0])
    dydxCenter[-1] = (y[-1]-y[-2])/(x[-1] -x[-2])
    return dydxCenter

def fourPtCenteredDiff(x,y):
    """Calculated dy/dx as a centered finite difference with four points of reference. If a < b < c < d < h, the derivative of f at b is calculated as f(a) - 8f(b) + 8f(d) - f(h), divided by 3(h-a)."""
    dydxcenter = numpy.zeros(y.shape,float)
    dydxcenter[2:-2] = (y[0:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:])/(12*(x[2:-2] - x[1:-3]))
    dydxcenter[0] = (y[1]-y[0])/(x[1]-x[0])
    dydxcenter[-1] = (y[-1]-y[-2])/(x[-1] - x[-2])
    dydxcenter[1] = (y[1] - y[3])/(x[1]-x[3])
    dydxcenter[-2] = (y[-1]-y[-3])/(x[-1] - x[-3])
    return dydxcenter