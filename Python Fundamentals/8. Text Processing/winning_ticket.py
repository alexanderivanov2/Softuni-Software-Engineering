import re

tickets = input().split(',')


def print_result(p1, p2, ticket):
    if len(p1[0]) > 5 and len(p2[0]) > 5:
        lower = len(p1[0]) if len(p1[0]) <= len(p2[0]) else len(p2[0])
        if lower == 10:
            print(f'ticket "{ticket}" - {10}{p1[0][0]} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {lower}{p1[0][0]}')
    else:
        print(f'ticket "{ticket}" - no match')


def get_final_p(final_p1, final_p2, p1, p2):
    if final_p1 is None:
        return p1, p2
    lower = len(p1[0]) if len(p1[0]) <= len(p2[0]) else len(p2[0])
    lower2 = len(final_p1[0]) if len(final_p1[0]) <= len(final_p2[0]) else len(final_p2[0])
    if lower2 >= lower:
        return final_p1, final_p2
    return p1, p2


for ticket in tickets:
    ticket = ticket.strip()
    if not len(ticket) == 20:
        print("invalid ticket")
        continue
    elif "@" not in ticket and '#' not in ticket and "$" not in ticket and '^' not in ticket:
        print(f'ticket "{ticket}" - no match')
        continue
    part_one = ticket[0:10]
    part_two = ticket[10:]
    final_p1, final_p2 = ['1'], ['1']
    if '@' in part_one and "@" in part_two:
        p1 = re.findall(r"[@]+", part_one)
        p2 = re.findall(r"[@]+", part_two)
        final_p1, final_p2 = get_final_p(final_p1, final_p2, p1, p2)
    if '#' in part_one and "#" in part_two:
        p1 = re.findall(r"[#]+", part_one)
        p2 = re.findall(r"[#]+", part_two)
        final_p1, final_p2 = get_final_p(final_p1, final_p2, p1, p2)
    if '$' in part_one and "$" in part_two:
        p1 = re.findall(r"[$]+", part_one)
        p2 = re.findall(r"[$]+", part_two)
        final_p1, final_p2 = get_final_p(final_p1, final_p2, p1, p2)
    if '^' in part_one and "^" in part_two:
        p1 = re.findall(r"[\^]+", part_one)
        p2 = re.findall(r"[\^]+", part_two)
        final_p1, final_p2 = get_final_p(final_p1, final_p2, p1, p2)
    print_result(final_p1, final_p2, ticket)
