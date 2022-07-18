# 코드로 파일 만들기
with open('test.txt', 'w', encoding = 'utf-8') as f:
    f.write('Hello World')
    # f.write('1번 줄')
    # f.write('2번 줄')
    # f.write('3번 줄')
    for i in range(1, 6):
        f.write(f'{i} 번째')


# test.txt 파일 이름과 확장자
# w write 의미. 쓰기용으로 열기. 덮어씀
# r read 읽기 전용
# a append 쓰는데 파일이 있으면 이어서 씀