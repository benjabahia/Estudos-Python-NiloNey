# 7. Trabalhando com strings;
# Strings são imutáveis, se quisermos alterar seus caracteres necessitamos transforma-la em lista.

s = "Hello world"
print(s[0]) # H
# Se eu falar que s[0] = "a" vai dar ERRO.

s = list("Hello world")
s[0] = "a"
print(s) # ['a', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'] - Cada caracter ocupa um índice;
s = "".join(s) # O método join az o inverso!! Transforma de volta em string.
print(s) # aello world

# 7.1 - Verificação parcial de string.
# Métodos startwsitch e endswitch.
# Servem para verificar se uma astring começa ou termina com alguns caracteres. Retornam True ou False

nome = "João da Silva"
print(nome.startswith("João")) # True
print(nome.startswith("joão")) # False
print(nome.endswith("Silva")) # True

# Métodos upper e lower, o método upper faz uma cópia da string com todas as letras maiúsculas e a lower faz o mesmo só que com minúsculas.
s = "O Rato roeu a roupa do rei de roma"
print(s.lower()) # 'o rato roeu a roupa do rei de roma'
print(s.upper()) # 'O RATO ROEU A ROUPA DO REI DE ROMA'
print(s.lower().startswith("o rato")) # True

# Outra forma de verificar se uma palavra pertence a uma string é com o operador in.
s = "Maria Amélia Souza"
print("Amélia" in s) # True
print("Souza" in s) # True
print("A" in s) # True

# Ou verificar se uma string não está contida em outra, com o operador not in.
s = "Todos os caminhos levam a Roma"
print("levam" not in s) # False
print("Caminhos" not in s) # True
print("roma" in s.lower()) # True
print("TODOS" not in s.upper()) # False

# 7.2 Contagem - O método count serve para contar as ocorreências de algo na sua string.
t = "um tigre, dois tigres, três tigres"
print(t.count("tigre")) # 3
print(t.count("tigres")) # 2
print(t.count("t")) # 4

# Esse método também funciona em listas.
L = [1, 1, 1, 2]
print(L.count(1)) # 3

# 7.3 Pesquisa de strings. O find e o rfind retornam o índice onde a substring começa, e não “o número do caractere”.
# esses métodos retornam o índice da PRIMEIRA ocorrência da substring.
s = "Alô mundo"
print(s.find("mun")) # 4. Pois a string mund inicia no índice 4. A(0) l(1) ô(2) espaço(3) m(4).
print(s.find("ok")) # -1. Pois quando não encontra a string ele retorna -1.
print(s[4:]) # mundo. Pois ele pega o caracter do quarto índice em diante até acabar a strnig.

# Se eu quiser pesquisar porém da direita para esquerda eu posso usar o método rfind.
# MAS ATENÇÃO: Isso NÃO significa que o índice muda. O índice continua começando em 0 da esquerda para a direita.
#  O que muda é apenas a direção da busca.

s = "Um dia de sol"
print(s.rfind("d")) # 7. Pois procura da direita para a esquerda.

# Caractere:  U  m     d  i  a     d  e     s  o  l
# Índice:     0  1  2  3  4  5  6  7  8  9 10 11 12

# Existem dois "d" o find procuraria da esquerda para direita, logo retornaria 3. Já o rfind retorna 7.
print(s[7:]) # de sol. Pega do índice 7 em diante até acabar a string.
print(s.find("d")) # 3. Procura da esquerda para a direita.
print(s[3:]) # dia de sol

# find(substring, início, fim)
# Ou seja, agora o find não procura mais na string inteira.
# Você pode mandar o Python procurar apenas em um trecho da string.

s = "um tigre, dois tigres, três tigres."
print(s.find("tigres")) # 15. No índice 15 inicia a substring.
print(s.rfind("tigres")) # 28. No índice 28 inicia o primeriro "tigres" que ele acha procurando da direita para a esquerda.


# Caractere:  u  m     t  i  g  r  e  ,     d  o  i  s     t  i  g  r  e  s  ,     t  r  ê  s     t  i  g  r  e  s  .
# Índice:     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36

