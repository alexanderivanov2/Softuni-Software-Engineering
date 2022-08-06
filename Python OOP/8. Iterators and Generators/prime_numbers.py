def get_primes(nums_list):

    for n in nums_list:
        if n == 0 or n == 1:
            continue
        prime = True
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            yield n



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))