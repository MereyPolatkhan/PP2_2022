# python math_1

import math 

# print(math.pi)

def degree_to_radian():
  degree = int(input("Input degree: "))
  print(f'Output radian: {degree * math.pi / 180}')


degree_to_radian()