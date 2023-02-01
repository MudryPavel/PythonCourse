def Factorial(n):
    i=1
    Res=1
    while i<=n:
        Res*=i
        i+=1
    return Res
x = int(input("Enter N: "))
print(Factorial(x))