def fib(num):
    a, b = 1,1
    for i in range(0,num):
        yield a
        a,b =b,a+b

for num in fib(5):
    print(num)