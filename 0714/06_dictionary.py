# 기본 순회
# key가 기준, 직접 딕셔너리에 key로 접근하면 value를 얻을 수 있다
my_dict = {'apple' : '사과', 'banana' : '바나나'}

for word in my_dict:
    print(word)
    print(my_dict[word])
    print(word, my_dict[word])


# 심화형. 다양한 방법 -> 일종의 리스트
print(my_dict.keys(), type(my_dict.keys()))
# dict_keys(['apple', 'banana']) <class 'dict_keys'>
print(my_dict.values())
# dict_values(['사과', '바나나'])
for values in my_dict.values():
    print(values)


print(my_dict.items())

for k, v in my_dict.items():
    print(k, v)
# 일종의 리스트 안에 tuple
# dict_items([('apple', '사과'), ('banana', '바나나')])

# k, v 이름 붙이기
# my_dict.items() 이거는 [('apple', '사과'), ('banana', '바나나')]
# 


my_dict_3 = {'a' : 0}

# my_dict_3['a'] += 1
my_dict_3 = my_dict_3['a'] + 1
print(my_dict_3)

my_list = [10, 11, 12]
my_list[0] = my_list[0] + 1
print(my_list)

# 딕셔너리는 키로 접근, 리스트는 인덱스로 접근
# 딕셔너리는 인덱스라는 개념이 없음. 키-밸류만 존재

# for 키 in 딕셔너리:
#     print(딕셔너리[키)

# 리스트는 + 로 결합 가능. 딕셔너리는 불가능