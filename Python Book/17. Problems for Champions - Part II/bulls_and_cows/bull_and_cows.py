secret_number = int(input())
bulls = int(input())
cows = int(input())
no_result = True
secret_number1 = secret_number
num4 = secret_number1 % 10
secret_number1 = secret_number1 // 10
num3 = secret_number1 % 10
secret_number1 = secret_number1 // 10
num2 = secret_number1 % 10
secret_number1 = secret_number1 // 10
num1 = secret_number1 % 10
sec_bulls = 0
sec_cows = 0

for n1 in range(1, 10):
    for n2 in range(1, 10):
        for n3 in range(1, 10):
            for n4 in range(1, 10):
                if num1 == n1:
                    sec_bulls += 1
                elif num1 != n1:
                    if n1 == num2 and n2 != num2:
                        sec_cows += 1
                    elif n1 == num3 and n3 != num3:
                        sec_cows += 1
                    elif n1 == num4 and n4 != num4:
                        sec_cows += 1
                if num2 == n2:
                    sec_bulls += 1
                elif num2 != n2:
                    if n2 == num1 and n1 != num1:
                        sec_cows += 1
                    elif n2 == num3 and n3 != num3 and (n1 != num3 or n1 == num1):
                        sec_cows += 1
                    elif n2 == num4 and n4 != num4 and (n1 != num4 or n1 == num1):
                        sec_cows += 1
                if num3 == n3:
                    sec_bulls += 1
                elif num3 != n3:
                    if n3 == num1 and n1 != num1 and (n2 != num1 or n2 == num2):
                        sec_cows += 1
                    elif n3 == num2 and n2 != num2 and (n1 != num2 or n1 == num1):
                        sec_cows += 1
                    elif n3 == num4 and n4 != num4 and (n1 != num4 or n1 == num1) and (n2 != num4 or n2 == num2):
                        sec_cows += 1
                if num4 == n4:
                    sec_bulls += 1
                elif num4 != n4:
                    if n4 == num1 and n1 != num1 and (n2 != num1 or n2 == num2) and (n3 != num1 or n3 == num3):
                        sec_cows += 1
                    elif n4 == num2 and n2 != num2 and (n1 != num2 or n1 == num1) and (n3 != num2 or n3 == num3):
                        sec_cows += 1
                    elif n4 == num3 and n3 != num3 and (n1 != num3 or n1 == num1) and (n2 != num3 or n2 == num2):
                        sec_cows += 1
                if sec_bulls == bulls and sec_cows == cows:
                    print(f"{n1}{n2}{n3}{n4}", end=" ")
                    no_result = False
                    sec_bulls = 0
                    sec_cows = 0
                else:
                    sec_bulls = 0
                    sec_cows = 0

if no_result:
    print("No")