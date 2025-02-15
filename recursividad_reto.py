def recursividad_reto(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + recursividad_reto(n-1)
    
number = int(input("Enter a number: "))
print(recursividad_reto(number))