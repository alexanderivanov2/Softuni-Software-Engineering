bitcoin = int(input())
yuans = float(input())
commission = float(input()) / 100
bitcoin_lv = bitcoin * 1168
yuans_dollars = yuans * (0.15 * 1.76)
sum_lv = bitcoin_lv + yuans_dollars
sum_eur = sum_lv / 1.95
sum_eur = round(sum_eur - (commission * sum_eur), 2)
print(sum_eur)
