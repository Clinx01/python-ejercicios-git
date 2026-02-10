edad = int(input("Ingrese su edad: "))
licencia = input("Usted tiene una licencia de conducir? ")
alcholenSangre = input ("Usted esta alcholizado? ")
pais = input("Ingrese su pais: ")

if alcholenSangre == "no":
    if licencia == "si":
        if pais == "argentina":
            if edad >= 17:
                print("Podes conducir")
            else:
                print("no podes conducir sos menor de edad")
        else:
            if edad >= 18:
                print("podes conducir en otro pais")
            else:
                print("No podes conducir")
    else:
        print("No tenes licencia no podes conducir")
else:
    print("Estas alcholizado no podes conducir")
