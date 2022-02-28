import math


def area_of_regular_polygon():
    num_of_sides = int(input('Input number of sides: '))
    length_of_sides = int(input('Input the length of a side: '))
    
    perimeter = num_of_sides * length_of_sides

    apothem = length_of_sides / (2 * math.tan(math.pi / num_of_sides)) 
    area = 0.5 * apothem * perimeter 
    print(f'The area of the polygon is: {round(area, 2)}')

area_of_regular_polygon()