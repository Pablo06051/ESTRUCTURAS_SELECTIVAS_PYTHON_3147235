precio_matri = int(input("escriba el precio de su matricula: "))
est = int(input("escriba su estrato: "))
edad = int(input("escriba su edad: "))

if  edad < 18 and  est == 1:
    precio_matri = precio_matri * 0.8
    print ("su descuento es de 20%") 
    print ("el precio final de su matricula es: ",precio_matri)
elif edad >= 18 and est == 1:
    precio_matri = precio_matri / 0.85
    print ("su descuento es del 15%")
    print ("el precio final de su matricula es: ",precio_matri)
elif edad < 18 and est == 2:
    precio_matri = precio_matri * 0.9
    print ("su descuento es del 10%")
    print ("el precio final de su matricula es: ",precio_matri)
elif edad >= 18 and est == 2:
    precio_matri = precio_matri * 0.95
    print ("su descuento es del 5%")
    print ("el precio final de su matricula es: ",precio_matri)
else:
    print("no se le aplica descuento")