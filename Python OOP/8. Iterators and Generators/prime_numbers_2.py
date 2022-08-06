def get_primes(nums):
    for num in nums:
        if num > 1:
            flag = True
            for i in range(2, num // 2 + 1):
                if (num % i) == 0:
                    flag = False
                    break
            if flag:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))