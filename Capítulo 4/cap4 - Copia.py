#4. Estruturas condicionais
# Programa 4.1: Lê dois valores e imprime qual é o maior.
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b:
 print("O primeiro valor é maior!")
if b > a:
 print("O segundo valor é maior!")

#Programa 4.2: Carro novo ou velho, dependendo da idade.
idade = int(input("Qual é a idade de seu carro?"))
if idade <= 3:
 print("O seu carro é novo")
if idade > 3:
 print("O seu carro é velho")

#Exercício 4.2: Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo
#que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5,00 por km acima de 80km/h.

velocidade = float(input("Em qual velocidade, em km/h, seu carro está andando? "))
valor = 5 * (velocidade - 80)
if velocidade > 80:
 print(f"Você foi multado em R${valor}")
 
#Exemplo de cálculo de Imposto de Renda. Programa 4.3
#O imposto é aplicado em partes!
#0% sobre os primeiros 1000 do salário, de R$1000 até R$3000 do salário é aplicado 20% e a parte do seu salário > R$3000 é aplicado 35%.
#Primeiro, o programa lê o saláriod igitado pelo usuário e armazena esse valor na variável "salário". Depois, é criada uma nova variável
#chamada base, que vai receber o mesmo valor de salário. Essa variável será utilizada como uma cópia do salário, porém que pode ser consumida
#e ter seu valor alterado com o tempo, enquanto o valor original fica inalterado.
#O programa inicia verificando se a base é maior que 3000, se sim irá aplicar somente na parte que é maior que 3000 o imposto de 35%.
#Depois disso a base é modificada para 3000 (é o que sobra quando eu já pago a parte acima de 3000) e ele verifica se isso é maior que 1000
#se sim, ele vai aplicar o imposto de 20% somente na parte que está acima de 1000. Logo, vai sobrar somente os últimos 100 reais que não sofrerão
#imposto.

salario = float(input("Digite o seu salário para cálculo de imposto: "))
base = salario
imposto = 0
if base > 3000:
 imposto = imposto + (0.35 * (base - 3000))
 base = 3000
if base > 1000:
 imposto = imposto + (0.2 * (base - 1000))
print(f"Salário: R${salario:6.2f} e Imposto de Renda a pagar: R${imposto:6.2f}")

#Teste se o salário for 4500 -> R$925
#Teste se o salário for 1500 -> R$100
 
 #Exercício 4.3 - Escreva um programa que leia três números e que imprima o maior e o menor.
a = int(input("Digite aqui o primeiro número: "))
b = int(input("Digite aqui o swgundo número: "))
c = int(input("Digite aqui o terceiro número: "))
maior = a
if b >= a and b >= c:
 maior = b
if c >= a and c >= b:
 maior = c
menor = a
if b <= a and b <= c:
 menor = b
if c <= a and c <= b:
 menor = c
print(f"O seu menor número é o {menor} e o maior número é o {maior}")
#Tem que sempre usar >= ou <=, se não, em casos de empate, dá pau.

#Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule
#o valor do aumento. Para salários superiores a R$1250, calcule um aumento de 10%.
#Para os inferiores ou iguais, 15%
salario = int(input("Qual é o seu salário? "))
if salario > 1250:
 aumento = salario * 0.1
if salario <= 1250:
 aumento = salario * 0.15
print (f"O seu aumento será de {aumento}")

#Programa 4.4: Cálculo da mensalidade de um plano de celular da operadora Tchau.
plano = input("Qual é o seu plano de celular? ")
if plano == "falopouco":
 minutos_no_plano = 100
 extra = 0.2
 preco = 50
if plano == "falomuito":
 minutos_no_plano = 500
 extra = 0.15
 preco = 99
if plano != "falopouco" and plano != "falomuito":
 print("Não conheço esse plano")
if plano == "falopouco" or plano == "falomuito":
 minutos_consumidos = int(input("Quantos minutos você consumiu? "))
 print ("Você vai pagar:")
 print (f"Preço do plano: R${preco:5.2f}")
 suplemento = 0
 if minutos_consumidos > minutos_no_plano:
  suplemento = extra * (minutos_consumidos - minutos_no_plano)
  print (f"Suplemento R${suplemento:6.2f}")
  print (f"Total R${preco + suplemento:6.2f}")

#Exercício 4.6 - Escreva um programa que pergunte a distância que um passageiro
#deseja percorrer em km. Calcule o preço da passgaem, cobrando R$0,5 por km
#para viagens até 200km, e R$0,45 para viagens mais longas.

distancia = int(input("Quantos km vocé percorrerá nessa viagem? "))
if distancia <= 200:
 preco = 0.5 * distancia
else:
 preco = 0.45 * distancia
print (f"Você irá pagar R${preco} de passagem.")


#Exercício 4.7 - Não faz sentido usar else naquele programa.