print(s.find("tigres", 7)) # 15. Ele começa a procurar a partir do índice 7. Não muda nada.
# Então o Python IGNORA tudo antes do "e" do índice 7. Ele começa a busca daqui: , dois tigres, três tigres.

print(s.find("tigres", 30)) # -1. A partir do índice 30 não existe mais a substring completa "tigres." Logo, retorna -1.
print(s.find("tigres", 0, 10)) # -1. Quando finaliza em 10, não da tempo de aparecer nenhuma subtring "tigres". Logo, retorna -1;

# Programa 7.1: Pesquisa de todas as ocorrências
s = "um tigre, dois tigres, três tigres"
p = 0
while (p > -1):
    p = s.find("tigre", p)
    if p >= 0:
        print(f"Posição: {p}")
        p += 1

# Também existem os métodos index e rindex, no lugar de find e rfind. Porém são menos interessantes, pois eles não retornam -1 e sim dão erros.

# EXercício 7.1 - Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira
# e imprima a posição de início. 1ª string: AABBEFAATT   2ª string: BE
# Resultado: BE encontrado na posição 3 de AABBEFAATT

# Minha versão:
s1 = input("Primeira string: ")
s2 = input("Segunda string: ")
p = 0
while p > -1:
    p = s1.find(s2, p)
    if p >= 0:
        print(f"{s2} foi encontrado na posição {p} de {s1}")
        p += 1
        
# Versão do livro:
s1 = input("Primeira string: ")
s2 = input("Segunda string: ")

p = s1.find(s2)

if p >= 0:
    print(f"{s2} encontrado na posição {p} de {s1}")
else:
    print(f"{s2} não foi encontrado em {s1}")
    
# Exercício 7.2: Escreva um programa que leia duas strings e gere uma terceira com os caracteres 
# comuns às duas strings lidas. 1ª string: AAACTBF    2ª string: CBT    Resultado: CBT
# A ordem dos caracteres da string gerada não é importante, mas deve conter todas
# as letras comuns a ambas.

# Meu jeito:
s1 = list(input("Primeira string: "))
s2 = list(input("Segunda string: "))
s3 = []
i = 0
while i < len(s2):
    if s2[i] in s1:
        s3.append(s2[i])
    i += 1
    
s3 = "".join(s3) # Transformei a lista de volta em string.
if len (s3) > 0:
    print(f"Carcateres comuns: {s3}")
else:
    print("Caracteres comuns não encontrados.")

# Jeito do livro:
primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ""
for letra in primeira:
    # Se a letra está na segunda string (comum a ambas)
    # Para evitar repetidas, não deve estar na terceira.
    if letra in segunda and letra not in terceira:
        terceira += letra

if terceira == "":
    print("Caracteres comuns não encontrados.")
else:
    print(f"Caracteres em comum: {terceira}")
    
# Exercício 7.3: Escreva um programa que leia duas strings e gere uma terceira apenas com
# os caracteres que aparecem em uma delas. 1ª string: CTA    2ª string: ABC   3ª string: BT
# A ordem dos caracteres da terceira string não é importante.

# Meu jeito:
primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ""
for letra in primeira:
    if letra in segunda and letra not in terceira:
        terceira += letra
        
c3 = set(terceira) 
c1 = set(primeira)
c2 = set(segunda)
conj_não_repetidos = (c1 - c3) | (c2 - c3) # | faz a união dos conjuntos
conj_não_repetidos = "".join(conj_não_repetidos)

if len(conj_não_repetidos) > 0:
    print(f"Carcateres não repetidos: {conj_não_repetidos}")
else:
    print("As duas strings são iguais")
    
# Jeito do livro:
primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ""

for letra in primeira:
    if letra not in segunda and letra not in terceira:
        terceira += letra

# Para cada letra na segunda string
for letra in segunda:
    # Além de não estar na primeira string,
    # verifica se já não está na terceira (evitar repetições)
    if letra not in primeira and letra not in terceira:
        terceira += letra

if terceira == "":
    print("Caracteres incomuns não encontrados.")
else:
    print(f"Caracteres incomuns: {terceira}")
    
# Exercício 7.4 - Escreva um programa que leia uma string
# e imprima quantas vezes cada caractere aparece nessa string.
# String: TTAAC Resultado: T: 2x    A: 2x   C: 1x

