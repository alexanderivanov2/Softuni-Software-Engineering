import math

volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

water = pipe_1 * hours + pipe_2 * hours

if volume >= water:
    x = int(water / (volume / 100))
    y = int(pipe_1 * hours / water * 100)
    z = int(pipe_2 * hours / water * 100)
    print(f"The pool is {x}% full. Pipe 1: {y}%. Pipe 2: {z}%.")
else:
    x = math.trunc(water - volume)
    print(f"For {hours} the pool overflows with {x} liters.")
