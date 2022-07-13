word = 'apple'

result = ''

# 1. for
for char in word:
    result = char + result
print(result)

# 2. pythonic
# print(word[::-1])
# print(' '.join(reversed(word)))

# 3. index
# 익숙해질수록 나중에 알고리즘 코드 풀기 좋음
word = 'apple'

for i in range(len(word)):
    print(word[len(word) - i - 1], end='')