add = lambda a,b: a + b
print(add(10,20))

multiply = lambda a,b: a * b
print(multiply(10,20))

#cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#filtrar solo los numeros pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)