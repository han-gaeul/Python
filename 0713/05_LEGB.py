sum = 5
sum([1, 2, 3])

# Traceback (most recent call last):
#   File "/Users/goobano/Desktop/Python/0713/05_LEGB.py", line 2, in <module>
#     sum([1, 2, 3])
# TypeError: 'int' object is not callable


# sum이 지금은 5가 되어버림

# Built-in scope에 sum 함수가 있었음
# global scope에 sum 이름의 변수를 만들었음
# 제가 찾으니까 L -> E -> G -> B


# def func1():
#     def func2():
#         return ''
#     return''
# 이 코드는 나중에