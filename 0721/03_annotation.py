# 동적 타입 언어인 파이썬에서
# 정적 타입으로 바꿔주는 것이 아니라
# 그냥 힌트... 노트... 메모.. 주석...

# 형 힌트에 대한 표준

# 변수 어노테이션
a : int = 3
print(a)

# 함수 어노테이션
def add(x : int, y : int) -> int:
    return x + y
print(add(7, 4))
print(add('hi ', 'hello'))

def add(x, y):
    return x + y
print(add(7, 4))