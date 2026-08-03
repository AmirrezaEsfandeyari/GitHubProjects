print('a program to solve quadratic equation.\nenter coefficients of the equation as follows:\nax²+bx+c')
a=int(input('please enter coefficient "a":'))
b=int(input('please enter coefficient "b":'))
c=int(input('please enter coefficient "c":'))

Delta=((b ** 2)-(4 * (a * c)))
if Delta > 1:
    x1=(-b + Delta ** 0.5)/(2 * a)
    x2 = (-b - Delta ** 0.5)/(2 * a)
    print(f'the equation has two solutions.x = {x1} and x = {x2}')
elif Delta == 0:
    x= -b / (2 * a)
    print(f'the equation has one solutions.x = {x}')
else:
    print('the equation has no answer..')
