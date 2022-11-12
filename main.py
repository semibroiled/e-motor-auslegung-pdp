import numpy as np
import pandas
import random
import matplotlib.pyplot as plt
import time
import pytest


'''The purpose of this script is to calculate
the necessary parameters for Energy Consumption in an E-Auto'''

#Calculate the Total Road Force acting on the car

def total_road_force (f_inertia, f_friction, f_wind, f_slope = 0):
    eff_f_t_start = time.perf_counter();
    f_t = np.sum(f_inertia, f_slope, f_friction, f_wind); #Total Road Force f_t in N
    return f_t

#Calculate the Intertial Force of car

def car_inertia (v_top, t_end, t_init =0, v_init = 0, m_car = 2200):
    a_car = ( (v_top - v_init) / (t_end - t_init) );
    f_inertia = m_car * a_car