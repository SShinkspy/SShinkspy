
print ("informe o peso da blança")
peso = float(input())

print ()

if peso > 50.0:
    exesso = peso - 50
    multa = exesso*4.5
    res = (f"voce pagará R${multa:,.2f} de multa pelo exesso!")
    res = res.replace(".",",")
    print (res)

elif peso <=50:
    print ("o peso nõ deu excesso, não pagará multa")


