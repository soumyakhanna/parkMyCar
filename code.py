'''
Created on Feb 15, 2020

@author: Aman Kothari
'''
from time import gmtime
'''
Assumption:
1. Parking lot remains empty during the night i.e before 5AM
2. Distances of rows in the big parking lots near the building are 
    almost as close as the smaller parking lots.
3. Equal distribution of incoming employees among both buildings 
    is assumed.
byulding_type: 
            1 - Building A
            2 - Building B
'''
percentage_lot = [0, 0, 0, 0, 0, 0]
count_lot = [0, 0, 0, 0, 0, 0]
spaces = [0, 75, 837, 852, 96, 750]  


def priority_parking(building_type: int, hour: int) -> int:
    #hour = gmtime().tm_hour
    if (hour <= 6):
        if (building_type == 1):
            if (percentage_lot[3] < 12.5):
                return 3
            else:
                return 2
            
        else:
            if (percentage_lot[5] < 12.5):
                return 5
            else:
                return 3
    elif (hour <= 7):
        if (building_type == 1):
            if (percentage_lot[1] < 100):
                return 1
            elif(percentage_lot[2] < 45):
                return 2
            else:
                return 3
        else:
            if(percentage_lot[4] < 100):
                return 4
            else:
                return 5
    elif (hour <= 9):
        if (building_type == 1):
            if (percentage_lot[1] < 100):
                return 1
            elif (percentage_lot[2] < 100):
                return 2
            elif (percentage_lot[3] < 100):
                return 3
            else:
                return -1
        else:
            if(percentage_lot[4] < 100):
                return 4
            elif (percentage_lot[5] < 100):
                return 5
            else:
                return -1
    elif (hour <= 10):
        count = 1
        while (count <= 5):
            if (percentage_lot[count] < 100):
                return count
            count += 1
    elif (hour <= 12):
        if (building_type == 1):
            count = 1
            while (count <= 3):
                if (percentage_lot[count] < 100):
                    return count
                count += 1
        else:
            if (percentage_lot[4] < 100):
                return 4
            else:
                return 5
    
                
    return 0

def percentage_calculation(parking_lot: int):
    percentage_lot[parking_lot] = count_lot[parking_lot] * 100 / spaces[parking_lot]

def arrival(parking_lot: int):
    count_lot[parking_lot] += 1

def departure(parking_lot: int):
    count_lot[parking_lot] -= 1
    percentage_calculation