#Exercício 4.10
#Meu jeito: Tem que digitar a operação
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
 print(f"Sua resposta será {resultado}")

#jeito do livro, bem mais fácil
valido = True
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
operacao = input("digite a operação a realizar (+, -, * ou /): ")
if operacao == "+":
 resultado = a + b
elif operacao == "-":
  opcao_subtracao = int(input("Você deseja o primeiro número subtraído do segundo (1), ou o segundo número subtraído do primeiro (2)? Digite 1 ou 2 para assinalar sua opção. "))
  if opcao_subtracao == 1:
   resultado = a - b
  elif opcao_subtracao == 2:
   resultado = b - a
  else:
   valido = False
  if not valido:
   print("Digite apenas  1 ou 2 para prosseguir com seu cálculo")
elif operacao == "*":
 resultado = a * b
elif operacao == "/":
 opcao_divisao = int(input("Voce deseja dividir o primeiro número pelo segundo (1), ou o segundo pelo primeiro (2)? Digite 1 ou 2 para assinalar sua opção. "))
 if opcao_divisao == 1:
  resultado = a / b
 elif opcao_divisao == 2:
  resultado = b / a
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

