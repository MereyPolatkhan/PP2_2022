def area_of_trapezoid():
    height = int(input('Height: ')) 
    first = int(input('Base, first value: ')) 
    second = int(input('Base, second value: '))

    area = (first + second) / 2 * height

    print(f'Expected Output: {area}')

area_of_trapezoid()