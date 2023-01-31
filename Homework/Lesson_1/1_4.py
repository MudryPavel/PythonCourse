# Требуется определить, можно ли от шоколадки размером n ×m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

def ChocoSplit(n,m,k):
    return (k<(m*n) and ((k%m==0) or (k%n==0)))
print(ChocoSplit(10,11,44))
print(ChocoSplit(3,7,14))
print(ChocoSplit(10,11,48))