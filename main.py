from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np
import runge_kutta
import argparse
# typing LaTeX code in matplotlib graphs
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# parsers so you don't need to edit the code to test it
parser = argparse.ArgumentParser(description='runge-kutta integration of the Lane-Emden equation.')
parser.add_argument('-n', '--nthorder', metavar = 'nth-order', type = float, default = 0, help='Change the order of the integrated function, default value is 0.')
parser.add_argument('-t', '--tstep', metavar = 'time_step', type = float, default = 0.05, help='Change the time step of integration, default value is 0.05.')
parser.add_argument('--check', action = 'store_true', default = False, help='Change if analytical plot is shown or not for n = 0 and n = 1, default is off.')
parser.add_argument('--eval', action = 'store_true', default = False, help='Change if xi_1 and d theta/d xi (xi_1) is printed or not, default is off.')

if __name__ == '__main__':
    args = parser.parse_args()
    # define integration variables
    n = args.nthorder
    t_step = args.tstep

    # define initial conditions
    x_0 = 1e-50 # need some small value that is close to 0 but not exactly 0
    y_0 = 1
    z_0 = 0

    # do the integration and compile the results into two lists
    xs = [x_0]
    ys = [y_0]
    while y_0>0:
        x_0, y_0, z_0 = runge_kutta.integrate(x_0, y_0, z_0, n, t_step)
        xs.append(x_0)
        ys.append(y_0)

    # checking that the runge-kutta method is valid
    if args.check:
        if n == 0:
            def check(x):
                return 1 - x**2/6
        elif n == 1:
            def check(x):
                return np.sin(x)/x

    if args.eval:
        print('xi_1 =', x_0)
        print('d theta / d xi (xi_1) =', z_0)

    # plots
    plt.plot(xs, ys, label = 'runge-kutta')
    if (args.check and n==0) or (args.check and n==1):
        plt.plot(xs, np.vectorize(check)(xs), label = 'actual')
        plt.legend()
    plt.xlabel(r'$\xi$')
    plt.ylabel(r'$\theta$')
    plt.show()
