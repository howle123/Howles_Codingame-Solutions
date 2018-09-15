import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thor_x = initial_tx
thor_y = initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if remaining_turns <= 0:
        print('out of turns')
    
    move_y = ''
    move_x = ''
    
    if thor_y > light_y:
        move_y = 'N'
        thor_y -= 1
    elif thor_y < light_y:
        move_y = 'S'
        thor_y += 1
        
    if thor_x > light_x:
        move_x = 'W'
        thor_x -= 1
    elif thor_x < light_x:
        move_x = 'E'
        thor_x += 1  

    move_yx = move_y + move_x 
    print(move_yx)
    
    