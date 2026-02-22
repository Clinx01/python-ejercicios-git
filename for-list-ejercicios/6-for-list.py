lista = [4, 7, 1, 9, 3]


mayor = lista[0]
menor = lista[0]

for numero in lista[1:]:
    if numero > mayor:
        mayor = numero

    if numero < menor:
        menor = numero

print(str(menor) + " Es el menor de la lista")
print(str(mayor) + " Es el mayor de la lista")
