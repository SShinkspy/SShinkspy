import math

from pygame import mixer

mixer.init ()
mixer.music.load("kkcte.mp3")
mixer.music.play()


print("primeiro me diga qual seu nome:")
nome = input()
print()
print ("okay vamos calcular de quanto de tinta voce precisa, quantos metros voce irá pintar?")
metros = float(input())

print()
print()

litros_tinta = (metros/6)
qtd_litros = litros_tinta/18
valor_tinta_litros = math.ceil(qtd_litros)*80

qtd_galoes = litros_tinta/3.6
valor_tinta_galao = math.ceil(qtd_galoes)*25
def conv (var):
    converter = var.replace('.',',')
    print (converter)
mixer.music.stop()

v1 = (f"olá {nome}, voce vai precisar comprar {math.ceil(qtd_litros)} litros de tinta, que vai lhe custar R$:{valor_tinta_litros:,.2f}")
v2 = (f"{nome} ou voce tembém podera comprar {math.ceil(qtd_galoes)} galoes de tinta, que irá lhe custar R$:{valor_tinta_galao:,.2f}")

conv(v1)
conv(v2)