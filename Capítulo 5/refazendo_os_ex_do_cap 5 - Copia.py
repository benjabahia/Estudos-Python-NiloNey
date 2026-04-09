#Vou refazer os exercícios pra ver se eu to conseguindo de boa.
#Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo.
#Utilize apenas os operadores de soma e subtração para calcular o resultado.
#Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
#Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
x = 1
soma = 0
while x <= num2:
   soma = soma + num1 
   x = x + 1
print(f"{num1} x {num2} = {soma}")

#Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão
#ilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender
#o quociente da divisão de dois números como a quantidade de vezes que
#podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos 
#subtrair 4 cinco vezes de 20.

num1 = int(input("numéro 1: "))
num2 = int(input("número 2: "))
resultado = num1
x = 0
while resultado >= num2:
    resultado = resultado - num2
    x = x + 1
print(f"{num1} / {num2} = {x}, sobra = {resultado}")

#Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.
pontos = 0 
questao = 1
while questao <= 3:
    resposta = input(f"Resposta da questão {questao}: ")
    if questao == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1 
    if questao == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questao == 3 and (resposta == "d" or resposta == "D"):
        pontos = pontos + 1
    questao = questao + 1 
print(f"O aluno fez {pontos} ponto(s)!")

#Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança
#Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

deposito_incial = float(input("Digite aqui o seu depósito inicial: "))
taxa = float(input("Taxa de juros da poupança (em %):  "))
x = 1
soma = deposito_incial
while x <= 24:
    soma = soma + (soma * (taxa / 100))
    print(f"O valor acumulado até o mês {x} é de: {soma:5.2f}")
    x = x + 1
print(f"O total ganho com juros foi de: {soma - deposito_incial:5.2f}")

#Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
#Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

deposito_incial = float(input("Digite aqui o seu depósito inicial: "))
taxa = float(input("Taxa de juros da poupança (em %):  "))
valor_mensal = float(input("Quanto você quer adicionar mensalmente? "))
x = 1
soma = deposito_incial
while x <= 24:
    soma = soma + (soma * (taxa / 100)) + valor_mensal
    print(f"O valor acumulado até o mês {x} é de: {soma:5.2f}")
    x = x + 1
print(f"O total ganho com juros foi de: {soma - deposito_incial - (24 * valor_mensal):5.2f}")
    
#Exercício 5.13 - Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal
#que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
divida = float(input("Dívida: "))
taxa = float(input("Taxa de juros em %: "))
parcela = float(input("Parcela: "))
mes = 1
juros_pago = 0
saldo = divida
if divida * (taxa / 100) > parcela:
    print("Juros maior que parcela, não é possível pagar!")
else: 
    while saldo >= parcela:
        juros_pago = juros_pago + (saldo * (taxa / 100))
        saldo = (saldo * (1 + (taxa / 100))) - parcela
        print(f"Após o mês {mes} a dívida é de {saldo:5.2f}")
        mes = mes + 1 
print(f"Para pagar a dívida será necessário {mes -1} meses de parcelas fixas de R${parcela} + um saldo residual de: {saldo:5.2f} ")
print(f"Você pagou no total {divida + juros_pago + (parcela * mes):6.2f}")
print(f"Somente de juros foram {juros_pago:6.2f}")
        
        








        
    


