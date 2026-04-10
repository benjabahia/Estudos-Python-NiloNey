#Exercícios do gemini:
#1)
#Escreva um programa que pergunte a quantidade inicial de um produto em
#estoque e a venda média mensal desse produto. O programa deve exibir o estoque mês a mês 
#urante um período de 12 meses. No início de cada mês par (mês 2, 4, 6...)
#a empresa recebe uma reposição fixa de 50 unidades no estoque
#antes de contabilizar a venda do mês. Ao final, exiba o total de itens vendidos no ano.
estoque = int(input("Quantidade do produto em estoque: "))
venda_mensal = float(input("Venda média mensal do produto: "))
mes = 1
saldo = estoque
while mes <= 12:
    if mes % 2 == 0:
        saldo = saldo + 50
    saldo = saldo - venda_mensal 
    print(f"O estoque atualizado no mês {mes} é de {saldo}")
    mes = mes + 1
print(f"No total dos 12 meses foram vendidos {venda_mensal * 12} itens")

#2) Escreva um programa que pergunte o valor de um veículo a ser financiado
#a taxa de juros mensal e o valor da parcela fixa mensal.
#Além disso, o programa deve perguntar um valor de "aporte extra" que o usuário fará a cada 6 meses
# (meses 6, 12, 18...) para reduzir o saldo devedor. 
#O programa deve exibir o saldo devedor mês a mês e interromper quando a dívida chegar a zero
# Informe em quantos meses o veículo foi quitado.

veiculo = float(input("Valor do veiculo a ser financiado: "))
taxa = float(input("Taxa de juros em %: "))
parcela = float(input("Parcela fixa mensal: "))
aporte_extra = float(input("Aporte extra realizado a cada 6 meses: "))
mes = 1 
juros_pagos = 0 
saldo = veiculo
if saldo * (taxa / 100) > parcela:
    print("Juros maior que parcela mensal, financiamento impossível!")
else:
    while saldo >= parcela:
        if mes % 6 == 0:
            saldo = saldo - aporte_extra
        saldo = saldo * (1 + (taxa / 100)) - parcela
        print(f"O saldo devedor no mês de {mes} é de {saldo:,.2f}")
        juros_pagos = juros_pagos + (saldo * (taxa / 100)) 
        mes = mes + 1
print(f"O veículo precisou de {mes - 1} meses pagos com parcelas fixas de {parcela}")
print(f"+ um saldo residual de {saldo:,.2f}")
print(f"O total pago pelo carro foi de {(parcela * mes) + (aporte_extra * (mes // 6)) + saldo:,.2f}")
print(f"Somente de juros foram pagos: {juros_pagos:,.2f}")
        
#3) = Escreva um programa que receba a população atual de duas cidades (A e B) e 
#suas respectivas taxas anuais de crescimento. A Cidade A deve ter obrigatoriamente, uma 
#população menor e uma taxa de crescimento maior que a Cidade B. O programa deve 
#calcular quantos anos serão necessários para que a população da Cidade A iguale ou 
#ultrapasse a da Cidade B, exibindo os valores anuais.

habA = int(input("Habitantes da cidade A: "))
taxaA = float(input("Taxa de crescimento anual (em %) da cidade A: "))
habB = int(input("Habitantes da cidade B: "))
taxaB = float(input("Taxa de crescimento anual (em %) da cidade B: "))
ano = 1
if habA >= habB:
    print("Erro! A cidade A tem que possuir, obrigatoriamente, uma população menor que a da cidade B")
if taxaB >= taxaA:
    print("Erro! A taxa de crescimento anual da cidade A tem que ser obrigatoriamente maior que a da cidade B.")
else:
    while habA < habB:
        habA = habA * (1 + (taxaA / 100))
        habB = habB * (1 + (taxaB / 100))
        ano = ano + 1
print(f"No ano {ano} a população da cidade A ultrapassou a da cidade B em  aproximadamente {habA - habB:6.2f} pessoas")



