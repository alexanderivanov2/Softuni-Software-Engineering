world_record_in_seconds = float(input())
distance = float(input())
swim_time_for_meter = float(input())

slow_down = distance // 15
time = distance * swim_time_for_meter + slow_down * 12.5

if time < world_record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")

else:
    print(f"No, he failed! He was {time - world_record_in_seconds:.2f} seconds slower.")