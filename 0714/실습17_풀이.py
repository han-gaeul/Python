word = 'banana'

result = ' '
for char in word:
    # 1. 알파벳을 숫자로 바꾸고
    number = ord(chr)

    # 2. 숫자를 -32를 하고
    number = number -32

    # 3. 다시 숫자를 알파벳으로 바꾼다.
    #print(chr(number))
    result += chr(number)
print(result)



for char in word:
    print(chr(ord(char)- 32), end=' ')