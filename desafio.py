def eleccion():
    print("Elija una operación aritmetica")
    print("Suma / Multiplicación/ División/ Resta")
    eleccion = input("Cuál es su elección: ")
    return eleccion

def operacion(eleccion):
    lista_numeros = []
    if eleccion == "Suma" or eleccion == "suma":
        numeros_por_sumar = int(input("Cuantos numeros sumara: "))
        print("Ingrese los números en el siguiente formato")
        print("EJ:")
        print("1,2,3,4,5...")
        numeros = input()
        


        



if __name__ ==  "__main__":
    elec = eleccion()
    resultado = operacion(elec)