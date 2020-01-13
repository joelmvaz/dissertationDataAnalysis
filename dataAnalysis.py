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
import seaborn as sns
import json

def mkdir_p(mypath):
    '''Creates a directory. equivalent to using mkdir -p on the command line'''
    from errno import EEXIST
    from os import makedirs,path

    try:
        makedirs(mypath)
    except OSError as exc:
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise

accX= []
accY= []
accZ= []
lat= []
longi= []
speed= []
time= []
timePlt= []
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
    for tripId in data.get(driverId):
        for dataSet in data.get(driverId).get(tripId):
            for sensorsLst in data.get(driverId).get(tripId).get(dataSet):
                if(sensorsLst=="acceleration_x"):
                    accX.append(data.get(driverId).get(tripId).get(dataSet).get(sensorsLst))
                if(sensorsLst=="acceleration_y"):
                    accY.append(data.get(driverId).get(tripId).get(dataSet).get(sensorsLst))
                if(sensorsLst=="acceleration_z"):
                    accZ.append(data.get(driverId).get(tripId).get(dataSet).get(sensorsLst))
                if(sensorsLst=="latitude"):
                    lat.append(data.get(driverId).get(tripId).get(dataSet).get(sensorsLst))
                if(sensorsLst=="longitude"):
                    longi.append(data.get(driverId).get(tripId).get(dataSet).get(sensorsLst))
                if(sensorsLst=="speed"):
                    speed.append(data.get(driverId).get(tripId).get(dataSet).get(sensorsLst))
                if(sensorsLst=="time"):
                    time.append(data.get(driverId).get(tripId).get(dataSet).get(sensorsLst))

        ## This break represents a trip by the driver with id 1 
        break

    #Save plot part on folder with driver id, with trip id as figure name
    plt.figure()
    plt.xticks(rotation=45, ha='right')
    plt.plot(np.arange(0, len(time), 1).tolist(), accX)
    plt.title('Acceleartion X over time stamp')
    plt.xlabel('Time Stamp')

    # Create new directory
    output_dir= driverId
    mkdir_p("Plots/" + output_dir)

    plt.savefig("Plots/" + driverId + "/accX.png")
    plt.clf()

    plt.plot(np.arange(0, len(time), 1).tolist(), accY)
    plt.title('Acceleartion Y over time stamp')
    plt.xlabel('Time Stamp')
    plt.savefig("Plots/" + driverId + "/accY.png")
    plt.clf()

    plt.plot(np.arange(0, len(time), 1).tolist(), accZ)
    plt.title('Acceleartion Z over time stamp')
    plt.xlabel('Time Stamp')
    plt.savefig("Plots/" + driverId + "/accZ.png")
    plt.clf()

    if(speed):
        plt.plot(np.arange(0, len(time), 1).tolist(), speed)
        plt.title('Speed over time stamp')
        plt.xlabel('Time Stamp')
        plt.savefig("Plots/" + driverId + "/speed.png")
        plt.clf()

    accX= []
    accY= []
    accZ= []
    speed= []
    time= []

    print("Saved Plots for driver Id: " + driverId)

print("Data Plotting Script Ended\n")
