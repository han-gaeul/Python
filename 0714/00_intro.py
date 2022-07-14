# 리스트
a = [10, 1, 100]
#정렬
new_a = a.sort()
print(a, new_a)
# [1, 10, 100] None
# 리스트 메서드를 활용하면 그 메서드를 정렬된 상태로 변경(원본 변경)
# return 되는 것은 None

# 리스트
b = [10, 1, 100]
# 정렬
new_b = sorted(b)
print(b, new_b)
# [10, 1, 100] [1, 10, 100]
# sorted 함수를 활용하면 원본 변경 X
# return 되는 것은 정렬된 리스트

# 실제 활용 코드
a = [10, 1, 100]
a.sort()
# a를 정렬된 상태로 활용

b = [10, 1, 100]
b = sorted(b)
# b를 정렬된 상태로 활용