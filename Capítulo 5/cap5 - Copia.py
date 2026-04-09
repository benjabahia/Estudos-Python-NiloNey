#Repetições
#A estrutura while repete um bloco enquanto a condição exposta for verdadeira
#Ex;
x = 1
while x <= 3:
    print (x)
    x = x + 1
    
#Eu basicamente falei assim p ele, por enquando que x for menor ou igual a 3, eu quero que tu fique repetindo esse bloco, que diz pra tu printar o x smad com 1 unidade.

#Exercício 5.1 - Modifique o programa para exibir os números de 1 a 100.
x = 1
while x <= 100:
    print(x)
    x = x + 1
    
#Exercício 5.2 - Modifique o porgrama para exibir os números de 50 a 100:
x = 50
while x <= 100:
    print(x)
    x = x + 1 

#Exercício 5.3 - Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
#O programa deve imprimir 10,9,8...,1,0 e Fogo! na tela.
x = 10
while x >= 0:
    print(x)
    x = x - 1
print("Fogo!")

#5.1 Contadores
#Contador é uma variável que serve para acompanhar quantas vezes algo aconteceu

fim = int(input("Digite o último número a imprimir: "))
x = 1
while x <= fim:
    print (x)
    x = x + 1 
    
#Nesse caso nosso X é o contador pois ele inicia valendo 0 e vai até o valor limite.

#Problema: Imprimir apenas os números pares enre 0 e um número digitado pelo usuário.
#Pode testar com if se o número é par antes de imprimi-lo, para ser par tem que ser 0 ou múltiplo de 2, no caso de ser múltiplo de 2
#signidica que quando esse número é dividido por 2, não sobra resto nenhum.

fim = int(input("Digite aqui o número limite:" ))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1

#Ou também poderia ser feito assim:

fim = int(input("Digite aqui o número limite: "))
x = 0
while x <= fim:
    print(x)
    x = x + 2
    
#Exercício 5.4 - Modifique o porgrama anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.
fim = int(input("Digite aqui o número limite : "))
x = 1
while x <= fim:
    print(x)
    x = x + 2

#Exercício 5.5 - Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
x = 3
while x <= 30:
    print(x)
    x = x + 3
    
#Tabuada de adição:
n = int(input("Digit um número entre 0 e 10: "))
x = 1 
while x <= 10:
    print (n + x)
    x = x + 1

#Exercício 5.6 - ltere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4, …
n = int(input("Tabuada do: "))
x = 1
while x <= 10:
    print(f"{n} x {x} = {(n * x)}")
    x = x + 1

#Exercício 5.7 - Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
n = int(input("Tabuada do : "))
inicio = int(input("Quer iniciar a tabuada com que valor? "))
fim = int(input("Quer saber a tabuada até que valor? o máximo é 10: " ))
if fim >= inicio:
    while inicio <= fim:
       print(f"{n} x {inicio} = {(n * inicio)}")
       inicio = inicio + 1

#5.8 - Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. 
#Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação
#de dois números como somas sucessivas de um deles.
#Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
contador = 1 #Começa em 1 e vai aumentado até o segundo número. Ele garante que você nn some a mais nem a menos.
resultado = 0 
while contador <= num2: #Enquanto meu contador não ultrapassar o segundo número, continue fazendo isso:
    resultado = resultado + num1
    contador = contador + 1
print(f"{num1} x {num2} = {resultado}")

#Exemplo: 5 e 7, contador = 1, resultado = 0, por enquanto que o contador for menor que 7: adicione o primeiro número e aumente uma unidade do contador
#1 < 7, logo: resultado = 5, contador = 2, depois 2 < 7, logo: resultao = 10, contador = 3, depois 3 < 7, logo: resultado = 15, contador = 4
#.. até contador = 7, e o resultado dar 35.

#5.9 - Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão
#Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números
#omo a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

dividendo = int(input("dividendo: ")) #O estoque total, ex: 20 garrafas
divisor = int(input("divisor: ")) #Quantas garrafas nós vamos colocar em cada caixa
quociente = 0 #O contador de caixas, começa com 0. Toda vez que eu monto um kit, eu marco mais 1 no meu caderninho.
x = dividendo
while x >= divisor: #Enquanto que eu tenho na mesa uma quantidade de garrafas maior que o tamanho de um kit, continue retirando as garrafas para o kit.
    x = x - divisor #Removi as garrfas da mesa para a realização de um kit.
    quociente = quociente + 1  #"Mointei mais um kit!" Adiciono mais 1 ao meu contador de kits.
