#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

print ("olá vamos converter temperatura agora")
print ()
print ("me fala ai se vc quer converter")
print ("celcios em farenheit DIGITE A, ou Fahenreit em celsios DIGITE B")
choss = input()
if choss == "a":
    print ("Okay, agora digite quantos graus Celcius vc quer conveter:")
    celcius_temp = float(input())
    celcius_temp_converter =celcius_temp*1.8+32
    print (f"{celcius_temp:,.1f} celcios, em farenheit fica {celcius_temp_converter:,.1f}")

elif choss == "b":
    print ("blz então gita ai quantos graus farenheit vc quer converter")
    farenheit_temp = float(input())
    farenheit_temp_conveter = (farenheit_temp-32)/1.8
    print (f"{farenheit_temp:,.1f} farenheit em celcios é {farenheit_temp_conveter:,.1f}")

else:
    print("escolha invalida")