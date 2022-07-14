# 'apple' a 카운트
# 득표수 구하는 것과 동일
word = 'apple'

# for '__' in word:
# '__' <- 이름을 붙여주는 곳
# word의 요소를 하나씩 '__' 에 바인딩

count = 0
for char in word:
    if char == 'a':
        # a일 때마다 + 1
        # 결과값을 담을 곳이 필요함
        # 그래서 만드는 변수 result, count
        count += 1
print(count)