resto = x #Após as sucessivas subtrações, quando o dividendo passa a ser menor que o divisor, o resto é exibido.
print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")

#Exemplo de programa utilizando condições acopladas a estruturas de repetições

pontos = 0 
questao = 1
while questao <= 3:
    resposta = input(f"Resposta da questão {questao}: ")
    if questao == 1 and resposta == "b":
        pontos = pontos + 1 
    if questao == 2 and resposta == "a":
        pontos = pontos + 1
    if questao == 3 and resposta == "d":
        pontos = pontos + 1
    questao = questao + 1 
print(f"O aluno fez {pontos} ponto(s)!")
    
#Exercício 5.10 - Modifique o programa para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.

pontos = 0 
questao = 1
while questao <= 3:
    resposta = input(f"Resposta da questão {questao}: ")
    if questao == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    elif questao == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1 
    elif questao == 3 and (resposta == "d" or resposta == "D"):
        pontos = pontos + 1 
    questao = questao + 1 
print(f"O aluno fez {pontos} ponto(s)!")

#Acumuladores 5.2 - É tipo um contador, porém o valor adicionado não é constante e sim variável.
#Ex:
n = 1 #n é um contador
soma = 0 #soma é um acumulador
while n <= 10:
    x = int(input(f"Digite o {n} número: "))
    soma = soma + x 
    n = n + 1
print(f"Soma: {soma}")

#Usando contadores e acumuladores para calcular médias.
x = 1
soma = 0 
while x <= 5:
    n = int(input(f"Digite o {x} termo: "))
    soma = soma + n
    x = x + 1
print(f"Sua média é igual a: {soma / 5:5.2f}")

#Exercício 5.11 - Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
#Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
x = 1
deposito = float(input("Qual será o seu depósito incial? "))
juros = float(input("Qual a taxa de juros em (%) associada a sua poupança? "))
soma = deposito 
while x <= 24:
   soma = soma + (soma * (juros / 100))
   print(f"Valor acumulado até o mês {x}: {soma:5.2f}")
   x = x + 1
print(f"Total ganho com juros: {(soma - deposito):5.2f}")

#EXercício 5.12 - Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
#Esse valor será depositado no início de cada mês, e você deve considerá-lo
#para o cálculo de juros do mês seguinte.

x = 1
deposito_inicial = float(input("Qual seré o seu depósito inicial? "))
juros = float(input("Qual a taxa de juros em (%) associada a sua poupança? "))
investimento_mensal = float(input("Depósito mensal: "))
soma = deposito_inicial
while x <= 24:
    soma = investimento_mensal + soma + (soma * (juros / 100))
    print(f"Valor acumulado até o mês {x}: {soma:5.2f}")
    x = x + 1 
print(f"Total ganho com juros foi: {(soma - (investimento_mensal * 24) - deposito_inicial):5.2f}")

#Exercício 5.13 - Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal
#que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
   
mes = 1
divida = float(input("Qual é o valor inicial de sua dívida? "))
taxa = float(input("Quanto de juros em % você pagará mensalmente? "))
parcela = float(input("Quantos reais você pagará por mês? "))
if divida * (taxa / 100) > parcela:
    print("Você nunca irá conseguir pagar a dívida! Juros mensais são superiores a parcela.")
else:
    saldo = divida
    juros_pago = 0
    while saldo > parcela: 
        juros = saldo * (taxa / 100)
        saldo = saldo + juros - parcela
        juros_pago = juros_pago + juros
        print(f"Saldo da dívida no mês {mes} é de R${saldo:6.2f}")
        mes = mes + 1
    print(f"Para pagar uma dívida de R${divida:8.2f}, a taxa {taxa:5.2f} % de juros")
    print(f"Você precisará de {mes - 1} meses, pagando um total de R${juros_pago:8.2f} de juros")
    print(f"No último mês, você teria um saldo residual de R${saldo:8.2f} a pagar")
    
#5.3 - Interrompendo a repetição = estrutura break
#Break interrompe o while independentemente do while estar sendo verdadeiro naquele momento.

s = 0 
while True:
    v = int(input("Digite um número a somar ou 0 para sair: "))
    if v == 0:
        break
    else:
        s += v
print(s)

#Exercício 5.14 - Escreva um programa que leia números inteiros do teclado. O programa deve ler
# os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade 
#de números digitados, assim como a soma e a média aritmética.

