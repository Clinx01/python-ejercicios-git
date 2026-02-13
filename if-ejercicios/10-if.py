n1 = int(input("Ingrese el primer: "))
n2 = int(input("Ingrese el segundo: "))
n3 = int(input("Ingrese el tercero: "))
if n1 > n2:
    if n1 > n3:
        print("El primero es mayor")
    elif n3 > n2:
        print("El tercero es el mayor")
elif n2 > n3:
    print ("El segundo numero es el mayor")
else:
    print("El tercer numero es el mayor")

