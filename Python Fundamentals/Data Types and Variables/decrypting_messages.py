key = int(input())
n = int(input())
string = ""

for i in range(n):
    char = input()
    string += chr(ord(char) + key)

print(string)