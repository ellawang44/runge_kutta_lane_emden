# 4th order Runge-Kutta for Lane-Emden equation  
Numerically integrate the Lane-Emden equation using the 4th order Runge-Kutta method.  

# Download  
To download the files, navigate to the directory where you want the folder in terminal, then type: `git clone https://github.com/ellawang44/runge_kutta_lane_emden`

# Running the Program  
To run the program, simply type `python main.py` in the terminal. This will run the numerical integration for `n = 0`.

There are optional arguments which will change the numerical integration being run and the outputs produced by the program.

To change the order of the Lane-Emden function being integrated, use the flag `-n` or `--nthorder`. e.g: `'-n 1'` will change the order to 1.  

To change the time step per integration, use the flag `-t` or `--tstep`. e.g: `-t 0.01` will change the time step to 0.01.

To plot the analytical solution for `n=0` and `n=1` on the same graph as the numerical solution, use the flag `--check`. Note that this is only valid for `n=0` and `n=1` as other values of `n` do not have an analytical solution.

To print the value of \xi and \frac{d \theta}{d \xi} at \xi = \xi_1 (i.e at \theta = 0), use the flag `--eval`.

# Dependencies
This program was written in Python, and runs on both Python 2 and 3 producing identical results.  
## Required Python Packages
The required Python packages include: `matplotlib.pyplot`, `numpy`, and `argparse`
