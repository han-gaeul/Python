# 숫자의 길이 구하기
number = 123

# 123 -> 1 * 100 + 2 * 10 + 3 * 1
# while
# 123 / 10 -> 12, 3 -> 1, 2 -> 0, 1
# 종료조건은 몫이 0

result = 0
# 몫이 0이 되면 종료 해야 하니까!
# != 0은 없어도 실행 됨
# 왜? 0은 False이고 False가 되면 반복 종료됨
# int 0이 아닌 다른 수는 무조건 True
while number != 0:
    # number = number // 10
    number //= 10
    result += 1

print(result)

# while은 종료 조건 때까지
# for문은 어떠한 반복 가능한 것들이 있을 때
# 그것들을 한 번씩 순회 하겠다


# 문자열로 형변환
# print(len(str(number)))

# 3. log
# import math
# print(int(math.log(number, 10)) + 1)