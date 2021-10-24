import math
n = int(input())
prime = True

for i in range(2, int((math.sqrt(abs(n))) + 1)):
    if n % i == 0:
        prime = False
        break

if prime and n > 1:
    print("prime")
else:
    print("Not prime")