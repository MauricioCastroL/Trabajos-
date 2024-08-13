#Autor: Mauricio Castro L:

def datos():
    print("Ingrese datos para una lista separados con comas (,)")
    ent = input("Datos: ")
    return ent

def oper(datos):
    lista = []
    linea = datos.rstrip().rsplit(",")
    lista.append(linea)
    return lista

def mostrar(nom):
    print(nom[0][0])
    print(nom[0][-1])

if __name__ == "__main__":
    ent = datos()
    data = oper(ent)
    mostrar(data)
