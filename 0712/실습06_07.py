numbers = [0, 20, 100]

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if max_num < num:
        max_num = num
    if min_num > num:
        min_num = num

print(max_num)
print(min_num)