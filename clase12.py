numbers = [1,2,3,4,5,6]
for i in numbers:
    print('i es igual a: ', i + 1)

for i in range(10):
    print(i)

for i in range(3,10):
    print(i)

fruits = ['apple', 'banana', 'cherry', 'orange', 'melon']

for fruit in fruits:
    print(fruit)
    if fruit == 'orange':
        print('I found the orange')

x = 0
while x<5:
    if x == 3:
        break
    print(x)
    x += 1 

numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 3:
        continue
    print('i es igual a: ', i)