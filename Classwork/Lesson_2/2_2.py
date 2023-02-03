def FibonacciCheck(n):
    a=0
    current=1
    i=1
    while a<n:
        t=current
        current+=a
        a=t
        i+=1
        if a>n:
            i = -1
    return i
x = int(input("Enter N: "))
print(FibonacciCheck(x))
    