# Gine: 40%, Traumatología 30%, Pediatría 30%


presupuesto_anual = float(input("cual es el presupuesto total: "))
ginecologia = presupuesto_anual-(presupuesto_anual * 0.4)
traumatologia = (presupuesto_anual * 0.7)
pediatria = presupuesto_anual- (presupuesto_anual * 0.3)

print("traumatologia recibe un total de: ", traumatologia)
print("pediatria recibe un total de: ", pediatria)
print("ginecologia recibe: ", ginecologia)
