'''
elabore un programa que permita calcular el salario neto(despues de descontar los conceptos de salud,
pension y ARL)
de un empleado 
el programa debe solicitar el tipo de empleado 
A= si es un empleado a termino indefinido
B= contrato de prestacion de servicios
C= contrato de aprendizaje 
D= contrato por jornal(freelance)
para el caso de prestacion de servicios 
se solicita 
-el valor del contrato
-el numero de meses del contarto
la anticipacion del empleado (años)
el salario neto , en este caso e calcula: 
1- dividir el contrato por el numero de meses 
2- restar el 15% del valor del contrato

Para el caso de contrato a termino indefinido
   se debe solicitar:
   - Antiguedad (años)
   - Grado o escalafon (1 - 5)
   - El salario minimo
   El salario mensual se calcula de acuerdo
   a la siguiente tabla:
   - grado 1: 1.5 SM
   - grado 2: 1.7 SM
   - grado 3: 2.0 SM
   - grado 4: 2.5 SM    
   - grado 5: 3.0 SM
   La bonificacion estará acorde a
   Los siguientes rangos segun la
   antiguedad:
   - entre 1 y 5 años: 1% del salario mensual
   - entre 6 y 10 años: 2% del salario mensual
   - superior a 10 años: 3 %  del salario mensual
   Para este caso, los descuentos de ley son:
   - 25% por concepto de EPS
   - 22 % por concepto de Pension
   - 0.1 % por concepto de ARL
'''

contrato = input("ingrese el tipo de contrato: ")
salario_neto = 0 
#inicializar variables:
#
if contrato == "a":
    print ("Eligio: contrato a termino indefinido")
    antiguedad = int(input("Ingrese la antiguedad del empleado (Año):"))
    grado = int(input("Ingrese el grado del empleado:(1-5)"))
    salario_neto= int(input("Ingrese el salario neto del empleado:"))
    salario_minimo = int(input("Ingrese el salario minimo:"))
    if grado == 1:
        salario_neto = salario_minimo*1.5
    elif grado == 2:
        salario_neto = salario_minimo*1.7
    elif grado == 3:
        salario_neto = salario_minimo*2.0
    elif grado == 4:
        salario_neto = salario_minimo*2.5
    elif grado == 5:
        salario_neto = salario_minimo*3.0
    if antiguedad >= 1 and antiguedad <= 5:
        salario_neto = salario_neto + (salario_minimo*0.01)
    elif antiguedad >= 6 and antiguedad <= 10:
        salario_neto = salario_neto + (salario_minimo*0.02)
    elif antiguedad >= 10:
        salario_neto = salario_neto + (salario_minimo*0.03)
    salario_neto = salario_neto - (salario_neto*0.25) - (salario_neto*0.22) - (salario_neto*0.001)
        
elif contrato == "b":
  print ("eligio: contrato de prestacion de servicios")
  valor_contarto = int(input("ingrese el valor del contarto: "))
  numero_meses = int(input("ingrese antiguedad del empleado (años): "))
  salario_anual = valor_contarto/numero_meses
  EPS =salario_anual*0.15
  pension = salario_anual*0.30
  bonificacion = salario_anual*0.05
  salario_neto =salario_anual - EPS -pension
  if numero_meses >= 10:
      salario_neto = salario_neto*bonificacion
      print ("su contrato es de: ", salario_neto)
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
  