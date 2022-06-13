#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.



print ("voce vai querer calcular qual seu ganho pelo tempo trabalhado, ou o ganho por hora trabalhada?")

choss = input()


if choss == "a":
    print ("quantas horas voce trabalha por dia? ")
    horas_trabalhadas = int(input())
    print ()

    print ("blz, agora me diz quanto que vc ganha por hora trabalhada?")
    ganho_hora = float(input())

    print ("Agora me fala quantos dias vc Trabalha no mes?")
    dias_trabalhados = int(input())

    ganho_mes = (ganho_hora * horas_trabalhadas) * dias_trabalhados
    ganho_dia = horas_trabalhadas * ganho_hora

    print("voce ganha por mes R$:",ganho_mes)
    print("voce ganha por dia R$:",ganho_dia)

elif choss == "b":
    print ("blz então me diz ai quanto voce ganha por mes?")
    ganho_mensal = float(input())

    print ("agora me diz ai quantos dias tu trabalha por mes")
    dias_trabalho = int(input())

    print ("agora me diz ai quantas horas vc trabalha por dia")
    horas_trabalho = float(input())


    res_ganho_hora = (ganho_mensal/dias_trabalho)/horas_trabalho
    res_ganho_dia = ganho_mensal/dias_trabalho
    res_ganho_ano = ganho_mensal*12

    def convert_simbol(palavra,variavel):
        variavel.replace(".", ",").replace("_", ".")
        print (palavra,variavel)

    print ()
    ga = (f"voce ganha por ano R$:{res_ganho_ano:_.2f}")
    ga = ga.replace(".",",").replace("_",".")
    print (f"{ga}")

    gd = (f"voce ganha por dia R$:{res_ganho_dia:_.2f}")
    gd = gd.replace(".", ",").replace("_", ".")
    print (f"{gd}")

    gh = (f"voce ganha por hota R$:{res_ganho_hora:_.2f}")
    gh = gh.replace(".", ",").replace("_", ".")
    print (f"{gh}")

    ga2 = (f"voce ganha em dois anos {res_ganho_ano*2:_.2f}")
    ga2 = ga2.replace(".", ",").replace("_", ".")
    print (f"{ga2}")

    gm = (f"que é equivalente a R$:{ganho_mensal-1212:_.2f} a mais que o salario minimo ou seja {10:,.0f}% a mais")
    gm = gm.replace(".", ",").replace("_", ".")
    print (f"{gm}")





input()
