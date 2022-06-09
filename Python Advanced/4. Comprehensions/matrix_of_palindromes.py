def print_matrix_palindrome(rows, columns):
    for col in range(columns):
        print(f"{chr(97 + rows)}{chr(97 + rows + col)}{chr(97 + rows)}", end=" ")
    return print()


r, c = [int(x) for x in input().split()]
[print_matrix_palindrome(row, c) for row in range(r)]
