import numpy as np
import pandas as pd
import os
import random
import matplotlib.pyplot as plt
import time
import pytest


'''The purpose of this script is to calculate
the necessary parameters for Energy Consumption in an E-Auto'''



#Experimental constants and coefficients from table    
    
density = { 'air1': 1.27554, #Air density with water load at
        'air2': None #Air density IUPAC
    }

road_roll_coeff = {'pavement':1.05, #block shape
            }

drag_coeff = {'placeholder' : 1.23}

#Vehicle Parameters

cars = {'Weight': 2200,
        'Maximum Speed': 30,
        'Nominal Deployment Speed': 10,
        'Acceleration Time to Max Speed': 5,
        'Steepest Slope Angle': 10,
        'Typical Slope Angle':0,
        'Car Height': 1.5,
        'Car Width': 1.5}



#Calculate the Interial Force of car
def resistive_inertia(m_car, v_car_max, v_car_nom, t_end, t_init =0, v_init = 0):
    '''
    Inputs are: 
    
    m_car as mass of car or vehicle in kg,
    v_car_max as the maximum car velocity in ms^-1,
    v_car_nom as the nominal car velocity in ms^-1
    t_end as accelertion time take to prescribed speed in s. 

    Other Inputs are:

    t_init as initial time in s and
    v_init as initial speed in ms^-1

    Both of which are by default 0

    Output is the resistive Inertia of vehicle f_inertia_max and f_inertia_nom for both use cases in N 
    
    '''
    #Check input types

    #Convert Inputs to suitable calculable units
    try:
        print(f'Car\'s Topspeed is {v_car_max} kmh')
        v_car_max_in_ms = v_car_max / 3.6 #Cars topspeed in ms^-1
        v_car_nom_in_ms = v_car_nom / 3.6 #Cars nominal speed in ms^-1
    except ValueError as ve:
        print(ve)
    
    #Calculate with converted values
    try:
        a_car_max_in_ms2 =  (v_car_max_in_ms - v_init) / (t_end - t_init) #max accelertaion of car in ms^-2
        a_car_nom_in_ms2 = (v_car_nom_in_ms - v_init) / (t_end - t_init) #nominal acceleration of car in ms^-2
        f_inertia_max = m_car * a_car_max_in_ms2 #Inertial force in N
        f_inertia_nom = m_car * a_car_nom_in_ms2 #Inertial force in N
    except:
        pass

    return f_inertia_max, f_inertia_nom



#Calculate the forces acting on car on a slope
def resistive_gradient (m_car, alpha_s_max, alpha_s_nom, g=9.81):
    '''
    Inputs are: 
    
    m_car as mass of car or vehicle in kg,
    alpha_s_max as the maximum road steepness in degrees and
    alpha_s_nom as the typical road steepness in degrees.
    

    Other Inputs are:

    g as gravitational acceleration in ms^-2 with a default value of 9,8 

    Output is the resistive Slope forces acting on vehicle f_slope_max and f_slope_nom for both use cases in N 
    '''
    #Check input types

    #Calculate formulas
    try:
        print(f'Steepest road angle is {alpha_s_max}')
        f_slope_max = abs(m_car * g * np.sin(alpha_s_max)) #Maximum force acting on vehicle due to slope in N
        f_slope_nom = abs(m_car * g * np.sin(alpha_s_nom)) #Nominal force acting on vehicle due to slope in N
    except ValueError as ve:
        print(ve)

    return f_slope_max, f_slope_nom



#Calculation frictional losses of car
def resistive_friction(m_car, alpha_s_max, alpha_s_nom, c_rr, g=9.81):
    '''
    Inputs are: 
    
    m_car as mass of car or vehicle in kg,
    alpha_s_max as the maximum road steepness in degrees,
    alpha_s_nom as the typical road steepness in degrees and
    c_rr as the road rolling coefficient which is dimensionless.

    Other Inputs are:

    g as gravitational acceleration in ms^-2 with a default value of 9,8 

    Outputs are the f_rollfriction_max and f_rollfriction_nom in N

    '''
    try:
        f_rollfriction_max = abs(m_car * g * c_rr * np.cos(alpha_s_max))
        f_rollfriction_nom = abs(m_car * g * c_rr * np.cos(alpha_s_nom))
    except:
        pass
    
    return f_rollfriction_max, f_rollfriction_nom



#Calculate the air drag acting on car
def resistive_drag(rho, c_d, width_car, height_car, v_wind, v_car_max, v_car_nom):
    '''
    Inputs are: 
    
    m_car as mass of car or vehicle in kg,
    v_car_max as the maximum car velocity in ms^-1,
    v_car_nom as the nominal car velocity in ms^-1
    t_end as accelertion time take to prescribed speed in s. 

    Other Inputs are:

    t_init as initial time in s and
    v_init as initial speed in ms^-1

    Both of which are by default 0

    Output is the resistive Inertia of vehicle f_inertia_max and f_inertia_nom for both use cases in N 
    
    '''
    try:
        v_car_max_in_ms = 30/3,6
        v_car_nom_in_ms = 10/3,6
    except:
        pass
        
    try:
        f_drag_max = 0.5 * rho * c_d * width_car * height_car * ((v_car_max_in_ms)**2)
        f_drag_nom = 0.5 * rho * c_d * width_car * height_car * ((v_car_nom_in_ms)**2)
    except ValueError as ve:
        print(ve)
    
    return f_drag_max, f_drag_nom






#Calculate the Total Road Force acting on the car
def total_resistive_force(f_inertia, f_friction, f_drag, f_slope):

    '''
    
    '''
    #eff_f_t_start = time.perf_counter()
    f_total_max = f_inertia+ f_slope+ f_friction+ f_drag #Total Road Force f_t in N
    f_total_nom = f_inertia + f_slope + f_friction + f_drag #Toal Road Force f_t in N
    
    
    return f_total_max, f_total_nom



if __name__ == '__main__':
    i = 2 #Time Delay
    j = time.sleep(2) #Time Delay Practice
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