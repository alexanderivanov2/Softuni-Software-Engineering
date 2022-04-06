def palindrome_check(num_list):
    results = [True if num == num[::-1] else False for num in num_list]
    return "\n".join(str(el) for el in results)


num_list = input().split(", ")
print(palindrome_check(num_list))