'''
elabore un programa que permita calcular el salario neto(despues de descontar los conceptos de salud,
pension y ARL)
de un empleado 
el programa debe solicitar el tipo de empleado 
A= si es un empleado a termino indefinido
B= contrato de prestacion de servicios
C= contrato de aprendizaje 
D= contrato por jornal(freelance)
'''

contrato = input("ingrese el tipo de contrato: ")
salario_neto = 0 
#inicializar variables:
#
if contrato == "a":
  print ("eligio: contrato a termino indefinido")
elif contrato == "b":
  print ("eligio: contrato de prestacion de servicios")
elif contrato == "c":
  print ("eligio: contrato de aprendizaje")
  salario_minimo = int(input("ingrese valor del salario minimo"))
  salario_neto = salario_minimo - ( salario_minimo * 0.75 )
  print("el salario neto es: ", salario_neto)
elif contrato == "d": 
  print ("eligio: jornal")
  #salario local
  numero_horas = int(input("ingrese el numero de horas: "))
  valor_horas = int(input("ingrese el valor por hora a pagar: "))
  salario_neto = numero_horas * valor_horas
  print("el salario neto es: ", salario_neto )
else:
  print("tipo de contrato no existente")
print ("fin del programa")
  