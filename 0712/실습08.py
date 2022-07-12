


# numbers.remove(max(numbers))
# max(numbers)

# numbers = list(set(numbers))

# max_num = numbers[0]
# for i in numbers:
#     if i > max_num:
#         max_num = i

# numbers.remove(max_num)

# max_num = numbers[0]
# for i in numbers:
#     if i > max_num:
#         max_num = i

# print(max_num)

# numbers = [0, 20, 100, 50, -60, 50, 100]


# numbers = [3, 6, 10, 14, 54]
# numbers.sort(reverse=True)
# print(numbers[1])


numbers = [0, 20, 100, 50, -60, 50, 100]
new_list = []
for v in numbers:
    if v not in new_list:
        new_list.append(v)
new_list.sort(reverse=True)
print(new_list[1])