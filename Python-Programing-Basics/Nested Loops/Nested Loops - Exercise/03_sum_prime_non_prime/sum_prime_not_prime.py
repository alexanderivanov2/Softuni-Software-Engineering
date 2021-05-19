num = input()
prime = 0
non_prime = 0
is_prime = True

while num != "stop":
    num = int(num)
    if num < 0:
        print(f"Number is negative.")
        num = input()
        continue
    for i in range(2, (num+1)//2):
        if num % i == 0:
            non_prime += num
            is_prime = False
            break
    if is_prime:
        prime += num
    is_prime = True
    num = input()

print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
