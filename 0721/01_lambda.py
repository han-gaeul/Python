# map(함수, 반복 가능한 것)
# 반복 가능한 것들의 모든 요소에 함수를 적용시킨 결과를
# map object로 반환

# map(int, input().split())
# int형 변환 함수를 
# input으로 받은 것을 쪼갠 결과인 리스트에 각각 적용한다.

numbers = [1, 2, 5, 10, 3, 9, 12]

# 기본 반복/조건 코드
result = []
for n in numbers:
    #if number % 3 == 0:
    result.append(n * 3)
print(result)

# map으로 쓰고 싶다면?
# (이 코드가 좋다는 것은 아님)
# 함수를 정의해야 함
def multiple_3(n):
    return n * 3

print(list(map(multiple_3, numbers)))

# 이 함수는 계속 사용되지 않고 map에서만 사용됨
# 임시적인 함수를 만들고 싶다 -> lmabda
print(list(map(lambda n: n * 3, numbers)))