soma = 0
quantidade = 0
while True:
    numero = int(input("Digite um número para somar e calcular a média final ou 0 para sair: "))
    if numero == 0:
        break
    else:
        soma += numero
        quantidade += 1
media = (soma / quantidade)
print(f"A quantidade de números digitados foi: {quantidade}")
print(f"A soma dos números é de: {soma}")
print(f"A média dos números é de: {media}")

# Exercício 5.15 - Escreva um programa para controlar uma pequena máquina registradora. 
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. 
# Utilize a tabela de códigos a seguir para obter o preço de cada produto:

# Código Preço
# 1      0,50
# 2      1,00 
# 3      4,00
# 5      7,00
# 9      8,00

# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro “Código inválido”.


compras = 0
while True: 
    codigo = int(input("Código do produto: "))
    preco = 0
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.5
    elif codigo == 2:
        preco = 1
    elif codigo == 3:
        preco = 4
    elif codigo == 5:
        preco = 7
    elif codigo == 9:
        preco = 8
    else:
        print("Código inválido")
    if preco != 0:
        quantidade = int(input("Quantidade: "))
        compras += + (preco * quantidade)
print(f"O total gasto foi R${compras:5.2f}")

#Programa 5.1 - Contagem de cédulas:

valor = int(input("Digite o valor a pagar:")) # Valor que quero sacar no banco.
cédulas = 0 # Contador de cédulas
cédula_atual = 50 # Vamos começar a pagar com a nota de R$50
o_que_falta_p_pagar = valor # Cria uma cópia do valor original, para irmos subtraindo essa cópia sem alterar o valor original.
while True: # Inicia o loop infinito
    if cédula_atual <= o_que_falta_p_pagar:
       o_que_falta_p_pagar -= cédula_atual
       cédulas += 1
    else: # Se a cédula de 50 for maior do que o próprio valor que eu devo
        print(f"{cédulas} cédula(s) de R${cédula_atual}")
        if o_que_falta_p_pagar == 0: 
            break
        if cédula_atual == 50: # Se o valor não chegou a zero, porém ele ele é menor que a cédula de 50, use agora as cédulas de 20.
            cédula_atual = 20
        elif cédula_atual == 20:
            cédula_atual = 10
        elif cédula_atual == 10:
            cédula_atual = 5
        elif cédula_atual == 5:
            cédula_atual = 1
        cédulas = 0 #Zera o contador para começar a contar as notas do novo valor
        
# Exercício 5.16 - Execute o Programa 5.1 para os seguintes valores: 501, 745, 384, 2, 7 e 1.
# Exercício 5.17 - O que acontece se digitarmos 0 (zero) no valor a pagar?
# Resposta: O programa diz que tem que entregar 0 notas de 50 e logo depois para.
# EXercício 5.18 - Modifique o programa para também trabalhar com notas de R$ 100.

valor = float(input("Digite o valor a pagar:")) # Valor que quero sacar no banco.
cédulas = 0 # Contador de cédulas
cédula_atual = 100 # Vamos começar a pagar com a nota de R$100
o_que_falta_p_pagar = valor # Cria uma cópia do valor original, para irmos subtraindo essa cópia sem alterar o valor original.
while True: # Inicia o loop infinito
    if cédula_atual <= o_que_falta_p_pagar:
       o_que_falta_p_pagar -= cédula_atual
       cédulas += 1
    else: # Se a cédula de 50 for maior do que o próprio valor que eu devo
        print(f"{cédulas} cédula(s) de R${cédula_atual}")
        if o_que_falta_p_pagar == 0: 
            break
        if cédula_atual == 100: # Se o valor não chegou a zero, porém ele ele é menor que a cédula de 50, use agora as cédulas de 20.
            cédula_atual = 50
        elif cédula_atual == 50:
            cédula_atual = 20
        elif cédula_atual == 20:
            cédula_atual = 10
        elif cédula_atual == 10:
            cédula_atual = 5
        elif cédula_atual == 5:
            cédula_atual = 1    
        cédulas = 0 #Zera o contador para começar a contar as notas do novo valor
        
# Exercício 5.19 - Modifique o programa para aceitar valores decimais, ou
# seja, também contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50.

