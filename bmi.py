while True:
     height = input('신장을 입력하세요(cm): ')
     weight = input('체중을 입력하세요(kg): ')
     
     bmi = (float(weight) / float(height) ** 2) * 10000
     
     print('[bmi-저체중-18.5-정상-23-과체중-25-비만-30-고도비만]')
     
     if bmi <= 18.5:
          level = '저체중'
     elif 18.5 < bmi < 23:  
          level = '정상'
     elif 23 < bmi < 25:
          level = '과체중'
     elif 25 < bmi < 30:
          level = '비만'
     elif bmi > 30:
          level = '고도비만'
         
         
     print('나의 신체질량지수(bmi) {:.2f} {}'.format(bmi, level))     
     