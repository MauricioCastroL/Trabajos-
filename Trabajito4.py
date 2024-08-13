#Autor: Muaricio Castro L
#Date: 21-06-2024 23:08

#Pedir la letra
letra = input("Deme una letra cualquiera: ")
letra = letra.lower()

#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def funcion(letra):
    if letra == "a" or letra == "e" or letra == "i"or letra == "o" or letra == "u":
        print("True")
    else: print("False")


if __name__ == "__main__":
    fun = funcion(letra)