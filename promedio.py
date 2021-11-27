print("sacar promedio")
mat1=float(input("ingrese la calificasion METROLOGIA:"))
mat2=float(input("ingrese la calificasion ALGEBRA:"))
mat3=float(input("ingrese la calificasion CALCULO:"))
mat4=float(input("ingrese la calificasion ECONOMIA:"))
mat5=float(input("ingrese la calificasion ESTADISTICA:"))
mat6=float(input("ingrese la calificasion ESTUDIO DEL TRABAJO:"))

total=((mat1+mat2+mat3+mat4+mat5+mat6)/6)
print("promedio:"+str(total))
if (total>=6 and total<=7.9):
 print ("pansaso")   
if (total>=8 and total<=8.9):
 print ("pasaste muy bien")
if (total>=9 ):
 print ("exelente")   