#Exercício 4.8 - Reescreva o programa 4.4 e calcule a conta da operadora Tchau usando else
# plano = input("Qual é o seu plano de celular? ")
if plano == "falopouco":
 minutos_no_plano = 100
 extra = 0.2
 preco = 50
if plano == "falomuito":
 minutos_no_plano = 500
 extra = 0.15
 preco = 99
else:
 print("Não conheço esse plano")
if plano == "falopouco" or plano == "falomuito":
 minutos_consumidos = int(input("Quantos minutos você consumiu? "))
 print ("Você vai pagar:")
 print (f"Preço do plano: R${preco:5.2f}")
 suplemento = 0
 if minutos_consumidos > minutos_no_plano:
  suplemento = extra * (minutos_consumidos - minutos_no_plano)
  print (f"Suplemento R${suplemento:6.2f}")
  print (f"Total R${preco + suplemento:6.2f}")

#4.3 Estruturas aninhadas
#Programa 4.7: Conta de telefone com três faixas de preço
minutos = int(input("Quantos minutos você utilizou esse mês: "))
if minutos < 200:
 preco = 0.2
else: #Ou seja, se os minutos forem maior que 200.
 if minutos < 400: #Ou seja maior que 200, porém menor que 400: Entre 201 e 399.
  preco = 0.18
 else:
  preco = 0.15 #Ou seja vai ser maior que 200, porém ao contrariar o if de cima, será, também, maior que 400!!
print (f"Você vai pagar R${minutos * preco:6.2f}")

#Agora irei mostrar a importância do if + else, mostrando um programa que da errado, caso só use o IF
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
 preco = 10
if categoria == 2:
 preco = 12
if categoria == 3:
 preco = 14
else:
 print(f"Categoria inválida, digite um valor entre 1 e 3")
 preco = 0
print(f"O preço do produto é R${preco:5.2f}")

#Esse código está errado, pois o else no final está relacionado somente ao if acima dele, porém para cada if é preciso o seu else! Exemplo: 
#Se eu escrever a categoria 1, ele irá analisar todos os if's, o primeiro seria verdadeiro, pois eu escolhi 1, o segundo seria falso e o terceiro falso,
#logo como o terceiro foi falso, é ai que está a bronca, pois o else do terceiro if seria ativado e a mensagem que irá aparecer será que a categoria é inválida.

#Para corrigir isso, cada if te-m que estar associado ao seu else:
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
 preco = 10
else:
 if categoria == 2:
  preco = 12
 else:
  if categoria == 3:
   preco = 14
  else:
   if categoria == 4:
    preco = 16
   else:
    preco = 0
    print(f"Categoria inválida, digite um valor entre 1 e 4")
print(f"O preço do produto é R${preco:5.2f}")
#Assim está certo, porém, o que ocorre é que devido ao escesso de aninhamento, o código se desloca excessivamente para direita, logo é preciso agrupar
#else + if em uma coisa só e é assim que nasce o ELIF.

#Jeito 100% correto agora:
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
 preco = 10
elif categoria == 2:
 preco = 12
elif categoria == 3:
 preco = 14
elif categoria == 4:
 preco = 15
else:
 preco = 0
 print(f"Categoria inválida, digite um valor entre 1 e 4")
print(f"O preço do produto é R${preco:5.2f}")

#Agora, evitamos o deslocamento excessivo para a direita

#Programa 4.10: Planos da Tchau com Elif utilizando controle de fluxo com True e False (explicação na pág 129).
valido = True
plano = input("Qual é o seu plano de celular? ")
if plano == "falopouco":
 minutos_no_plano = 100
 extra = 0.2
 preco = 50
elif plano == "falomuito":
 minutos_no_plano = 500
 extra = 0.15
 preco = 99
else:
 valido = False
if not valido:
 print (f"Erro: Não conheço esse {plano}")
else:
 minutos_consumidos = int(input("Quantos minutos você consumiu? "))
 print ("Você vai pagar:")
 print (f"Preço do plano R${preco}")
 suplemento = 0 
 if minutos_consumidos > minutos_no_plano:
  suplemento = extra * (minutos_consumidos - minutos_no_plano)
  print (f"Suplemento R${suplemento}")
  print (f"Total R${suplemento + preco}")
#Exercício 4.10 - Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você pode calcular soma (+), subtração (-)
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

valido = True
primeiro_numero = float(input("Digite seu primeiro número: "))
segundo_numero = float(input("Digite seu segundo número: "))
operacao = input("Qual operação básica você deseja aplicar nesses 2 números? ")
if operacao == "soma":
 resultado = primeiro_numero + segundo_numero
