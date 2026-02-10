edad = int(input("Ingrese su edad:  "))
pais = input("Ingrese su pais: ")

if pais == "argentina":
           if edad >= 16:
                print("podes votar")
           else:
               print("no podes")
elif edad >= 18:
    print("podes votar")
else:
           print("no podes votar")
