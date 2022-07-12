# 1. num은 input으로 사용자에게 입력 받기
num = int(input()) # input으로 받는 기본 타입은 문자열!!
# print(num)
# 2. 조건문을 통해서 홀수/짝수 여부를 출력
# 숫자로서의 num!
if num % 2 == 1: #int(num)으로 작성 가능
    print('홀수')
else:
    print('짝수')