working_days_month = int(input())
daily_salary = float(input())
USD = float(input())
month_salary = working_days_month * daily_salary
year_salary = (month_salary * 12) + (month_salary * 2.5)
year_salary_taxes = year_salary - (year_salary * (25/100))
year_salary_leva = (year_salary_taxes * USD) / 365
print(round(year_salary_leva, 2))
