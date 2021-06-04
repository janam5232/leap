fib = 0
nextFib = 1

while(nextFib <= 100):
    print(nextFib)

    tmp = nextFib
    nextFib += fib
    fib = tmp
