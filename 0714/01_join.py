names = ','.join(['홍길동', '김철수'])
print(names)
# 홍길동,김철수

# numbers = ' '.join([10, 20, 100])
numbers = ' '.join(map(str, [10, 20, 100]))
# str 형변환 해주는 함수의 이륾!

print(numbers)
# Traceback (most recent call last):
#   File "/Users/goobano/Desktop/Python/0714/01_join.py", line 5, in <module>
#     numbers = ' '.join([10, 20, 100])
# TypeError: sequence item 0: expected str instance, int found