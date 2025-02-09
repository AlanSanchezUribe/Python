#ejemplo de iterador

#crear una lista

my_list = [4, 7, 0, 3]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))#next permite ver los valores que se van almacenando en memoria
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
