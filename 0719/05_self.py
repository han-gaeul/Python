class Person:
    # 생성자! 인스턴스가 생성 될 때 어떠한 작업!
    def __init__(self, name):
        # 그 인스턴스의 이름을 name으로 해주세요
        self.name = name
        # print('야옹')

# Person 클래스의 인스턴스인 rv를 생성
rv = Person('웬디')

print(rv.name)