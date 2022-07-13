def minus_and_product(x, y):
    return x - y # 실행 후 종료
    return x * y # 실행되지 않음. 도달할 수 없음.

# 값을 두개 이상 반환하는 방법
def minus_and_product(x, y):
    return x - y, x * y


def foo():
    return 1, 2

result = foo()
print(result, type(result)) #<class 'tuple'>

def no():
    a = 1

result = no()
print(result, type(result)) # None <class 'NoneType'>

# pritn 함수는 출력을 해주고
# return 값은 없다(None)
a = print('hi')
print(a, type(a)) #None <class 'NoneType'>