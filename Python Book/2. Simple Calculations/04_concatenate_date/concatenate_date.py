#Напишете програма, която прочита от конзолата име, фамилия, възраст и град и печата съобщение от следния вид:
# You are <firstName> <lastName>, a <age>-years old person from <town>.
firstName = input().title()
lastName = input().title()
age = int(input())
town = input().title()
print(f"You are {firstName} {lastName}, a {age}-years old person from {town}.")
