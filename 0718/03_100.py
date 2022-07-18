# 100을 사용자가 입력한 숫자로 나눠서 결과를 출력
from logging import exception


number = input()

# print(100/int(number))
#  10을 입력하면 10.0 출력

try:
    print(100/int(number))
except ZeroDivisionError as err:
    print(err) # 실제 파이썬에서 출력되는 에러
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('숫자 형식을 입력 해주세요.')
except exception: # 가장 상위의 오류. 맨 위에 작성하게 되면 아래 코드는 실행되지 않음
    print('오류')

# 예외 처리 할 에러들을 한 번에 묶어서 작성 가능
# except ZeroDivisionError, ValueError:
#     print('0으로 나눌 수 없습니다.')


# 조건문과 다른 점은 에러가 발생했을 때 다른 것을 하도록 함
# 예외 대신에 어떠한 행동을 함