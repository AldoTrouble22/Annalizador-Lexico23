print("ingrese el primer numero: ")
n1 = float(input())
print("ingrese el segundo numero: ")
n2 = float(input())
suma=n1+n2
resta=n1-n2
multiplicacion=n1*n2
division=n1/n2

print("la suma es: ",suma)
print("la resta es: ",resta)
print("la multiplicacion es: ",multiplicacion)
print("la division es: ",division)

#radio de un circulo
import math
print("ingrese el radio de un circulo: ")
r = float(input())
pi = math.pi
A = math.pi*(r*r)
print("el area del circulo con radio :",r,"Es",round(A,2))