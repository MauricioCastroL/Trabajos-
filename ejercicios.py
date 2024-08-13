# Autor: Mauricio Castro L
# Calculo área de un circulo

from math import pi

#Función que pida datos (radio)
def datos():
    print("Ingrese la unidad metrica a utilizar")
    tipo = input("cm / m / km: ")
    radio = float(input("¿Cuál es la longitud del radio: "))
    return radio, tipo

#Función que realicel los calculos
def operacion(ent):
    area = pi * ent ** 2 
    return area

def mostrar(mos, med):
    print("El área de este circulo es: ", mos, loco)

if __name__ == "__main__":
    rad, loco = datos()
    entre = operacion(rad)
    mostrar(entre, loco)

