# Al ingresar a,b,c



def resolver_ec(a , b , c):
   x = (c-b)/a   
   return x



def main():
    a = float(input("Ingrese valor de a: "))
    b = float(input("Ingrese valor de b: "))
    c = float(input("Ingrese valor de c: "))
    valor_de_x = resolver_ec(a , b , c )
    print("El valor de 'x' es:", valor_de_x)

if __name__ == "__main__":
 main()
