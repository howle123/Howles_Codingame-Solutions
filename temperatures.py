import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number_of_temperatures = int(input())  # the number of temperatures to analyse
closest_temp = 5526

if number_of_temperatures == 0:
    print('0')
else:
    for i in input().split():
        temp = int(i)
        if temp == 0:
            print('0')
        elif abs(temp) < abs(closest_temp):
            closest_temp = temp
        elif abs(temp) == abs(closest_temp) and temp != closest_temp:
            closest_temp = abs(temp)
        elif abs(temp) == abs(closest_temp) and temp == closest_temp:
            closest_temp = temp
            
    print(closest_temp)
