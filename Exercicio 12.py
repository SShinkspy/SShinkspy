print("vamos calcular seu salario!")
print()
print("quantas hrs voce trabalha por dia?")
hora_dia = float(input())
print("quantos dias na semana voce trabalha?")
dia_semana = int(input())
print("certo, e quanto voce recebe por hora?")
ganho_hora = float(input())

#calculo de salario bruto liquido e descontos
salario_semanal = hora_dia * dia_semana * ganho_hora
salario_mensal = salario_semanal*4
desconto_ir = (salario_mensal/100)*11
desconto_inss = (salario_mensal/100)*8
desconto_sindicato = (salario_mensal/100)*5
salario_liquido = (((salario_mensal-desconto_sindicato)-desconto_ir)-desconto_inss)

print("de acordo com os meus calculos, seu salaria ficará assim:")



a = (f"R$:{salario_mensal:_.2f}")
b = (f"R$:{desconto_ir:_.2f}")
c = (f"R$:{desconto_inss:_.2f}")
d = (f"R$:{desconto_sindicato:_.2f}")
e = (f"R$:{salario_liquido:_.2f}")

#função que converter os sinais para os corretos e manda printat a string desejada com os simbolos convertidos
def conv(palavra,varr):
    convertida = varr.replace(".",",").replace("_",".")
    print (varr,convertida)

#usando a função
conv("seu salario mensal é",a)
conv("Desconto do IR",b)
conv("Desconto do INSS", c)
conv("desconto do sindicato",d)
conv("seu salario liquido é ",e)

