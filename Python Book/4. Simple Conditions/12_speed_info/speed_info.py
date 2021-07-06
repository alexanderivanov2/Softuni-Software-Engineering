speed = float(input())
if speed <= 10:
    print("slow")
elif 50 >= speed > 10:
    print("average")
elif 150 >= speed > 50:
    print("fast")
elif 1000 >= speed > 150:
    print("ultra fast")
elif speed > 1000:
    print("extremely fast")