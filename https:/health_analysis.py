# import pandas and rename to pd
import pandas as pd
# import numpy and rename to np
import numpy as np 

#Create the following variables and assign values: 
Age = 32
Sex = 'Male'
Height = 160
Weight = 109
Name = "Billy Bob"

#bloodpressure for 08/18/2023
systolic = 138
diastolic = 90

#dictionary
past_blood_pressure_data = {
    "08/17/2023": {
        "Systolic": 142,
        "Diastolic": 88
    },
    "08/16/2023": {
        "Systolic": 138,
        "Diastolic": 90
    },
    "08/15/2023": {
        "Systolic": 140,
        "Diastolic": 100
    }
}

#list
MAP: "past 3 days" = {223.3, 226, 113.3}


print('\n')
print('Patient', Name, 'is a', Age, 'year old', Sex, 'has a reported blood pressure for 08/18/2023 of:', systolic, "/", diastolic)


print('\n')
print(Name, 'also presented with the following vitals:', past_blood_pressure_data, 'Mean Arterial Pressure Reported', MAP)
print('\n')

#if-else statement 
if systolic < 120:
    print('\n')
    print("This blood pressure is normal")
elif systolic >= 120 and systolic <= 129 and diastolic < 80:
    print('\n')
    print("This blood pressure is prehypertensive")
elif systolic >= 130 and systolic <= 139 or diastolic >= 80 and diastolic <= 89:
    print('\n')
    print("This is blood pressure is stage 1 hypertensive")
else:
    print("This is blood pressure is stage 2 hypertensive")

    

print('\n')
print("Please notify PCP")
print('\n')
