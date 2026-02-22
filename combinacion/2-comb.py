palabra = str(input("Ingrese una palabra: "))
invertida = ""

for i in range(len(palabra) -1, -1,-1):
    invertida += palabra[i]

print(invertida)
