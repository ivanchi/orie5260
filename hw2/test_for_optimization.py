import numpy as np
import scipy.optimize as opt
import sys

if __name__ == '__main__':
    #Define Rosenbrock function with n=3
    f = lambda x: (100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2) + (100 * (x[2] - x[1]**2)**2 + (1 - x[1])**2)
    #Select initial points
    points = [-10000, -5000, - 500, -10, -1, 0, 1, 10, 500, 5000, 10000]
    mini = sys.maxsize
    #Using different initial points, find the minium value
    for x1 in points:
        for x2 in points:
            for x3 in points:
                x0 = np.array([x1, x2, x3])
                y = opt.minimize(f, x0, method='BFGS')
                if y.fun < mini:
                    mini = y.fun
                    ans = y.x
                    initials = np.array(x0)
    print("minimum value: ", mini)
    print("initial points: ", initials)
    print("optimal solution: ", ans)
