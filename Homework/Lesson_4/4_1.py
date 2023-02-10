def SameNumsIn2Arrays(array1,array2):
    array3=list()
    for number in array1:
        if number in array2 and number not in array3:
            array3.append(number)
    sorted(array3)
    return array3
print(SameNumsIn2Arrays([1,2,3,4,5],[4,5,7,8]))      