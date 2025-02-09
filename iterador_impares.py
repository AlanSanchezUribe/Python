#Crear un iterador para numeros impares
#limite
limit = 10

#crear iterador
odd_itter = iter(range(1, limit+1, 2))

for num in odd_itter:
    print(num)