valor = float(input("Digite o valor a pagar:")) # Valor que quero sacar no banco.
cédulas = 0 # Contador de cédulas
cédula_atual = 100 # Vamos começar a pagar com a nota de R$100
o_que_falta_p_pagar = valor # Cria uma cópia do valor original, para irmos subtraindo essa cópia sem alterar o valor original.
while True: # Inicia o loop infinito
    if cédula_atual <= round(o_que_falta_p_pagar, 2):
       o_que_falta_p_pagar -= cédula_atual
       cédulas += 1
    else: #Se a cédula for maior do que o próprio valor que eu devo
        if cédula_atual >= 1: # Se a cédula de 50 for maior do que o próprio valor que eu devo e for maior do que 1 real:
            print(f"{cédulas} cédula(s) de R${cédula_atual}")
        else: #Se a cédula for maior do que o prórpio valor que eu devo, e menor do que 1 real, ai passa para as moedas.
            print(f"{cédulas} moeda(s) de R${cédula_atual}")
        if round(o_que_falta_p_pagar, 2) < 0.01: 
            break
        if cédula_atual == 100: # Se o valor não chegou a zero, porém ele ele é menor que a cédula de 100, use agora as cédulas de 50.
            cédula_atual = 50
        elif cédula_atual == 50:
            cédula_atual = 20
        elif cédula_atual == 20:
            cédula_atual = 10
        elif cédula_atual == 10:
            cédula_atual = 5
        elif cédula_atual == 5:
            cédula_atual = 1
        elif cédula_atual == 1:
            cédula_atual = 0.5
        elif cédula_atual == 0.5:
            cédula_atual = 0.1
        elif cédula_atual == 0.1:
            cédula_atual = 0.05
        elif cédula_atual == 0.05:
            cédula_atual = 0.02
        elif cédula_atual == 0.02:
            cédula_atual = 0.01
        cédulas = 0
        
# 5.4 = Repetições aninhadas 
# Programa 5.3 : Tabuada com repetições aninhadas;

tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        numero += 1
    tabuada += 1
    
# Programa 5.3: Tabuada sem repetições aninhadas
tabuada = 1
numero = 1
while tabuada <= 10:
    print(f"{tabuada} x {numero} = {tabuada * numero}")
    numero += 1
    if numero == 11:
        numero = 1
        tabuada += 1
        
# Exercício 5.21 - Reescreva o programa 5.1 de forma a continuar executando até que o valor seja 0.
# Utilize repetições aninhadas.



while True:
    valor = int(input("Digite o valor a pagar (ou 0 para sair)"))
    if valor == 0:
        break
    o_que_falta_p_pagar = valor
    cédula_atual = 50
    cédulas = 0
    while True:
        if cédula_atual <= o_que_falta_p_pagar:
            o_que_falta_p_pagar -= cédula_atual
            cédulas += 1
        else:
            print(f"{cédulas} cédula(s) de R${cédula_atual}")
            if o_que_falta_p_pagar == 0:
                break
            if cédula_atual == 50:
                cédula_atual = 20
            if cédula_atual == 20:
                cédula_atual = 10    
            if cédula_atual == 10:
                cédula_atual = 5
            if cédula_atual == 5:
                cédula_atual = 1
            cédulas = 0
            
# Exercício 5.22 - Escreva um programa que exiba uma lista de opções (menu): adição, 
# subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
# repita até que a opção saída seja escolhida;

while True:
    operação = input("Escolha uma dessas operações (*, /, +, -) ou (sair) para sair: ")
    if operação == "sair":
        break
    else:
        while True:
            tabuada = 1 
            numero = 1
            while tabuada <= 10:
                if operação == "*":
                    print(f"{tabuada} x {numero} = {tabuada * numero}")
                elif operação == "/":
                    print(f"{tabuada} / {numero} = {tabuada / numero}")
                elif operação == "+":
                    print(f"{tabuada} + {numero} = {tabuada + numero}")
                elif operação == "-":
                    print(f"{tabuada} - {numero} = {tabuada - numero}")
                numero += 1 
                if numero == 11:
                    numero = 1
                    tabuada += 1
            if tabuada == 11:
                    break       

# Números primos.
# 5.23 - Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 
# e depois por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número não é primo
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.


# Eu comecei o raciocínio e o lapidei com a ajuda do gemini!!
n = int(input("Teste se esse número é primo: "))
if n < 2:
    print(f"{n} não é primo.")
elif n == 2:
    print(f"{n} é primo.")
elif n % 2 == 0:
    print(f"{n} não é primo.")
else:   # Agora os números só podem ser ímpares e maiores que 2, ou seja: 3, 5, 7, 9, 11...
    divisor = 3
    e_primo = True
    while divisor < n:
        if n % divisor == 0:
            print(f"{n} não é primo.")
            e_primo = False
            break
        divisor += 2
    if e_primo:
        print(f"{n} é primo.")
        
