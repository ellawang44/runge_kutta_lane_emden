from __future__ import division, print_function

# define functions used in integrate
def f(x, y, z):
    return z

def g(x, y, z, n):
    return -y**n-2/x*z

# integrate
def integrate(x_0, y_0, z_0, n, t_step):
    '''Integrates one time step'''
    k_0 = t_step * f(x_0, y_0, z_0)
    l_0 = t_step * g(x_0, y_0, z_0, n)
    k_1 = t_step * f(x_0+1/2*t_step, y_0+1/2*k_0, z_0+1/2*l_0)
    l_1 = t_step * g(x_0+1/2*t_step, y_0+1/2*k_0, z_0+1/2*l_0, n)
    k_2 = t_step * f(x_0+1/2*t_step, y_0+1/2*k_1, z_0+1/2*l_1)
    l_2 = t_step * g(x_0+1/2*t_step, y_0+1/2*k_1, z_0+1/2*l_1, n)
    k_3 = t_step * f(x_0+t_step, y_0+k_2, z_0+l_2)
    l_3 = t_step * g(x_0+t_step, y_0+k_2, z_0+l_2, n)
    x_1 = x_0 + t_step
    y_1 = y_0 + 1/6 * (k_0+2*k_1+2*k_2+k_3)
    z_1 = z_0 + 1/6 * (l_0+2*l_1+2*l_2+l_3)
    return (x_1, y_1, z_1)
