# 리스트는 mutable
# 리스트는 바꿀 수 있다
a = [1, 2, 3]
a[0] = 100
print(a) # 변경

# 문자열은 immutable
# 문자열의 첫번째 인덱스에 해당하는 값을 바꿀 수 있다? 없다
a = 'hi'
a[0] = 'c'
print(a)
# Traceback (most recent call last):
#   File "/Users/goobano/Desktop/Python/0714/04_mutable.py", line 10, in <module>
#     a[0] = 'c'
# TypeError: 'str' object does not support item assignment