# Agora esse será o raciocínio do livro!

n = int(input("Digite um número:"))
if n < 0:
    print("Número inválido. Digite apenas valores positivos")
if n == 0 or n == 1:
    print(f"{n} é um caso especial.")
else:
    if n == 2:
        print("2 é primo")
    elif n % 2 == 0:
        print(f"{n} não é primo, pois 2 é o único número par primo.")
    else:
        x = 3
        while x < n:
            if n % x == 0:
                break
            x = x + 2
        if x == n:
            print(f"{n} é primo")
        else:
            print(f"{n} não é primo, pois é divisível por {x}")    

# Exercício 5.24 - Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

# Essa questão beira o impossível, vou tentar entender depois denovo.
quantidade_de_primos = int(input("Digite a quantidade de números primos a gerar: "))
if quantidade_de_primos < 0:
    print("Número inválido. Digite apenas valores positivos")
else:
    if quantidade_de_primos >= 1:
        print("2")  # 2 é o único número que é primo e par ao mesmo tempo
    primos_gerados = 1  # logo é o primeiro número primo gerado
    próximo_primo = 3  # o próximo primo começa então com 3
    while primos_gerados < quantidade_de_primos: # Mantém o programa vivo até bater a meta.
        divisor = 3
        while divisor < próximo_primo: # Obviamente, o divisor tem que ser menor do que o número que queremos testar se é primo.
            # Se o resto for zero, o número é divisível
            if próximo_primo % divisor == 0: # SE achar qualquer divisão exata, ele para o código na hora.
                break
            # Incrementa o divisor
            divisor = divisor + 2
        # Quando o número é primo, ele é divisível apenas por ele mesmo
        if divisor == próximo_primo: # Se ele não caiu em nenhum break e conseguiu chegar até aí é porque ele é primo.
            print(próximo_primo)
            primos_gerados = primos_gerados + 1
        # passa para o próximo número ímpar,
        # pois os pares não são primos, salvo 2
        próximo_primo = próximo_primo + 2

# Exercício 5.25 - Escreva um programa que calcule a raiz quadrada de um número.
# Utilize o método de Newton para obter um resultado aproximado.
# Sendo n o número a obter a raiz quadrada, considere a base b=2.
# Calcule p usando a fórmula p=(b+(n/b))/2.
# Agora, calcule o quadrado de p.
#A cada passo, faça b=p e recalcule p usando a fórmula apresentada.
# Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.

n = int(input("Insira um número para cáculo da raiz quadrada: "))
b = 2
p = (b + (n / b)) / 2
while n - (p ** 2) >= 0.0001:
    b = p
    if n - (p ** 2) < 0.0001:
        print(f"A raiz quadrada de n é igual a {p ** 2}")
        
# Exercício 5.26 - Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas 
# as operações de soma e subtração para calcular o resultado.


dividendo_og = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
dividendo = dividendo_og
while dividendo >= divisor:
    dividendo -= divisor
print(f"A sobra da divisão de {dividendo_og} por {divisor} é {dividendo}")

# Exercício 5.27 - Escreva um programa que verifique se um número é palíndromo.
# Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
# Exemplos: 454, 10501


# Raciocínio: Imagine uma fábrica que produz fitas com números. Para saber se a fita é de qualidade "palíndromo", temos dois operários: o Operário I (Início) e o Operário F (Fim).

# Eles começam nas pontas opostas da fita.

# A cada passo, eles gritam o número que estão vendo. Se os números forem iguais, eles dão um passo para dentro (se aproximando no meio).

# Se em algum momento eles virem números diferentes, eles param de andar imediatamente.

# Se eles se cruzarem ou se encontrarem no meio e todos os números até ali foram iguais, a fita é aprovada!

s = input("Teste se é palíndromo: "))
i = 0 # Define que o Operário "Início" começa na primeira posição (índice 0).
f = len(s) - 1 # Mede a fita e coloca o Operário Fim na última posição válida.
# Quando você usa len a primeira posição é de índice 0 e a última é de índice len(a) - 1.
while f > i and s[i] == s[f]: # É o teste de movimento. "Enquanto os operários não se cruzarem E o que eles estão vendo for igual, continue andando".
    f -= 1
    i += 1
if s[i] == s[f]:
    print("É palíndromo.")
else:
    print("Não é palíndromo")
    

