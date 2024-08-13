#Autor: Mauricio Castro L.

def datos():
    eato = input("Ingrese la cadena de caracteres: ")
    return eato

def opera(datos):
    for i in range(len(datos) -1, -1,-1 ):
        print(datos[i])
    



if __name__ == "__main__":
    dato = datos()
    ent = opera(dato)

