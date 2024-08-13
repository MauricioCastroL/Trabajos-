#Autor: Mauricio Castro Leal 
#Fecha:24-06-2024


def lectura():
    datos = []
    Edad_s= int(input("0 para meses / 1 para años: "))
    Edad = int(input("Edad: "))
    Hemoglobina= float(input("Porcentaje de hemoglobina: "))
    sexo = input("masculino / femenino: ")
    sexo = sexo.lower()
    if sexo == "masculino":
        sexo = "True"
    elif sexo == "femenino":
        sexo = "False"
    datos.append(sexo) #0
    datos.append(Hemoglobina)#1
    datos.append(Edad)#2
    datos.append(Edad_s)#3
    print(datos)
    return datos

def operativa(nombre):
    if datos[3] == 0 and datos[2]<=1 and datos[1]>= 12 and datos[1]<=16:
        a = "positivo"
    elif datos[3] == 0 and datos[2]<=1 and datos[1]< 12:
        a ="Negativo por debajo"  
    elif datos[3] == 0 and datos[2]<=1 and datos[1]> 16:
        a = "negativo por arriba"
    elif datos[3] == 0 and datos[2]>1 and datos[2]<6 and datos[1]>= 14 and datos[1]<=18:
        a = "positivo"
    elif datos[3] == 0 and datos[2]>1 and datos[2]<6 and datos[1]>18:
        a = "negativo por arriba"
    elif datos[3] == 0 and datos[2]>1 and datos[2]<6 and datos[1]<14:
        a = "negativo por abajo"
    return a
        
def muestra(datos):
    print(datos)
    
    


if __name__=="__main__":
    datos = lectura()
    ope = operativa(datos)
    muestra(ope)