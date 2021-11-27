print("calculo del imc para adultos de 20 años o más")
peso=float(input("ingresa tu peso en kilogramos:"))
altura=float(input("ingrresa tu altura en mebtros:"))
imc=(peso/(altura*altura))
print ("INDICE DE MASA CORPORAL ES:"+str (imc))

if (imc>18.4 and imc<24.8 ):
 print ("Saludable")   
if (imc<18.5 ):
 print ("Bajo de Peso")  
if (imc>=25 and imc<=29.9 ):
 print ("Sobrepeso")   
if (imc>30 ):
 print ("Obesidad")