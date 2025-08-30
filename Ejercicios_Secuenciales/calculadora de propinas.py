#Calculadora de propinas en un restaurante

#El programa debe:
#✓ Pedir al usuario el monto total de la cuenta.
#✓ Calcular la propina sugerida al 10%.
#✓ Calcular la propina sugerida al 15%.
#✓ Calcular el total a pagar en ambos casos (cuenta + propina).
#✓ Mostrar todos los resultados en pantalla.

cuenta = float(input("Ingrese el monto total de la cuenta: "))

propina_1= cuenta * 0.10
total_1 = cuenta + propina_1

propina_2 = cuenta * 0.15
total_2 = cuenta + propina_2

print("Propina calculada (10%):", propina_1)
print("Total a pagar (10%):", total_1)

print("Propina calculada (15%):", propina_2)
print("Total a pagar (15%):", total_2)
