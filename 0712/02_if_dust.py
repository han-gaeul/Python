dust = int(input())
if dust <= 30:
    print('미세먼지 농도 : 좋음')
elif dust <=  80:
    print('미세먼지 농도 : 보통')
elif dust <=  150:
    print('미세먼지 농도 : 나쁨')
else:
    print('미세먼지 농도 : 매우나쁨')


dust = 100

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
# else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능
# else에는 조건문 '절대로' 작성하지 않음!!
# 조건문에서 else는 생략 가능
else:
    print('좋음')
print('미세먼지 확인 완료')