# Meu jeito
s = input("String: ")
conj = set(s) # Criei um conjunto, pois assim não há repetições.
for letra in conj:
    print(f"{letra} apareceu {s.count(letra)} vez(es) em {s}")
    
# Jeito do livro:
sequencia = input("Digite a string: ")

contador = {}

for letra in sequencia:
    contador[letra] = contador.get(letra, 0) + 1 

for chave, valor in contador.items():
    print(f"{chave}: {valor}x")
    
# O que é .get()? O .get() é um método de dicionários. Ele serve para: pegar um valor associado a uma chave.
# dicionario.get(chave, valor_padrao) Se a chave que vc colocou não existir ele retorna o valor padrão digitado. Não da erro.
# dados = { 
    # "nome": "Ana",
    # "idade": 20}    
# dados.get("nome") --- Resultado: "Ana." 

# O que é .items()?

# O que é .items()? .items() pega TODOS os pares: chave -> valor
# Eemplo: ("b", 1)   ("a", 3)   ("n", 2)

# O for faz desempacotamento
# for chave, valor in contador.items():
# é como se cada tupla fosse separada em duas variáveis.

# Exercício 7.5 - Escreva um programa que leia duas strings e gere uma terceira
# na qual os caracteres da segunda foram retirados da primeira.
# 1ª string: AATTGGAA     2ª string: TG      3ª string: AAAA.

# Meu jeito:
s1 = input("Primeira string: ")
s2 = input("Segunda string: ")
conjs1 = set(s1)
conjs2 = set(s2)
for letra in conjs2:
    if letra in conjs2 and letra in conjs1:
        conjs1 -= conjs2
s3 = "".join(conjs1)
print(f"3° string: {s3 * (s1.count(s3) + s2.count(s3))}")

# jeito do livro:
primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ""

for letra in primeira:
    if letra not in segunda:
        terceira += letra

if terceira == "":
    print("Todos os caracteres foram removidos.")
else:
    print(f"Os caracteres {segunda} foram removidos de {primeira}, gerando: {terceira}")
    
# Exercício 7.6: Escreva um programa que leia três strings. Imprima o resultado da
# substituição na primeira, dos caracteres da segunda pelos da terceira.
# 1ª string: AATTCGAA     2ª string: TG     3ª string: AC     Resultado: AAAACCAA

# Meu jeito:
s1 = input("Primeira string: ")
s2 = input("Segunda string: ")
s3 = input("Terceira string: ")
nova = ""
d = {}

if len(s2) == len(s3):
    for i in range(len(s2)):
        d[s2[i]] = s3[i]
    for letra in s1:
        if letra in s2:
            nova += d[letra]
        else:
            nova += letra          
else:
    print("A 2º e a 3º string têm que ser do mesmo tamanho.") 

print(f"Resultado: {nova}")       

# Jeito do livro:
primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
terceira = input("Digite a terceira string: ")

if len(segunda) == len(terceira):
    resultado = ""
    for letra in primeira:
        posição = segunda.find(letra) # find devolve a posição do que vc quer achar ou -1 se não estiver presente na string.
        if posição != -1:
            resultado += terceira[posição]
        else:
            resultado += letra

    if resultado == "":
        print("Todos os caracteres foram removidos.")
    else:
        print(
            f"Os caracteres {segunda} foram substituidos por "
            f"{terceira} em {primeira}, gerando: {resultado}"
        )
else:
    print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")

# Exercício 7.7: Escreva um programa que peça ao usuário que digite uma frase e imprima quantas vogais ela contém.
# Não considere maiúsculas e minúsculas como diferentes. Exemplo: uma frase como “A casa” deve imprimir três “as”.

vogais = "aeiou"
frase = input("Digite uma frase: ")
frase_minúscula = frase.lower()
for vogal in vogais:
    ocorrência_vogal = frase_minúscula.count(vogal)
    if ocorrência_vogal > 0:
        print(f"{vogal} aparece {ocorrência_vogal} vez(es)")

# 7.4 - Posicionamento de strings.
# Método center, centraliza a string em um número de posições passado como parâmetro.

