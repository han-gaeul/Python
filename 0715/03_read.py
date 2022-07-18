# 파일명, 어떤 모드로 열지, 인코딩 설정
with open('students.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    print(text, type(text))
# 김김김
# 이이이
# 박박박
# 최최최
# 장장장
# 정정정
# 한한한
# 심심심
# 차차차
# 주주주
#  <class 'str'>

with open('students.txt', 'r', encoding = 'utf-8') as f:
    # 텍스트는 string 타입
    text = f.read()
    print(text, type(text))
    # string.split() -> 리스트 타입
    names = text.split()


with open('students.txt', 'r', encoding = 'utf-8') as f:
    # 텍스트는 string 타입
    text = f.read()
    print(text, type(text))
    # string.split() -> 리스트 타입
    names = text.split()
    count = 0
    for name in names:
        # name : 첫번째 시행 - 김김김
        # 언제? 김씨?
        if name.startswith('김'):
        # if name[0] == '김':
            count += 1
    print(count)

# if name[0] == '김': 이 코드보다
# 성이 김씨인 사람을 찾고 싶구나가 조금 더 명확하게 보임