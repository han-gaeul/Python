def my_case_word(text):

    re_text = ''
    length = len(text)
    
    for x in range(length):
        letter = text[x]
        # 대문자 --> 소문자로
        if 64 < ord(letter) < 96:
            num = ord(letter) + 32
            str = chr(num)
            re_text = re_text + str

        # 소문자 --> 대문자로
        elif ord(letter) > 96:
            num = ord(letter) - 32
            str = chr(num)
            re_text = re_text + str
            
        # 공백은 ' '공백으로
        elif ord(letter) == 32:
            str = ' '
            re_text = re_text + str
        
            
    return re_text

input_txt = input()
#print("대소문자를 바꿉니다!")
cnt = input(my_case_word(input_txt))