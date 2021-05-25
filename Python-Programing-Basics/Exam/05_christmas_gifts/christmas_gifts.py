adulst = 0
kids = 0

family_member = input()

while not family_member == "Christmas":
    if int(family_member) > 16:
        adulst += 1
    else:
        kids += 1
    family_member = input()

toys = kids * 5
blouse = adulst * 15

print(f"Number of adults: {adulst}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys}")
print(f"Money for sweaters: {blouse}")