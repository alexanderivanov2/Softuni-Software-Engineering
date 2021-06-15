import math

I = float(input()) * 100
W = float(input()) * 100 - 100
height_workplace = math.floor(I / 120)
width_workplace = math.floor(W / 70)
workplaces = height_workplace * width_workplace - 3
print(workplaces)