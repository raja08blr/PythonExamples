def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            # print(num, "is Not a prime")
            break
    else:
        print(num, "is prime number")


# check_prime(9)
# check_prime(7)


def check_prime_range(starting, ending):
    for num in range(starting, ending):
        for i in range(2, num):
            if (num % i) == 0:
                # print(num, "is Not prime number")
                break
        else:
            print(num, "is prime number")


check_prime_range(10, 20)
