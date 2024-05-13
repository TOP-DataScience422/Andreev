#Все A C E G нечетные и B D F H четные - всегда черные, значит - A C E G четные и B D F H нечетные - всегда белые
first_coordinate = input()
second_coordinate = input()
first_coordinate = list(first_coordinate)
second_coordinate = list(second_coordinate)

if(first_coordinate[0] in ["a", "c", "e", "g"]):
    if(int(first_coordinate[1]) % 2 == 0):
        first_coordinate_color = 'white'
    else: first_coordinate_color = 'black'
elif(first_coordinate[0] in ["b", "d", "f", "h"]):
    if(int(first_coordinate[1]) % 2 == 0):
        first_coordinate_color = 'black'
    else: first_coordinate_color = 'white'

if(second_coordinate[0] in ["a", "c", "e", "g"]):
    if(int(second_coordinate[1]) % 2 == 0):
        second_coordinate_color = 'white'
    else: second_coordinate_color = 'black'
elif(second_coordinate[0] in ["b", "d", "f", "h"]):
    if(int(second_coordinate[1]) % 2 == 0):
        second_coordinate_color = 'black'
    else: second_coordinate_color = 'white'
    
if(first_coordinate_color == second_coordinate_color): print('да')
else: print('нет')

# PS D:\AcademyTop\Python\Andreev\2024.04.13> python .\4.py
# a1
# b2
# да