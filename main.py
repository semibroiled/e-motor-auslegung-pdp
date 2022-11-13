import numpy as np
import pandas as pd
import os
import random
#import matplotlib.pyplot as plt
import time
import pytest


'''The purpose of this script is to calculate
the necessary parameters for Energy Consumption in an E-Auto'''



#Experimental constants and coefficients from table    
    
rho = { 'air1': 1.27554, #Air density with water load at
        'air2': None #Air density IUPAC
    }

c_rr = {'pavement':1.05, #block shape
            }



#Calculate the Interial Force of car
def resistive_inertia(v_car=10, t_end=5, t_init =0, v_init = 0, m_car = 2200):
    '''Insert misc'''
    #Check input types
    #
    #
    user_input = input('Do you want to calculate with top speed? Press Enter to skip and calculate at Operational Speed. Enter YES to calculate at Topspeed: \n')


    if user_input:
        try:
            v_car_top = 30 #Cars topspeed in kmh
            print(f'Car\'s Topspeed is {v_car_top} kmh')
            v_car_top_in_ms = v_car_top / 3.6 #Cars topspeed in ms
            a_car = ( (v_car_top_in_ms - v_init) / (t_end - t_init) )
        except ValueError as ve:
            print(ve)
    else:
         #vehicle_speed = int(input(f'Give the speed of your car travelling in kmh'))*3.6 #Cars travelling speed, usually 10kmh
         #time_frame =  int(input(f'Give the time required for your car travelling to accelerate to topspeed in s')) #Cars time required to accelerate
         v_car_operational_in_kmh = v_car
         v_car_operational_in_ms = v_car_operational_in_kmh/3.6
         print(f'Car\'s speed at normal operation is {v_car_operational_in_kmh} kmh')
         a_car = ( (v_car_operational_in_ms - v_init) / (t_end - t_init) )

    f_inertia = m_car * a_car
    return f_inertia

#Calculate the forces acting on car on a slope
def resistive_gradient (alpha_s=10, g=9.81, m_car=2200):
    '''Insert Description here'''
    #Check types here
    #
    #
    try:
        f_s = abs(m_car * g * np.sin(alpha_s))
    except ValueError as ve:
        print(ve)
    return f_s

#Calculation frictional losses of car
def resistive_friction(alpha_s=10, c_rr=1, g=9.81,m=2200):
    '''This function will calculate the frictional force acting on a car
    
    >The inputs are:
    
    ---> alpha_s in [-] gives the slope of road to horizontal
    
    ---> c_rr in [-] gives the road rolling resistance coefficient
    
    ---> g in [ms^-2] gives the gravitional acceleration
    The deafault value of g is 9.81 ms^-2
    
    ---> m_car in [kg] gives the mass of the vehicle.
    The default value is 2200 kg.

    '''
    
    f_r = abs(m * g * c_rr * np.cos(alpha_s))

    return f_r

#Calculate the air drag acting on car
def resistive_drag(fluid_density='air1', c_d='placeholder1', frontal_area = 1.5**2, v_wind=0, v_car = 10):
    '''Insert misc'''

    air_density = rho[fluid_density]
    c_d = 1
    user_input = input(f'Do you want to calculate at nominal wind speed of 0kmh? Press Enter or enter Yes to get speed prompt')
    if user_input:

        wind_speed_in_ms= int(input(f'The wind speed in kmh:\n'))*3.6 #wind speed in ms
        v_wind = wind_speed_in_ms.copy()
    
    else:
        pass

    user_input = input('Do you want to calculate drag at top speed? Enter to skip and calculate at 10kmh')
    if user_input:
        try:
            v_car_top = 30
            f_a = 0.5 * air_density * c_d * frontal_area * ((v_car_top-v_wind)**2)
        except ValueError as ve:
            print(ve)
    else:
        f_a = 0.5 * air_density * c_d * frontal_area * ((v_car-wind_speed)**2)
    
    return f_a

#Calculate the Total Road Force acting on the car
def total_resistive_force(f_inertia, f_friction, f_wind, f_slope = 0):
    eff_f_t_start = time.perf_counter()
    f_t = f_inertia+ f_slope+ f_friction+ f_wind #Total Road Force f_t in N
    return f_t



if __name__ == '__main__':
    i = 2 #Zeitverzog
    print('Run script...')
    time.sleep(i)
    
    
    print('Calculate intertial resistance...')
    time.sleep(i)
    # try:
    #     #vehicle_speed = int(input(f'Give the speed of your car travelling in kmh'))*3.6 #Cars travelling speed, usually 10kmh
    #     #time_frame =  int(input(f'Give the time required for your car travelling to accelerate to topspeed in s')) #Cars time required to accelerate
    # except:
    #     None
    f_i = resistive_inertia()
    time.sleep(i)
    print(f'The inertial resistance of your car is {f_i} N')
    time.sleep(i)

    
    print('Calculate resistance on a slope...')
    time.sleep(i)
    try:
        user_input = input('Do you want to calculate slope resistance? Press Enter to skip and calculate nominally at 13\% \rise. Or enter YES to calculate at flat surfaces: \n')
        if user_input:
            #gradient_slope = float(input(f'The angle gradient of your slope in degrees')) #Slope angle, normally upto 10 degrees in German Roads
            f_slope = resistive_gradient(alpha_s=0) #assuming flat surface
        else:
            f_slope = resistive_gradient() #assuming nominal rise of 13%
    except:
        None
    
    time.sleep(i)
    print(f'The gradient resistance of your car is {f_slope} N')
    time.sleep(i)

    print('Calculate frictional resistance...')
    time.sleep(i)
    try:
        user_input = input('Do you want to calculate friction nominally? Press Enter to skip and calculate nominally or yes to edit: \n')
        if user_input:
            frictional_coefficient = float(input(f'The frictional coefficient between tires and road:\n')) #frictional coefficient
            f_f = resistive_friction(c_rr=frictional_coefficient)
        else:
            f_f = resistive_friction()
    except:
        None

    time.sleep(i)
    print(f'The frictional resistance of your car is {f_f} N')
    time.sleep(i)

    print('Calculate air drag resistance...')
    time.sleep(i)
    #car_height= 1.5
    #car_width =1.5 #in m

    #frontal_area = car_height * car_width#Slope angle



    f_drag = resistive_drag()
    time.sleep(i)
    print(f'The frictional resistance of your car is {f_drag} N)')
    time.sleep(i)

    total_force = total_resistive_force(f_i, f_f, f_drag)
    print(f'Total Resistance is {total_force} N \n Percentage of drag is {(f_drag/total_force)*100}% \n Percentage of friction is {(f_f/total_force)*100}% \n Percentage of{None}{None}')

    try:
        with open('e_eff.txt', 'w') as parameter:
            parameter.writelines(f'''
            The individual forces are:\n
            Inertial force = {f_i}\n
            Frictional force = {f_f}\n
            Drag force = {f_drag} \n
            Slope resistance = {f_slope}\n

            The total force is:\n
            Total Force = F_inertia + F_friction + F_drag + F_slope = {None}{None}{None}{None} = {total_force}
            
            '''

            )

    except ValueError as ve:
        print(ve)