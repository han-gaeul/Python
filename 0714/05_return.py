# a라는 이름에 타입이 int, 1을 할당
a = 1
# 

print(1 + 2)
print(3 * 3)
print(4 * 5)
# print는 출력하기 위한 것!!

# 한 단계 up
a = [1, 2, 3]
cnt = len(a)
# sum(a)의 결과(int, 합 계산 결과)를 result에 할당
result = sum(a)

numbers = [1, 2, 3]
# None이 반환. numbers는 바뀌어있음
#result = numbers.reverse()
# 일반적으로 코드는 아래처럼 작성
numbers.reverse()


print('1 2 3'.split().index('2') + 10)
# '1 2 3'.split() 이 ['1', '2', '3']

# ['1', '2', '3'].index('2') 여기까지 1
# + 10 하면 11