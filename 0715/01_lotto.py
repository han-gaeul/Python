import random

# numbers = random.sample([1, 2, 3], 2)
# print(numbers, type(numbers))

# [1, 2] <class 'list'>



# 1~45까지의 숫자
# 그 중에 6개

# numbers = random.sample(range(1, 46), 6)
# print(numbers, type(numbers))

#[41, 16, 28, 27, 8, 18] <class 'list'>



# 정렬

numbers = random.sample(range(1, 46), 6)
numbers.sort()
print(numbers, type(numbers))

# [1, 5, 9, 20, 34, 39] <class 'list'>




# n = int(input('몇 번? '))
# for i in range(n):
#     numbers = random.sample(range(1, 46), 6)
#     numbers.sort()
#     print(numbers, type(numbers))

# 몇 번? 5
# [4, 13, 14, 21, 24, 26] <class 'list'>
# [4, 9, 18, 22, 29, 35] <class 'list'>
# [7, 11, 12, 34, 38, 43] <class 'list'>
# [6, 16, 20, 21, 36, 37] <class 'list'>
# [4, 5, 19, 30, 32, 41] <class 'list'>