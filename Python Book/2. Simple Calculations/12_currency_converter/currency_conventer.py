#Напишете програма за конвертиране на парична сума от една валута в друга.
# Трябва да се поддържат следните валути: BGN, USD, EUR, GBP. Използвайте следните фиксирани валутни курсове:
sum = float(input())
type_currency_in = input().upper()
type_currency_out = input().upper()

BGN_ = 1
USD_ = 1.79549
EUR_ = 1.95583
GBP_ = 2.53405

if type_currency_in == "BGN":
    sum = sum * BGN_
elif type_currency_in == "USD":
    sum = sum * USD_
elif type_currency_in == "EUR":
    sum = sum * EUR_
elif type_currency_in == "GBP":
    sum = sum * GBP_

if type_currency_out == "USD":
    result = sum / USD_
elif type_currency_out == "EUR":
    result = sum / EUR_
elif type_currency_out == "GBP":
    result = sum / GBP_
elif type_currency_out == "BGN":
    result = sum / BGN_

print(f"{round(result, 2)}")