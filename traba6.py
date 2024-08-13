#Autor: Mauricio Castro L
#Fecha: 21-06-2024

#Pedir valores
print("Ingrese los valores que quiera")
num = (input("Ingrese los valores separados por una ´,´: "))
val = []
val.append(num.split(","))
print(val)



#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
#Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
def function(datos):
    j = 0
    for i in datos:
        j += float(i[0])
        j += float(i[1])
        j += float(i[2])
        j += float(i[3])
        j += float(i[4])
    print(j)

def multi(datos):
    j = 1
    for i in datos:
        j = j*float(i[0])
        j = j*float(i[1])
        j = j*float(i[2])
        j = j*float(i[3])
        j = j* float(i[4])
    print(j)






if __name__ == "__main__":
    pa = function(val)
    pe = multi(val)