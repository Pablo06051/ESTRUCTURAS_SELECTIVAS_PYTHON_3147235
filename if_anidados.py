'''
son if anidados: 
if dentro de otros if
sintax:

if condicion1:
   if condicion2:
   print (mensaje)
    if condicion3:
    print (mensaje)
     if condicion4: 
      print(mensaje)
       if condicion5:
       print(mensaje)
         if condicion6:
          print(mensaje)
   
'''

# EJEMPLO !
#MODIFIQUE EL EJERCICIO DE LA EDAD PARA 
#LAS SIGUIENTES CONDICIONES 
# EJE: SI ES MAYOR DE 18 AÑOS PERO NO TIENE DOCUMENTO NO PUEDE VOTAR
# DE LO CONTRARIO SI PUEDE VOTA.
# SI ES MENOR DE 18 AÑOS NO PUEDE VOTAR
# UTILICE ESTRUCTURA DE IF ANINADOS

edad = int (input("ingrese su edad: "))
if edad >= 18:
    documento = input("tiene documento? (si/no): ")
    if documento == "si":
       print ("puede votar")
    else:
     print ("no puede votar")
else:
   print("no puede votar")