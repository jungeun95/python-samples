height = input('신장을 입력하세요(cm): ')
weight = input('체중을 입력하세요(kg): ')

bmi = (float(weight) / float(height) ** 2) * 10000
print('나의 신체질량지수(bmi) {:.2f}'.format(bmi))

if bmi > 23:
    print('당신은 과체중입니다')
    

