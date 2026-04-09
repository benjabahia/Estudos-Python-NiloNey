#3.2 Vriáveis numéricas
#Passando um número da base binária para a base decimal
a = 0b11
print (a)
#Passando um número decimal em binário
b = bin(25)
print (b)

#Variáveis de tipo lógico
a = 1 
b = 5
c = 2
d = 1

#agora vou fazer algumas afirmações para testar os operadores, esses operadores já estão relacionados as variáveis do tipo lógico,
#logo se eu fizer uma afirmação usando o operador ==, o python SEMPRE imprimirá um resultado True ou False.
resultado = (a == b)
print (resultado)
resultado2 = (a == d)
print (resultado2)
resultado3 = (c<= b)
print (resultado3)
resultado4 = (d != a)
print (resultado4)

#Exemplo do dia-a-dia;
nota = 8
média = 7
aprovado = (nota >= média)
print(aprovado)
#Nesse caso eu atribui os valores de 8 e 7 para nota e média e basicamenteeu fiz uma afirmação que a nota era maior que a média
#e essa afirmação foi feita utilizando o operadores de tipo lógico, ou seja o python analisou a afirmação, eimprimiu o valor lógico de True
#a palavra aprovado, pois a afirmação estava correta.

#Combinações de operadores lógicos seguem uma lista de prioridades regidas pelo mnemonico "NAO"
#1) Not, 2)And, 3)Or
#EXemplo: TRue or False and (not true) = true or (false and false) = true or false = true


#Exercício 3.6 - Escreva uma expressão que será utilizada para decidir se  um aluno ofoi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores ou iguais a 7
#Considere que o aluno cursa apenas três matérias.
matéria1 = 6
matéria2 = 7
matéria3 = 8
aprovado = (matéria1 >= 7 and matéria2 >= 7 and matéria3 >= 7)
print (aprovado)

#3.4 variáveis string
# a funcão len -> lenght, determina a qtd de carcteres da string (sequência de caracteres)
print (len("O rato roeu a roupa do rei de roma"))
print (len(""))

#Para acessar um caracter específico da minha string eu uso colchetes, a primeira letra tá np índice 0, a segunda no índice 1 e assim por diante.
a = "EU SOU LINDO"
print (a[3])
print (a[0])

#Operações com strings
#3.4.1.1 Concatenação = soma
s = "ABC"
print (s + "C")
print (s + 4 * "D")
print("X" + 10 * "-" + "X")
print (s + "x4 = " + 4 * s)

#3.4.1.2 Composição
#Marcador de posição = %d
#Operados = %
idade = 20
print ("João tem %d anos" % idade)

#Variações do operadoe %
idade = 22
print("%d" %idade) #22
print("%03d" %idade) #022
print("%3d" %idade) #_22
print("%-3d" %idade) #22_

#%f -> Relação com números decimais
print ("%f" %7) #Por padrão ele escreve com 6 casas decimais -> 7.000000
print ("%5f" %7) #Acontece a mesma coisa, pq eu disse pra ele que a largura mínima era de 5 caracteres da string, mas de td jeito ele já tinha 8
print ("%5.2f" %7) #_7.00 -> Pq eu disse que tinha q ter no mínima 5, porém só 2 casas decimais, ai ficam 4 caracteres (junto com o ponto) ai ele
#coloca um espaço na frente para completar.
print ("%10.5f" %7) #___7.00000 -> Teve que xompletar com 3 espaços em branco na frente.

#Conclusão:
#%s -> string
#%d -> número inteiro
#%f -> número decimal (f vem de floating)

#Agora juntando => João tem 22 anos e apenas R$51,34 no bolso.
print ("%s tem %d anos e apenas RS %5.2f no bolso" % ("João", 22, 51.34))
#A primeira aspas cobre tudo, porque é um único objeto de texto.
#Somente João possui aspas pq ele é uma string em formato de texto, os números não precisam.

#Formatted string -> mais utilizada hoje em dia
nome = "João"
idade = 22
grana = 51.34
print ("{} tem {} anos e apenas R${} no bolso." .format (nome, idade, grana))
#alterações das formatted strings
print ("{:12} tem {:3} anos e apenas R${:5.2f} no bolso" .format (nome, idade, grana))
print ("{:5} tem {:03} anos e apenas R${:5.2f} no bolso" .format (nome, idade, grana))
#como mudar a ordem dos parÂmetros inseridos na string
print ("{2} {1} {2} {0}" .format ("x", "y", "z"))

#Forma mais atual ainda: F-string
#Aqui, a variável é escrita diretamente na string, fica bem mais compacto e visual
print (f"{nome} tem {idade} anos e apenas R${grana} no bolso")
print (f"{nome:12} tem {idade:5} anos e apenas R${grana:5.2f} no bolso")

