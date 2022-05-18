MAXIMUM_HP = 100
MAXIMUM_MP = 200

heroes = {}
n = int(input())

for i in range(n):
    hero_name, hp, mp = input().split()
    heroes[hero_name] = {"hp": int(hp), "mp": int(mp)}

command = input()

while not command == "End":
    action, hero_name, *data = command.split(" - ")
    if action == "CastSpell":
        mp_need = int(data[0])
        spell_name = data[1]
        if mp_need <= heroes[hero_name]["mp"]:
            heroes[hero_name]["mp"] -= mp_need
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage = int(data[0])
        attacker = data[1]
        heroes[hero_name]['hp'] -= damage
        if heroes[hero_name]['hp'] < 1:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
    elif action == "Recharge":
        amount = int(data[0])
        if heroes[hero_name]["mp"] + amount > MAXIMUM_MP:
            print(f"{hero_name} recharged for {MAXIMUM_MP - heroes[hero_name]['mp'] } MP!")
            heroes[hero_name]["mp"] = MAXIMUM_MP
        else:
            heroes[hero_name]["mp"] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif action == "Heal":
        recharge = int(data[0])
        if heroes[hero_name]["hp"] + recharge > MAXIMUM_HP:
            print(f"{hero_name} healed for {MAXIMUM_HP - heroes[hero_name]['hp'] } HP!")
            heroes[hero_name]["hp"] = MAXIMUM_HP
        else:
            heroes[hero_name]["hp"] += recharge
            print(f"{hero_name} healed for {recharge} HP!")
    command = input()


sorted_heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1]['hp'], x[0])))

for key, value in sorted_heroes.items():
    print(f"{key}\nHP: {value['hp']}\nMP: {value['mp']}")