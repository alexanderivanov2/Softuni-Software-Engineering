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
    for m in range(1, 12 + 1):
        for d in range(1, 32):
            if year % 4 == 0:
                if year % 100 == 0 and year % 400 == 0:
                    high_year = True
                elif year % 100 != 0:
                    high_year = True
                else:
                    high_year = False
            else:
                high_year = False
            if high_year:
                if m == 2 and d == 30:
                    break
            else:
                if m == 2 and d == 29:
                    break
            if m == 4 or m == 6 or m == 9 or m == 11:
                if d == 31:
                    break
            if m < 10:
                m1 = 0
                m2 = m
            else:
                m2 = m % 10
                m1 = (m // 10) % 10
            if d < 10:
                d1 = 0
                d2 = d
            else:
                d2 = d % 10
                d1 = (d // 10) % 10