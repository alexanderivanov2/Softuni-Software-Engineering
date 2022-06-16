from test import fibonachi

comand_1 = input()
comand_2 = input().split()[1]
while not comand_1 == "Stop":
    comand_1 = comand_1.split()[2]
    fibonachi.get_result(int(comand_1), int(comand_2))
    comand_1 = input()
    comand_2 = input().split()[1]
