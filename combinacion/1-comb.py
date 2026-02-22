lista = []
listaOrdenamenor = []
listaOrdenamayor = []
for i in range(10):
    dato =int(input("Ingrese 10 numeros enteros:"))
    lista.append(dato)

while len(lista) > 0:
    menor = lista[0]
    for i in lista[1:]:
        if i < menor:
            menor = i
    listaOrdenamenor.append(menor)
    lista.remove(menor)

print(listaOrdenamenor)
