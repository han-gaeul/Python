# a, e, i, o, u 의 개수
word = 'apple'

# 지금은 인덱스가 필요 없어서 그냥 char를 받음
# 1.
count = 0
for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print(count)

count = 0
for char in word:
    if char == 'a':
        count += 1
    elif char == 'e':
        count += 1
    elif char == 'i':
        count += 1
    elif char == 'o':
        count += 1
    elif char == 'u':
        count += 1
print(count)

# 2.
count = 0
for char in word:
    # ['a', 'e', 'i', 'o', 'u']
    if char in 'aeiou':
        count += 1
print(count)