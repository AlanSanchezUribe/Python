square = [x**2 for x in range(1,11)]
print('Square:', square)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print('Fahrenheit:', fahrenheit)

#numeros pares
evens = [x for x in range(1,21) if x % 2 == 0]
print('Evens:', evens)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print('Transposed:', transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print('Transposed2:', transposed)

numbers = [1,2,3,4,5]
dobles = [x*2 for x in numbers]
print(dobles)

words = ['sol', 'mar', 'cerro', 'rio', 'estrella']

words_upper = [word.upper() for word in words if len(word) > 3]
print(words_upper) 

list1 = ['nombre', 'edad', 'ocupacion']
list2 = ['Juan', 25, 'Ingeniero']

combined_list = [(list1[i], list2[i]) for i in range(len(list1))]
print(combined_list)