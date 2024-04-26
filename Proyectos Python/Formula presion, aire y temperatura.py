#La presión, el volumen y la temperatura de una masa de aire se relacionan por la formula: 
presion = float(input("La presion es: "))
volumen = float(input("El volumen es: "))
temperatura = float(input("La temperatura es: "))
masa = (presion * volumen)/(0.37 * (temperatura + 460))
print("El resultdo es: ", masa)
