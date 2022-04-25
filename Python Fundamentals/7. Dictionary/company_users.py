companies = {}

command = input()

while not command == "End":
    company, id_employee = command.split(" -> ")
    if company not in companies:
        companies[company] = [id_employee]
    elif id_employee not in companies[company]:
        companies[company].append(id_employee)
    command = input()


sorted_companies = dict(sorted(companies.items(), key=lambda x: x[0]))

for key, value in sorted_companies.items():
    print(key)
    [print(f"-- {x}") for x in value]