"""
IF EN CASCADA
Es una estructura selectiva compuesta por multiples
condicionales seguidos unos de otros 
sintaxis:
if condicional 1
instruccion 1
instruccion 2
elif condicional 2 
instruccion 1
instruccion 2

NOTA
"""
#vamos a hacer un traductor 
#el programa debe permitir 
#leer una fruta en español 
#y traducirlo al ingles

fruta_es = input("ingrese fruta: ")
if fruta_es == "manzana" or fruta_es == "manzana":
    print("apple")
elif fruta_es == "naranja" or fruta_es == "naranja":
    print("orange")
elif fruta_es == "uva" or fruta_es == "uva":
    print("grape")
else:
    print("fruta no reconocida")