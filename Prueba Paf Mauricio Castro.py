
# FUNCION QUE PIDA DATOS
def datos():
    lista = []
    xp = float(input("Ingrese coordenada x, en el primer punto: "))
    yp = float(input("Ingrese coordenada y, en el primer punto: "))
    zp = float(input("Ingrese coordenada z, en el primer punto: "))
    xs = float(input("Ingrese coordenada x, en el segundo punto: "))
    ys = float(input("Ingrese coordenada y, en el segundo punto: "))
    zs = float(input("Ingrese coordenada z, en el segundo punto: "))
    lista.append(xp)
    lista.append(yp)
    lista.append(zp)
    lista.append(xs)
    lista.append(ys)
    lista.append(zs)
    return lista

#FUNCION QUE SUME
def suma(sum):
    resultados = []
    sumasx = sum[0] + sum[3]
    sumasy = sum[1] + sum[4]
    sumasz = sum[2] + sum[5]
    resultados.append(sumasx)
    resultados.append(sumasy)
    resultados.append(sumasz)
    return resultados


def produ(nom):
    productox = nom[0] * nom[3]
    productoy = nom[1] * nom[4]
    productoz = nom[2] * nom[5]
    a = productox + productoy + productoz 
    return a


def mostrar(a,b,c):
    print("El primer punto es: " , a[0:3])
    print("El segundo punto es: ", a[3:6])
    print("La suma de los ", b)
    print("El escalar es: " , c)


if __name__ == "__main__":
    lista = datos()
    sumando = suma(lista)
    producto = produ(lista)
    mostrar(lista, sumando, producto)