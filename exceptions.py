try:
    divisor = int(input("Enter a number: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:
    print("You can't divide by zero")
    print(e)
except ValueError:
    print("You must enter a number")


def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)