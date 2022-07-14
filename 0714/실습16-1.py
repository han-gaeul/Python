# in

word = 'apple'

is_a = False
for char in word:
    if char == 'a':
        is_a = True
print(is_a)

# 위의 4줄의 코드를 한 줄로 표현 가능
print('a' in word)