def CrArray():
    n=input("Введите количество элементов массива")
    list1=list[n]
    for i in list1:
        list[i]=input(f"Введите {i} элемент массива")
    return list1
def MaxTripleInArray(list):
    maxTriple=0
    list.append(list[0])
    list.append(list[1])
    for i in range (0, len(list)-2):
        print((list[i],list[i+1],list[i+2]))
        if maxTriple<(list[i]+list[i+1]+list[i+2]):
            maxTriple=(list[i]+list[i+1]+list[i+2])
    return maxTriple
print(MaxTripleInArray([26,5,3,4,5,20]))