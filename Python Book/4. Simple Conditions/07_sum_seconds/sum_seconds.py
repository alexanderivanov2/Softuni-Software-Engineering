competitor1 = int(input())
competitor2 = int(input())
competitor3 = int(input())

sum_sec = competitor1 + competitor2 + competitor3

minutes = sum_sec // 60
sec = sum_sec % 60

if sec < 10:
    print(f"{minutes}:0{sec}")
else:
    print(f"{minutes}:{sec}")