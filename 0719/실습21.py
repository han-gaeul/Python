# 숫자 뒤집기
def recursive(n):
    if n <= 0:
        return
    print(n % 10, end='')
    recursive(n//10)

num = int(input())
recursive(num)

# recursive 함수에서 n이 0보다 같거나 작을 때 return
# 그렇지 않으면 n을 10으로 나눈다(%)
# 그 후에 재귀함수를 호출해서 n을 10으로 나눈다

# 예시
# 1234를 입력하면
# 4를 출력하고 123을 재귀함수로 호출함
# 그 후에 3을 출력하고 12를 return
# 0까지 같은 작업 반복 후에 모든 함수가 종료됨