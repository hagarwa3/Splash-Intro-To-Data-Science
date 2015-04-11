import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

def solve1():
    x = np.array([-1.02494, -0.949898, -0.866114,-0.773392, -0.671372,
                  -0.559524,-0.437067,-0.302909, -0.155493, -0.007464], dtype = "float_")
    y = np.array([-0.389269, -0.322894, -0.265256, -0.216557, -0.177152,
                  -0.147582, -0.128618, -0.121353, -0.127348,-0.148885], dtype = "float_")
    rhs = x**2
    col1 = y*y
    col2 = x*y
    col3 = x
    col4 = y
    col5 = np.ones(len(x))
    A = np.array([col1,col2,col3,col4,col5]).T
    Q, R = la.qr(A)
    Qt = Q.T
    c1 = np.dot(Qt, rhs)
    result = la.solve(R, c1)
    residual = rhs - np.dot(A, result)
    norm_residual = la.norm(residual, np.inf)
    print "Coefficients:"
    print result
    print "Residual vector: "
    print residual
    print "Residual inf norm:"
    print norm_residual
    return result

def solve2():
    x = np.array([-1.02494, -0.949898, -0.866114,-0.773392, -0.671372,
                  -0.559524,-0.437067,-0.302909, -0.155493, -0.007464], dtype = "float_")
    y = np.array([-0.389269, -0.322894, -0.265256, -0.216557, -0.177152,
                  -0.147582, -0.128618, -0.121353, -0.127348,-0.148885], dtype = "float_")    
    rhs = x**2
    col1 = y
    col2 = np.ones(len(x))
    A = np.array([col1,col2]).T
    Q, R = la.qr(A)
    Qt = Q.T
    c1 = np.dot(Qt, rhs)
    result = la.solve(R, c1)
    residual = rhs - np.dot(A, result)
    norm_residual = la.norm(residual, np.inf)
    print "Coefficients:"
    print result
    print "Residual vector: "
    print residual
    print "Residual inf norm:"
    print norm_residual
    return result

def plot():
    x0 = np.array([-1.02494, -0.949898, -0.866114,-0.773392, -0.671372,
                  -0.559524,-0.437067,-0.302909, -0.155493, -0.007464], dtype = "float_")
    y0 = np.array([-0.389269, -0.322894, -0.265256, -0.216557, -0.177152,
                  -0.147582, -0.128618, -0.121353, -0.127348,-0.148885], dtype = "float_")    
    coe1 = solve1()
    coe2 = solve2()
    x = np.linspace(np.min(x0), np.max(x0), 20, "float_")
    y1 = (-(coe1[1]*x+coe1[3]) - np.sqrt((coe1[1]*x+coe1[3])**2 - 4*coe1[0]*(coe1[2]*x+coe1[4]-x**2)))/(2*coe1[0])
    y2 = (x**2 - coe2[1])/coe2[0]
    plt.plot(x, y1, color='red')
    plt.plot(x, y2, color='blue')
    #plt.plot(x0, y0, "gs")
    plt.legend(["Ecllipse", "Parabola", "Observations"], loc=2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    #plt.savefigs("out.png")
plot()
