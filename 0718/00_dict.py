word = 'banana'

result = {}

# 문자열을 반복하면서 알파벳 하나씩이 char
for char in word:
    # 만약에 기존에 키가 없으면 1로 초기화
    if char not in result:
        result[char] = 1
    # 키가 있으면 기존 값에 더하자
    else:
        result[char] = result[char] + 1

print(result)

cnt = 0
for i in word:
    cnt += 1

result = {}
# 키-값의 쌍 추가
result['a'] = 0
print(result)

# 값의 추가
list = []
list.append(1)
# list[0] = 3
print(list)