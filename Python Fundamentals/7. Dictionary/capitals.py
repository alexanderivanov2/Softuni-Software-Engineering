country = input().split(", ")
capitals = input().split(", ")

dict_country_capitals = dict(zip(country, capitals))

[print(f"{key} -> {value}") for key, value in dict_country_capitals.items()]