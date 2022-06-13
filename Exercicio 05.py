#Faça um Programa que converta metros para centímetros.

print ("VAMOS CONVETER")
print ()
print ("metros para centimetros? ESCOLHA X")
print ("centimentros para metros? ESCOLHA Y")

chs = input()

if chs == 'x':
    print ("certo agora me informe quantos metros vc quer converter: ")
    mtc = float(input())
    mtcr = mtc*100
    print(mtc," metros, é igual a ",int(mtcr),"cm")
elif chs == 'y':
    print ("certo agora me informe quantos centimentos voce quer convetre ")
    ctm = float(input())
    ctmr = ctm/100
    print (int(ctm)," centimentos é igual a ",ctmr,"metros")
else:
    print ("escolha invalida")
 
 




input ()
