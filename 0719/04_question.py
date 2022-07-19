# 얕은 복사
a = [1, 2, 3]
b = a
b[0] = 'hi'

# list 형변환 결과 : 사실은 list고 사실은 값도 같지만 다른 메모리 주소 결과를 받아냄
c = [4, 5, 6]
d = list(c)
d[0] = 'hi'

# 슬라이싱
e = [7, 8, 9]
f = e[::]
f[0] = 'hi'

print(a)
print(b)

# 깊은 복사
a = [[1, 2], 2, 3]
b = list(a)
b[0][0] = 'hi'

print(a)
print(b)


import copy
a = [[1, 2], 2, 3]
b = copy.deepcopy(a)
b[0][0] = 'hi'


# 얕은 복사
# 리스트 주소가 123
# a = '12345'