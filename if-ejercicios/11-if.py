numero = int(input("Ingrese un numero: "))
if numero % 3 ==  0 and numero % 5 == 0:
    print ("Multiplo de ambos")
elif numero % 3 == 0:
    print("Es multiplo de 3")
elif numero % 5 == 0:
    print ("Es multiplo de 5")
else:
    print ("No es multiplo")
