import numpy as np
import pandas as pd
import os
import random
#import matplotlib.pyplot as plt
import time
import pytest


'''The purpose of this script is to calculate
the necessary parameters for Energy Consumption in an E-Auto'''

#Calculate the Total Road Force acting on the car
def total_resistive_force(f_inertia, f_friction, f_wind, f_slope = 0):
    eff_f_t_start = time.perf_counter()
    f_t = np.sum(f_inertia, f_slope, f_friction, f_wind); #Total Road Force f_t in N
    return f_t

#Calculate the Interial Force of car
def resistive_inertia(v_top, t_end, t_init =0, v_init = 0, m_car = 2200):
    a_car = ( (v_top - v_init) / (t_end - t_init) )
    f_inertia = m_car * a_car
    return f_inertia

#Calculate the forces acting on car on a slope
def resistive_gradient (alpha_s, g=9.81, m_car=2200):
    '''Insert Description here'''
    try:
        f_s = m_car * g * np.sin(alpha)
        return f_s
    except ValueError as ve:
        print(ve)

#Calculation frictional losses of car
def resistive_friction(alpha_s, c_rr, g=9.81,m=2200):
    '''This function will calculate the frictional force acting on a car
    
    >The inputs are:
    
    ---> alpha_s in [-] gives the slope of road to horizontal
    
    ---> c_rr in [-] gives the road rolling resistance coefficient
    
    ---> g in [ms^-2] gives the gravitional acceleration
    The deafault value of g is 9.81 ms^-2
    
    ---> m_car in [kg] gives the mass of the vehicle.
    The default value is 2200 kg.

    '''
    
    f_r = m * g * c_rr * np.cos(alpha_s)

    return f_r

#Calculate the air drag acting on car
def resistive_drag(rho, c_d, frontal_area, v_car = 10):
    '''Insert misc'''
    user_input = input('Do you want to calculate top speed? Enter to skip')
    if user_input:
        try:
            v_car_top = 30
            f_a = 0.5 * rho * c_d * frontal_area * v_car_top
        except ValueError as ve:
            print(ve)
    else:
        f_a = 0.5 * rho * c_d * frontal_area * v_car
    
    return f_a





if __name__ == '__main__':
    