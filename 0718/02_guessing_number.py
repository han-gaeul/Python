# 숫자 입력을 받아서 출력
numbers = input('숫자를 입력해주세요 : ')
print(numbers)

# int 형변환
# if int(numbers) == 5:
#     print('오오~')
# else:
#     print('오가 아닙니다.')

try: # 얘를 먼저 실행해보고
    if int(numbers) == 5:
     print('오오~')
    else:
        print('오가 아닙니다.')
except: # 예외가 있다면 얘를 실행
    print('숫자를 입력하지 않았습니다.')