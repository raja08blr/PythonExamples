def recu_fib(n):
    if n<=1:
        return n
    else:
        return (recu_fib(n-1)+recu_fib(n-2))
nitems=5
if nitems <=0:
    print("Enter positive integer")
else:
    for i in range(nitems):
        print(recu_fib(i))