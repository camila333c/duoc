NumACL = int(input("ingrese el numero de la access list:"))
if NumACL >= 1 and NumACL <=99:
    print("es una access-lis de tipo estandar")
    if NumACL == 50:
        print("ip access-list 50 permit any")
    if NumACL == 20:
        print("ip access-lis 20 deny any")
elif NumACL >= 100 and NumACL <=199:
    print("Es una access-list de tipo extendida")
    if NumACL == 100:
        print("ip access-list 100 permit ip any any")
else:
    print("esto se encuentra fuera de rango")