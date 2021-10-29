print(' *** BMI ***')
inp = input('Enter your weight(kg) and height(m) : ')
w,h=map(float,inp.split(' '))
BMI = w/h**2
print('Your status is :',end=' ')
if BMI < 18.5:
    print('Below normal weight',end='.')
elif 18.5<= BMI < 25:
    print('Normal weight',end='.')
elif 25<= BMI < 30:
    print('Overweight',end='.')
elif 30<= BMI < 35:
    print('Case I Obesity',end='.')
elif 35<= BMI < 40:
    print('Case II Obesity',end='.')
else:
    print('Case III Obesity',end='.')