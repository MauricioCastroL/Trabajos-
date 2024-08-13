#Autor: Mauricio Castro L.
#Date: 21-06-2024  22:48

num = float(input("Primer número: "))
num1= float(input("Segundo número: "))
num2= float(input("Tercer número: "))

def funcion_max(num, num1, num2):
    if num > num1 and num > num2:
        print("El mayor es: ", num)
    elif num < num1 and num1 > num2:
        print("El mayor es: ", num1)
    elif num < num2 and num1 < num2:
        print("El mayor es: ", num2)
    elif num == num2 and num1 == num2:
        print("Todos son iguales ", num2)
    elif num > num2 and num1 == num2:
        print("El mayor es: ", num)
    elif num1 > num2 and num == num2:
        print("El mayor es: ", num1)
    elif num2 > num and num == num1:
        print("El mayor es: ", num2)


if __name__ == "__main__":
    pasa = funcion_max(num, num1, num2)
