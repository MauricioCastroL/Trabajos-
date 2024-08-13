#Autor: Mauricio Castro L.

def datos():
    lista = []
    dato = (input("ingrese los numeros que quiera: "))
    for i in dato:
        linea = i.rsplit()
        lista.append(linea)
    return lista

def mostrar(datos):
    print(datos[0:])
        

if __name__ == "__main__":
    data = datos()
    mostrar(data)