#3.4.1.3 Fatiamento de strings
s = "ABCDEFGHI"
print (s[0:2]) #AB -> inclui o caracter dposição 0 e 1 (não inclui o 2)
print (s[2:6]) #CDEF -> inclui o caracter de posição 2 ao 5 (não inclui o 6)
print (s[2:]) #CDEFGHI -> Ele começa a contar do caracter de índice 2 e vai até o final
print (s[:4]) #ABCD -> Vai do caracter de posição 0 até o de posição 4, mas sem incluir o de posição 4.
print (s[:]) #ABCDEFGHI -> Não limitei nada.
print (s[0:-2]) #ABCDEFG -> Vai do início até o segundo ( de trás para frente pq é negativo) e não inclui ele.
print (s[-5:7]) #EFG -> Vai do 5 da direita para a esquerda (pq é negativo) e vai até o 7 mas sem incluir ele.
print (s[::-1]) #IHGFEDCBA -> Inverte a sring toda
print (s[::2]) #Ele vai passando de 2 em 2

#3.5 Sequências e tempo
#Mudanças no valor de duas variáveis no tempo.

dívida = 0 
compra = 100 
dívida = dívida + compra
compra = 200
dívida = dívida + compra
compra = 300
dívida = dívida + compra
compra = 0
print (dívida)

#Rastreamento 3.6
#Entrada de dados
x = input("Digite um número: ")
print (x)

#O que acontece aqui é o seguinte, eu primeiro pedi para que ele mostrasse a mensagem Digite o número para mim
#e que pausasse o programa e esperasse eu responder com qualquer número lá no terminal, e quando eu tivesse digitado
#que ele exprima esse número na tela.
#Então primeiro ele mostrou essa msg na tela, depois eu digitei o número 5 e ele guardou essa informação e depois ele mostrou na tela por causa do print.]

nome = input("Digite seu nome: ")
print(f"Você digitou {nome}")
print(f"Olá {nome}!")

#EU peço para ele me perguntou meu nome lá no terminal e assim que eu respondo e dou enter, ele imprime na tela dizendo qual foi o nome que eu digitei
#e me dando olá!]

#3.7.1 Conversão de entrada de dados
#O input sempre devolve valores do tipo string (texto), e para transforma-la em números temos que usar a função int para inteirou ou float para decimais
#E porque é importante transforar em número? Porque para fazer operações matemáticas, não funciona com string.

anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bônus = anos * valor_por_ano
print(f"Bônus de R$ {bônus: 5.2f}")

#Exercícios de entrada de dados
#3.7) FAça um programa que peça dois números inteiros e imprima sua soma na tela.
a = int(input("Digite seu primeiro número: "))
b = int(input("Digite seu segundo número: "))
soma_dos_dois_números = (a+b)
print(f"A soma de seus dois números resultou em {soma_dos_dois_números: }")

#3.8) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
a = int(input("Digite um valor em metros: "))
b = a * 1000
print (f"O seu valor convertido em milímetros é {b}")

#3.9) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
a = int(input("Insira uma quantidade de dias "))
b = int(input("Insira uma quantidade de horas "))
c = int(input("Insira uma quantidade de minutos "))
d = int(input("Insira uma quantidade de segundos "))
soma_em_segundos = (a * 24 * 60 * 60 + b * 60 * 60 + c * 60 + d)
print( f"A soma de todo o tempo que você digitou em segundo é {soma_em_segundos}")

#3.10) FAça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário
salário = float(input("Digite aqui o seu salário: "))
aumento = float(input("Digite aqui quantos '%' de aumento será aplicado no seu salário: "))
print(f"seu salário aumentou em R${salário * aumento/100}")
print(f"seu novo salário é de R${salário * (1 + aumento/100)}")

#3.11) Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
a = float(input("Insira aqui o preço dessa mercadoria: "))
b = float(input("Quanto de desconto você quer dar a essa mercadoria em '%'?"))
preço_a_se_pagar = a * (1 - b/100)
print(f"Você pagará R${preço_a_se_pagar}, pois seu desconto foi de {b}%")

#3.12) Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância percorrer e a velocidade média esperada para a viagem.
distancia = float(input("Qual é a distância em KM até o seu destino? "))
velocidade = float(input("Quantos km/h em média você manterá nessa viagem? "))
tempo = distancia / velocidade 
print (f"Sua viagem demorará {tempo} horas")

#3.13) Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é: F = 9 * C/5 + 32
celcius = float(input("Digite aqui uma temperatura em celcius: "))
fahrenheit = 9 * celcius / 5 + 32
print (f"Aqui está a sua temperatura na escala °F: {fahrenheit}")

#3.14) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade
#de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
a = float(input("Quantos km você percorreu com o carro no total dos dias? "))
b = float(input("Quantos dias você permaneceu com o carro? "))
preco_diaria = 60 * b
preco_por_km = 0.15 * a 
print (f"Você irá pagar R${preco_diaria + preco_por_km}")

#3.15 Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e 
#a quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule qunatos dias de vida
#um fumante perderá. Exiba o total em dias.

a = int(input("Quantos cigarros você fuma em média por dia? "))
b = float(input("Há quantos anos você fuma? "))
perda_de_vida = a * b * 365 / 144
print (f"Você, até agora, já perdeu {perda_de_vida: 5.2f} dias de vida")




