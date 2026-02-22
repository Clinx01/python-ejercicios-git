#Lista "infinita"
numeros = []
copia = numeros [:]
copia2 = numeros [:]

menorlist = []
mayorlist = []

while True:
    entrada = int(input("Ingresa un numero (o escribe 0 para terminar): "))
    if entrada == 0:
        break
    numeros.append(entrada)
#Copiando lista y extrayendo cantidad de elementos
copia = numeros [:]
copia2 = numeros [:]
cantidad = len(numeros)

print("La cantidad de elementos en la lista ingresada son " + str(cantidad))

#Menor
while len(copia) > 0:
    menor = copia[0]
    for i in copia[1:]:
        if i < menor:
            menor = i
    copia.remove(menor)
    menorlist.append(menor)

print ("El numero mas pequeño ingresado es " + str(menorlist[0]))

#Mayor 
while len(copia2) > 0:
    mayor = copia2[0]
    for i in copia2[1:]:
        if i > mayor:
            mayor = i
    copia2.remove(mayor)
    mayorlist.append(mayor)

print("El numero mas grande ingresado es " + str(mayorlist[0]))


#Promedio


promedio = sum(numeros) / len(numeros)


print("El promedio de los numeros ingresados es " + str(promedio))























