# 직사각형의 넓이를 구하시오.
# 직사각형 세로는 n, 가로는 m
# input 예시 : 10 20

n, m = map(int, input().split())
# int는 함수
# input 타입 - 항상 string(문자열)
# 문자열.split() 내가 구분값을 기준으로 쪼개겠다. 반환 결과는 항상 list
# input().split() 문자열로 받을 것은 각각을 공백을 기준으로 리스트로 쪼갰다. -> 여기까지 리스트 ['10', '20']

# map은 어떤 함수를 반복 가능한 것들의 요소에 모두 적용시킨 결과
# int 함수를 input().split() 리스트의 모든 요소에 적용한 결과 -> map object(맵 어떤 것) -> 여기까지 결과 [10, 20]

# n, m = [10, 20]
print(n * m)

# 내장함수를 10을 다 더해주는 함수
def plus10(n):
    return n + 10

numbers = [10, 20, 30]
new_numbers = (list(map(plus10, numbers)))
print(new_numbers)