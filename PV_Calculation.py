# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

building_width = 8 
building_length = 28
roof_angle = 22
pv_width = 1690 
pv_length = 1046 
pv_power = 400 

roof_angle_rad = math.radians(roof_angle)
pv_width_m = pv_width / 1000
pv_lengthth_m = pv_length / 1000


rw =  building_width / math.cos(roof_angle_rad)
rl = building_length 


no_p = (rl // pv_lengthth_m ) * (rw // pv_width_m )


power_capacity = no_p * pv_power / 1000  


print("Number of panels:", int(no_p))
print("Total power capacity (kWp):", power_capacity)
print (rw)