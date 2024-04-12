vlansw1= [10,20,30]
vlansw2= [40,50,60]
vlanrequerimiento= [10,100,30]

if nativew1 == 99:
    print("la vlan nativa de SW1 es correcta y cunple con el requerimiento")
else:
    print("la vlan nativa de SW1 no es correcta y no cumple con el requerimiento")

if vlansw1 == vlanrequerimiento:
    print("las vlans de SW1 son iguales y cunplen con el requerimiento")
else:
    print("las vlans de SW1 no son iguales y no cumplen con el requerimiento")

if nativesw2 == 200:
    print("la vlan nativa de SW2 no es correcta y no cumple con el requerimiento")

if vlansw2 == [40,50,60]
   print("las vlans de SW2 son iguales y cumplen con el requerimiento")
else:
    print("las vlans de SW2 no son iguales y no cumplen con el requerimiento")