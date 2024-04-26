def main():
    sueldo_base = float(input("Cual es su sueldo base: "))
    comision1 = float(input("el valor de mi primera comision es: "))
    comision2 = float(input("el valor de mi segunda comision es: "))
    comision3 = float(input("el valor de mi tercera comision es: "))
    valor_de_x = resolver_ec(comision1 ,comision2 , comision3, sueldo_base )
    print("su sueldo es: ", valor_de_x)


def resolver_ec(comision1 , comision2 , comision3, sueldo_base):
    x = sueldo_base + ((comision1+comision2+comision3)/10)
    return x
    

if __name__ == "__main__":
 main()
    
