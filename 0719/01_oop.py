word_list = ['abc', 'banana', 'apple']

def transform_uppercase(word):
    result = ' '
    for char in word:
        number = ord(char)
        number = number - 32
        result += char(number)
    return result

for word in word_list:
    print(transform_uppercase(word))


my_list = [1, 2, 3]
my_list.sort()
# 리스트의 데이터를 직접 정렬

sorted(my_list)
# 리스트는 sorted 함수의 인자로 전달 될 뿐