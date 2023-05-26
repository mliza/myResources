#!/opt/homebrew/bin/python3.9 
'''
    Date:   04/17/2023
    Author: Martin E. Liza
    File:   particle_in_cell_method.py
    Def:

    Author		Date		Revision
    ----------------------------------------------------
    Martin E. Liza	04/17/2023	Initial version.
'''
import IPython 
import numpy as np 
import scipy.constants as s_consts
import matplotlib.pyplot as plt 



# Makes a mesh with constant spacing 
def make_mesh(nx, ny, lx, ly):
    '''
        nx = # of grid points on x
        lx = total length on x 
        ny = # of grid points on y
        ly = total length on y 
    '''
    dx = np.linspace(0, lx, nx)
    dy = np.linspace(0, ly, ny)
    X, Y = np.meshgrid(dx, dy) 
    return X, Y

def deby_lenght(electron_Temperature, ):
    k_B = s_consts.Boltzmann #[J/k] 
    e_0 = s_consts.epsilon_0 #[F/m] 
    m_e = s_consts.m_e       #[kg] 
    q_e = s_consts.e         #[C] 

def compute_charge_density(ni, ne):
    '''
    ni = # density of ions [ions/m3]
    ne = # density of electrons [electrons/m3] 
    '''
    charge_density = s_consts.e * (ne - ni)
    return charge_density #[C/m3] 

def compute_electric_potential(charge_density, X_grid, Y_grid): 
    '''
    charge_density = [C/m3]
    '''
    # This can be an input from simulation 
    dielectric_const_m = s_consts.epsilon_0 #[F/m]
    # Source term of Poisson's equation
    source_term  = - char_density / dielectric_const_m #[V/m3] 
    x_len, y_len = np.shape(X)                         #[m]  

    
    electric_potential = 0
    return electric_potential #[V] 

def compute_electric_field():
    electric_field = 0 
    return electric_field #[V/m] 

if __name__ == "__main__":
    # Input parameters #
    n0   = 1E12 # number density [particles/m3]
    phi0 = 0 # initial potential [V] 
    Te   = 1 # electron temperature [eV]



    # Mesh Generation #
    nx = 10
    ny = 7
    lx = 10     #[m]
    ly = 5      #[m] 
    dx = np.linspace(0, lx, nx)
    dy = np.linspace(0, ly, ny)
    X, Y = np.meshgrid(dx, dy) 

    # Compute Charge Density #




    IPython.embed(colors = 'Linux') 

    
