import numpy as np
import pandas as pd
import os
import random
#import matplotlib.pyplot as plt
import time
import pytest


'''The purpose of this script is to calculate
the necessary parameters for Energy Consumption in an E-Auto'''

#Calculate the Interial Force of car
def resistive_inertia(v_car, t_end, t_init =0, v_init = 0, m_car = 2200):
    '''Insert misc'''
    #Check input types
    #
    #

    user_input = input('Do you want to calculate with top speed? Enter to skip')
    if user_input:
        try:
            v_car_top = 30 #Cars topspeed in kmh
            v_car_top_in_ms = v_car_top / 3.6 #Cars topspeed in ms
            a_car = ( (v_car_top_in_ms - v_init) / (t_end - t_init) )
        except ValueError as ve:
            print(ve)
    else:
         a_car = ( (v_car - v_init) / (t_end - t_init) )
    a_car = ( (v_car - v_init) / (t_end - t_init) )
    f_inertia = m_car * a_car
    return f_inertia

#Calculate the forces acting on car on a slope
def resistive_gradient (alpha_s, g=9.81, m_car=2200):
    '''Insert Description here'''
    #Check types here
    #
    #
    try:
        f_s = m_car * g * np.sin(alpha_s)
    except ValueError as ve:
        print(ve)
    return f_s

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

#Calculate the Total Road Force acting on the car
def total_resistive_force(f_inertia, f_friction, f_wind, f_slope = 0):
    eff_f_t_start = time.perf_counter()
    f_t = np.sum(f_inertia, f_slope, f_friction, f_wind); #Total Road Force f_t in N
    return f_t



if __name__ == '__main__':
    i = 5 #Zeitverzog
    print('Starting script...')
    time.sleep(i)
    
    
    print('Calculating intertial resistance...')
    time.sleep(i)
    vehicle_speed = int(input(f'Give the speed of your car travelling in kmh'))*3.6 #Cars travelling speed, usually 10kmh
    time_frame =  int(input(f'Give the time required for your car travelling to accelerate to topspeed in s')) #Cars time required to accelerate
    f_i = resistive_inertia(vehicle_speed, time_frame)
    time.sleep(i)
    print(f'The inertial resistance of your car is {f_i} N)')
    time.sleep(i)

    print('Calculating resistance on a slope...')
    time.sleep(i)
    gradient_slope = int(input(f'The angle gradient of your slope in degrees')) #Slope angle
    f_slope = resistive_gradient(gradient_slope)
    time.sleep(i)
    print(f'The gradient resistance of your car is {f_slope} N)')
    time.sleep(i)

    print('Calculating frictional resistance...')
    time.sleep(i)
    gradient_slope = int(input(f'The angle gradient of your slope in degrees')) #Slope angle
    f_slope = resistive_gradient(gradient_slope)
    time.sleep(i)
    print(f'The gradient resistance of your car is {f_slope} N)')
    time.sleep(i)



