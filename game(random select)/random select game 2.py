from random import randint

#A game in which the user guesses a number, and the system verifies it against its own selected number.
userNumber = int(input('Pleas enter number in range 1,100 :'))
a,b = 1,100
randNumber = randint(a, b)
count=0
while randNumber != userNumber:
    print(randNumber)
    userSelect = input("Please tel me your number is langer or smaller as my number.l(longer) and s(smaller) :")

    if userSelect == "l":
        a = randNumber +1
        randNumber = randint(a, b)
    elif userSelect == "s":
        b = randNumber-1
        randNumber = randint(a, b)

    count += 1
print(randNumber)
print(f'my(system) WIN.\ncount of my choices : {count}')