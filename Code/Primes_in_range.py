def primes_in_range(start,end):
    primes = []
    for num in range(start,end+1):
        is_prime = True

        if num <= 1:
            is_prime = False
        else:
            for i in range(2,num):
                if num % i == 0:
                    is_prime = False
                    break

        if is_prime == True:
            primes.append(num)
    

    return primes

# print(primes_in_range(1,10))
# print(primes_in_range(11,20))