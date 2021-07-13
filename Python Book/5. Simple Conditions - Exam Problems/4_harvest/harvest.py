import math

vineyard_area = int(input())
production_area = vineyard_area * (40 / 100)
kg_grape = float(input()) * production_area
vine_for_sale = int(input())
workers = int(input())
vine = kg_grape / 2.5

if vine >= vine_for_sale:
    vine_left = vine - vine_for_sale
    vine_for_workers = vine_left / workers
    print(f"Good harvest this year! Total wine: {math.floor(vine)} liters.\n{math.ceil(vine_left)}"
          f" liters left -> {math.ceil(vine_for_workers)} liters per person.")
else:
    vine_need = vine_for_sale - vine
    print(f"It will be a tough winter! More {math.floor(vine_need)} liters wine needed.")