elif operacao == "subtração":
 opcao_subtracao = int(input("Você deseja o primeiro número subtraído do segundo (1), ou o segundo número subtraído do primeiro (2)? Digite 1 ou 2 para assinalar sua opção. "))
 if opcao_subtracao == 1:
  resultado = primeiro_numero - segundo_numero
 elif opcao_subtracao == 2:
  resultado = segundo_numero - primeiro_numero
 else:
  valido = False
  if not valido:
   print("Digite apenas  1 ou 2 para prosseguir com seu cálculo")
elif operacao == "multiplicação":
 resultado = primeiro_numero * segundo_numero
elif operacao == "divisão":
 opcao_divisao = int(input("Voce deseja dividir o primeiro número pelo segundo (1), ou o segundo pelo primeiro (2)? Digite 1 ou 2 para assinalar sua opção. "))
 if opcao_divisao == 1:
  resultado = primeiro_numero / segundo_numero
 elif opcao_divisao == 2:
  resultado = segundo_numero / primeiro_numero
 else:
  valido = False
  if not valido:
   print ("Digite apenas 1 ou 2 para prosseguir com seu cálculo")
else: 
 valido = False
 if not valido:
  print("digite uma operação válida")
if valido:
 print(f"Seu resultado é igual a {resultado}")

 #EXercício 4.11 - Escreva um programa para aprovar o empréstio bancário para compra de uma casa. o porgrama deve perguntar o valor da casa
 #o salário e a quantidade de anos para pagar. O valor d prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo
 #o valor da casa a comprar dividido pelo número de meses a pagar.

valor = float(input("Qual o valor da casa que você quer comprar? "))
salario = float(input("Qual é o seu salário? "))
anos = float(input("Você deseja pagar essa casa durante quantos anos? "))
emprestimo_mensal = valor / (anos * 12)
if emprestimo_mensal <= 0.3 * salario:
 print(f"O empréstimo mensal fornecido pelo banco será de R$ {emprestimo_mensal}")
elif emprestimo_mensal > 0.3 * salario:
 print("O empréstimo não poderá ser efetivado, pois seu valor excede 30% do seu salário")

 #Exercício 4.12 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de
#Instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

valido = True
consumo = float(input("Quantos kWh você consumiu esse mês? "))
instalacao = input("Qual o tipo de instalação? Residencial, Comercial ou Industrial? ")
if consumo <= 500 and instalacao == "Residencial":
 preco = 0.4
elif consumo > 500 and instalacao == "Residencial":
 preco = 0.65
elif consumo <= 1000 and instalacao == "Comercial":
 preco = 0.55
elif consumo > 1000 and instalacao == "Comercial":
 preco = 0.6
elif consumo <= 5000 and instalacao == "Industrial":
 preco = 0.55
elif consumo > 5000 and instalacao == "Industrial":
 preco = 0.6
else:
 valido = False
if not valido:
 print ("Você provavelmente digitou algo errado, cheque se escreveu o nome da instalação com letra maiúscula!")
valor_total = consumo * preco
if valido:
 print(f"O seu gasto foi de R${valor_total}")

 #Inversão de condições 4.5, exercício 4.13 - No programa a seguir, inverta as linhas do if e else, negando a condição.
 #Adicione as linhas necessárias para fazê-lo funcionar em Python.
#if a > b:
    #print("a é maior que b")
#else:
    #print("b é maior que a")
a = int(input("a: "))
b = int(input("b: "))
if a <= b:
 print("b é maior do que a")
else:
 print ("a é maior do que b")
 
 #Reescreva o programa a seguir com if-elif-else. Adicione as linhas necessárias para fazê-lo funcionar em Python.
#if a < 10:
    #print("a é menor que 10")
#if a >= 10 and a < 20:
    #print("a é maior que 10 e menor que 20")
#if a >= 20:
    #print("a é maior que 20")

a = int(input("a: "))
if a < 10:
 print("a é menor do que 10")
elif 20 > a >= 10:
 print("a é maior ou igual a 10 e menor do que 20")
else:
 print("a é maior do que 20")

 #Exercício 4.15 - Reescreva o programa a seguir com if-elif-else
 
#hora = int(input("Digite a hora atual:"))
#if hora < 12:
    #print("Bom dia!")
#if hora >=12 and hora <=18:
    #print("Boa tarde!")
#if hora >=18:
    #print("Boa noite!")

hora = int(input("Digite a hora atual: "))
if hora < 12:
 print("Bom dia!")
elif hora <= 18:
 print("Boa tarde!")
else:
 print("Boa noite!")


#Exercício 4.16 - Corrija o problema a seguir:

#média = input("Digite sua média:")
#if média < 4:
    #print("Infelizmente você reprovou")
#if média < 7:
    #print("Você ficou de recuperação")
#if média > 7:
    #print("Você passou de ano")

media = input("Digite aqui a sua média: ")
if media < 4:
 print("Infelizmente você reprovou")
elif media < 7:
 print("Você ficou de recuperação")
else:
 print("Você passou de ano")