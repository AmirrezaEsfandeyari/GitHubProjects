print('**Multiplication table**\nWhat size multiplication table do you want?(axb)')
a = int(input("please enter a:"))
b = int(input("please enter b:"))

list1 = []
for x in range(1, a+1):
    for num in range(1, b+1):
        list1.append(num * x)
    print(list1)
    list1.clear()


