

def lectura(arch_entrada):
    dias = []
    temp = []
    abrir = open(arch_entrada)
    for i in abrir:
        dia , temperatura = i.rstrip().rsplit(":")
        dias.append(dia)
        temp.append(float(temperatura))
    abrir.close()
    print(dias)
    print(temp)
    return dias , temp
    
def tem_media(dias , temp):
    promedio = sum(temp) / len(dias)
    return round(promedio, 2)
    
def tem_max(temp):
    maxima = max(temp)
    return maxima


def tem_min(temp):
    minima = min(temp)
    return minima

def mostrar(media , maximo, minimo):
    print("Temperatura media de la semana: " , media)
    print("Día más caluroso: " , maximo)
    print("Día más frio: " , minimo)
    


if __name__ == "__main__":
    dias , temp = lectura("temperaturas.txt")
    media = tem_media(dias , temp)
    maximo = tem_max(temp)
    minimo = tem_min(temp)
    mostrar(media , maximo, minimo)