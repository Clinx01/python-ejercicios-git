frase = input("Ingrese una frase corta ")
cantidad = len([i for i in frase if i != " "])
print (cantidad)
palabras = []
palabra_actual = ""
for i in frase:
    if i != " ":
        palabra_actual += i
    else:
        palabras.append(palabra_actual)
        palabra_actual = ""
if palabra_actual:
    palabras.append(palabra_actual)
    palabra_actual=""

print(len(palabras))
vocales = "aeiou"
cantidadVocales = len([i for i in frase.lower() if i in vocales])
print(cantidadVocales)
#Palabra mas larga, no hace falte reiniciar la variable palabra_actual, ya que ya no contiene ningun valor.
palabra_larga = ""
for i in frase:
    if i != " ":
        palabra_actual += i
    else:
        if len(palabra_actual) > len(palabra_larga):
            palabra_larga = palabra_actual
        palabra_actual = ""
if palabra_actual != "":
    if len(palabra_actual) > len(palabra_larga):
        palabra_larga = palabra_actual
    palabra_actual = ""
print (palabra_larga)
