#Brute Force Python Implementation to check if a number is prime - O(N)
def isPrime(num):
    if (num<=1):
        return False
    factors = 0
    for i in range(1, num+1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False
print(isPrime(10))
print(isPrime(7))
print(isPrime(9))

for x in range(10,20):
    print(x,"is",isPrime(x))
