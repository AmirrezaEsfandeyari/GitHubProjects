from random import randint

#game to guess the number selected by the system
randNumber = randint(1,100)
userNumber = int(input('Pleas enter number in range 1,100 :'))
count = 0
while userNumber != randNumber:
    if randNumber > userNumber:
        print('my choice of number for you is a large.')
        userNumber = int(input('Pleas enter number in range 1,100 :'))
    else:
        print('my choice of number for you is a Small.')
        userNumber = int(input('Pleas enter number in range 1,100 :'))
    count += 1
print(f'YOU WIN.\nyour count of choices = {count}')

