start = int(input())
end = int(input())

a = 5
b = -12
c = 47
d = 7
e = -32
no = 0
n1 = ord("a")
n2 = ord("e")
combination = ""
count = 0
have = True
weight = 0

for s1 in range(n1 , n2 + 1):
    for s2 in range(n1, n2 + 1):
        for s3 in range(n1, n2 + 1):
            for s4 in range(n1, n2 + 1):
                for s5 in range(n1 , n2 + 1):
                    combination = chr(s1) + chr(s2) + chr(s3) + chr(s4) + chr(s5)
                    combination1 = combination
                    combination1 = "".join(dict.fromkeys(combination1))
                    for digit in combination1:
                        count += 1
                        if digit == ("a"or "A"):
                            chr1 = a
                        elif digit == ("b" or "B"):
                            chr1 = b
                        elif digit == ("c" or "C"):
                            chr1 = c
                        elif digit == ("d" or "E"):
                            chr1 = d
                        elif digit == ("e" or "E"):
                            chr1 = e
                        else:
                            chr1 = no
                        weight += count * chr1
                        chr1 = 0
                    if start <= weight <= end:
                        print(combination, end=" ")
                        have = False
                    weight = 0
                    count = 0

if have:
    print("No")