number_of_pages = int(input())
read_pages_per_hour = int(input())
days_for_read = int(input())


def calculate_need_hours(num_pages, pages_per_hour, days_read):
    hours_a_day_read = num_pages / days_read / pages_per_hour
    print(hours_a_day_read)


calculate_need_hours(number_of_pages, read_pages_per_hour, days_for_read)
