# 정수 number가 주어질 때
# 각 자릿수의 합을 구해서 출력

number = 123

# number가 0일 때 멈춤
# -> int는 0일 때 False
result = 0
while number:
    # 몫은 다음 number가 됨
    # 나머지는 더해나가면 됨
    result += number % 10
    number //= 10

print(result)

# 2.
# divmod(x, y)는 x를 y로 나누고
# 결과를 tuple로 반환
# (몫, 나머지)
number, remainder = divmod(number, 10)
result += remainder