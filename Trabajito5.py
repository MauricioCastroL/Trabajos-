#Autor: Mauricio Castro L
#Fecha: 21-06-2024

#Pedir valores
print("Ingrese los valores que quiera")
num = (input("Ingrese los valores separados por una ´,´: "))
val = []
val.append(num.lstrip("\n").split(","))
print(val)



#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
#Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
def function(datos):
    j = 0
    for i in datos:
        j = i
    print(j)






if __name__ == "__main__":
    pa = function(val)