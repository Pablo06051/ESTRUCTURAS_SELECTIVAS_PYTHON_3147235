'''
if else:
determinar dos caminos de ejecucion.
 basados en la evaluacion de una condicional
 sintaxis:
 if instruccion 1
    instruccion 2
else 
    instruccion 3
    instruccion 4

'''
# EJEMPLO 
# elabore un programa en python 



edad = 20
documento = False

if edad >= 18 and documento==True:
    print("usted es mayor de edad")
    print("puede votar")
else:
    print("usted es menor de edad")
    print("o")
    print("no yiene documento")
    print("no puede votar")
    print("fin del programa")