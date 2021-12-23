start_year = int(input())
end_year = int(input())
date_weight = int(input())
have = True
high_year = False

for year in range(start_year, end_year + 1):
    year1 = year
    y4 = year1 % 10
    year1 = year1 // 10
    y3 = year1 % 10
    year1 = year1 // 10
    y2 = year1 % 10
    year1 = year1 // 10
    y1 = year1 % 10