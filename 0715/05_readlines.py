with open('students.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    print(lines, type(lines))

# ['김김김\n', '이이이\n', '박박박\n', '최최최\n', '김장장\n', '정정정\n', '한한한\n', '심심심\n', '김차차\n', '주주주\n'] <class 'list'>