# 처음 시작값
n = 0
# 0부터 더하기 위해
result = 0
# user_input 값
user_input = int(input())

while n <= user_input:
        result += n
        n += 1
print(result)

#while n < user_input:
#        n += 1
#        result += n
#print(result)

# print(f'n: {n}, result{result}) 현재 값 확인