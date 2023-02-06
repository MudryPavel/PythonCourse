numbers = [2, 3, 4, 2, -1, 8, 9, 1, 2, 5, 7, 8]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
print(len(unique))