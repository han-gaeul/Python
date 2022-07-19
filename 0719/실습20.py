# 각 자릿수의 합 구하기

# 1. 문자열로 형 변환하여 풀기
num = int(input())

# 값을 담을 변수 생성
result = 0

for n in str(num):
    # 다시 정수형으로 바꿔서 더하기
    result += int(n)

print(result)



# 2. 형 변환 없이 풀기
num = int(input())

#def solution(num):
result = 0

while num > 0:
    result += num % 10
    num //= 10

print(result)


# return은 해당 함수가 어떤 값을 가질지 지정해주는 용도
# print처럼 단독으로 사용할 수 없고 실제 출력도 되지 않음
