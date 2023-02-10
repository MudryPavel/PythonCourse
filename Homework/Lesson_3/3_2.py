def ArrayClosestNum(array1,num):
    diff=abs(array1[1]-num)
    closeNum=array1[1]
    for x in array1:
        if abs(x-num)<diff:
            diff=abs(x-num)
            closeNum=x
    return closeNum
numbers = [0, -1, 5, 2, 3, 5]


print(ArrayClosestNum(numbers,3.9))