tabs_in_browser = int(input())
salary = int(input())

for i in range(tabs_in_browser):
    tab_name = input()
    if tab_name == "Facebook":
        salary -= 150
    elif tab_name == "Instagram":
        salary -= 100
    elif tab_name == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)

