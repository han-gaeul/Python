# 리스트 컴프리핸션

even_list = [ i for i in range(10) if i % 2 == 0]
print(even_list)
# [0, 2, 4, 6, 8]

even_list = [ i ** 2 for i in range(10) if i % 2 == 0]
print(even_list)
# [0, 4, 16, 36, 64]

print(sum([ i ** 2 for i in range(10) if i % 2 == 0]))
# 120

# 딕셔너리 컴프리핸션
# dic_list = [num : num ** 3 for i in range(10)]