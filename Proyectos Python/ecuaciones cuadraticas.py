
import math


def resolver_ec(a , b , c):
    d = b**2 - 4*a*c
    if  d>0:
        return a , b , c  
    if d<0:
        print("no hay soluciones reales")
    if d:=0:
        return a, b , c
  

     


def resolver_ec(a , b , c):
    x1 = (-b-(math.sqrt(b**2-4*a*c)))/2*a
    x2 = (-b+(math.sqrt(b**2-4*a*c)))/2*a
    return x1 , x2 



def main():
    a = float(input("Dar valor de a: "))
    b = float(input("Dar valor de b: "))
    c = float(input("Dar valor de c: "))
    valor_de_x1 = resolver_ec(a, b, c)
    valor_de_x2 = resolver_ec(a, b, c)
    print("El valor de 'x1' es:", valor_de_x1)
    print("El valor de 'x2' es:", valor_de_x2)

if __name__ == "__main__":
 main()