import math
bricks = int(input())
workers = int(input())
cars = int(input())

courses = math.ceil(bricks / (workers * cars))
print(courses)