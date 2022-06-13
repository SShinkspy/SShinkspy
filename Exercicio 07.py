#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print ("vamos calcular a área de um retangulo :)")
print ()
print("qual as medidas do retangulo?")
print ()
lar = int(input("LARGURA: "))
comp = int(input("COMPRIMENTO: "))

calculo_area = lar*comp
calculo_areax2 = calculo_area*2
print ("A área do retangulo de largura", lar,"e comprimento",comp,"é:",calculo_area)
print ("o dobro dessa aréa é: ",calculo_areax2)

input ()