s = "tigre"
print(s.center(20)) # Vai centralizar tigre em um espaço de 20 caracteres. 20 - 5 = 15, irão ficar
# 8 caracterer para a esquerda + 5 da string + 7 caracteres em branco à direita.

# Caracter de preenchimento - Ele é utilizado ao invés de espaços vazios;
print(s.center(10, ".")) # O total precisa ter 10 espaços, 10 - 5 = 5, ficaram 2 pontos na esquerda da string e 3 pontos na direita dela.

# Método ljust - alinha a string à esquerda.
s = "tigre"
print(s.ljust(20, ".")) # Vai criar 20 espaços, e a string estará ocupando os primeiros à esquerda.

# Método rjust - alinha à direita.
print(s.rjust(20, ","))

# Dá pra fazer o mesmo com F-STRINGS.
print(f"{'tigre':^20}") # ^ é a mesma coisa que center.
print(f"{'tigre':<20}") # < é a mesma coisa que ljust.
print(f"{'tigre':>20}") # > é a mesma coisa que rjust.
print(f"{'tigre':.>20}") # Igual ao rjust porém passando o "." como parâmetro.

# 7.5 - Quebra ou separação de strings.
# Método split quebra uma string a partir de um caracter passado como parâmetro e gera uma lista com as substrings já separadas.

s = "um tigre, dois tigres, três tigres."
print(s.split(",")) # ['um tigre', 'dois tigres', 'três tigres'.]
print(s.split(" ")) # ['um', 'tigre,', 'dois', 'tigres,', 'três', 'tigres']
print(s.split()) # MESMA COISA QUE O EXEMPLO DE CIMA, qnd vc nn passa parâmetro ele usa os espaços em branco como padrão. ['um', 'tigre,', 'dois', 'tigres,', 'três', 'tigres']

# Se você quiser fazer isso, porém a string possui várias linhas de texto, utilize o método SPLITLINES;
m = "Uma linha\noutra linha\nmais uma linha"
print(m.splitlines()) # ['Uma linha', 'outra linha', 'mais uma linha']

# Exercício 7.8: Escreva um programa para exibir todas as palavras de uma frase. 
# Considere que uma palavra termina com um espaço em branco ou quando a string terminar. Exemplo: “O rato roeu a roupa” deve imprimir 5.

# Meu jeito
frase = input("Frase: ")
espaços = frase.count(" ")
print(f"A frase selecionada possui {espaços + 1} palavras.")

# Jeito do livro:
frase = input("Frase: ")
palavras = frase.split()
for palavra in palavras:
    print(palavra)
print("Número de palavras:", len(palavras))

# 7.6 - Substituição de strings. Método replace: 1º parâmetro: parte pra substituir, 2º parâmetro: o que vai entrar no lugar.
s = "um tigre, dois tigres três tigres."
print(s.replace("tigre", "gato")) # "um gato, dois gatos, três gatos".

# Opcionalmente, da pra passar um terceiro parâmetro, o qual diz quantas vezes ooorrerá a substituição.
print(s.replace("tigre", "gato", 1)) # "um gato, dois tigres, três tigres".
print(s.replace("tigre", "gato", 2)) # " um gato, dois gatos, três tigres".
print(s.replace("tigre", "gato", 3)) # "um gato, dois gatos, três tigres."

# Também podemos remover caracteres dessa forma:
print(s.replace("tigre", "")) # "um , dois s, três s"
print(s.replace(" ", "")) # "umtigre,doistigres,trêstigres".

# 7.7 - Remoção de caracteres nas EXTREMIDADES.
# Método strip remove todos os espaços em branco.
# Método lstrip remove os espaços em brancos à esquerda e o rstrip remove os espaços em branco à direita.
t = "      Olá   "
print(t.strip()) # 'Olá'
print(t.rstrip()) # '     Olá'
print(t.lstrip()) #'Olá   '

# Se você passar parâmetros nas strip, lstrip ou rstrip, ele irá remover, além dos espaços em branco, esse caracter do parâmetro.
s = "...///Olá///..."
print(s.lstrip(".")) # "//Olá///..."
print(s.strip("/")) # "...///Olá///..." FICA IGUAL, pq o strip só remove caracteres da ponta e esses "/" não estão na ponta.

# 7.8 - VAlidação por tipo de conteúdo.
