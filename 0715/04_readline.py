# 줄 단위로 한 줄씩 호출
with open('students.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        print(line, end = ' ')
    # lines = f.readline()
    # print(lines, type(lines))
    # lines = f.readline()
    # print(lines, type(lines))
    # lines = f.readline()
    # print(lines, type(lines))
    # lines = f.readline()
    # print(lines, type(lines))
    # lines = f.readline()
    # print(lines, type(lines))
    # lines = f.readline()
    # print(lines, type(lines))

# 김김김
#  이이이
#  박박박
#  최최최
#  김장장
#  정정정
#  한한한
#  심심심
#  김차차
#  주주주


#김김김
#  <class 'str'>
# 이이이
#  <class 'str'>
# 박박박
#  <class 'str'>
# 최최최
#  <class 'str'>
# 김장장
#  <class 'str'>
# 정정정
#  <class 'str'>