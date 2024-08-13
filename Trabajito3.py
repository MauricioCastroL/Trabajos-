#Autor: Mauricio Castro L
#Date: 21-06-2024 23:06


#Funcion que cuente el largo de una lista o string (.len())
dat = "Hola mundo"
list = ["Hola", "Que", "Tal"]

def largo(dat):
    j = 0 
    for l in dat:
        j += 1
    print(j)

def largo1(dat):
    j = 0 
    for l in dat:
        j += 1
    print(j)

if __name__ == "__main__":
    da = largo(dat)
    da1 = largo1(list)
