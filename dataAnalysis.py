##                                                  ##
#Python 3 Script for data plotting and analysis      #
#Project Data-Droid                                  #
#Author: Joel M. Vaz                                 #   
##   

######################################################
#Imports 
import sys #Allows argv[] use
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import json

#Hard Coded file name
#File must be in the same folder as script
filename= "droid-data-export.json"

with open(filename, 'r') as f:
    data= json.load(f)
#data is a dictionary

#Get Acceleration from trip 1 of driver 1
#Data Set Example from dictionary" 
#
##
# 999 {'1': {'-Lvq47hW67bzFI6p5_-d':{'acceleration_x': 0.002, 'acceleration_y': 0.004, 'acceleration_z': -0.001, 'date': '11-12-2019', 'label': 'good', 'latitude': 41.1527084, 'longitude': -8.6082637, 'rotation_x': -0.001, 'rotation_y': 0.001, 'rotation_z': -0.058, 'speed': 0, 'time': '17:49:31'}, 

#
##
for driverId in data:
    print("Driver' Id: " + driverId) #Prints the Driver ids
    for tripId in data.get(driverId):
        print("Trip Id: " + tripId) #Prints the Trip Ids
        for dataSet in data.get(driverId).get(tripId):
            print("Data Set: " + dataSet)
