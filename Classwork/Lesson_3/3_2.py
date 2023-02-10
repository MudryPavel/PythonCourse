numbers = [1, 2, 3, 4, 5]
k = 3
#new_numbers = []
# for i in range(k, len(numbers)):
#     new_numbers.append(numbers[i])
# for j in range(0, k):
#     new_numbers.append(numbers[j])
# print(new_numbers)
print(numbers[-k+1:] + numbers[:k])

numbers = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        count += 1
print(count)
