numero = int(input("Ingresa un numero: "))
divisor = 2
es_primo = True

if numero <= 1:
    es_primo=False


while divisor < numero:
    if numero % divisor == 0:
        es_primo = False
        break
    divisor += 1

if es_primo == True:
    print("Es primo")
else:
    print("No es primo")



