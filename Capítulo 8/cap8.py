# 8 - Funções.

# 1) Bloco: Definição da função em si.
def soma (a, b): # Define uma função chamada "soma"
    print(a + b) # A minha função realiza essa ação. "a" e "b" são os parâmetros.

# 2) Bloco: Chamando a função.     
soma(2, 9)  # Chama a função passando os argumentos 2 e 9
soma(7, 8) 
soma(10, 15)

# Instrução return:

# Pensa assim: uma função é como uma máquina fechada.

# Você coloca algo nela → ela processa → e no final ela pode:

# devolver um resultado para fora (return)
# ou não devolver nada.

# O ponto mais importante é:

# O print() NÃO consegue enxergar o que acontece dentro da função.
# Ele só consegue enxergar o que a função DEVOLVE para fora.



def cubo(num): # Defino uma função chamada cubo que receberá argumentos para preencherem o parâmetro denominado de num.
    num ** 3 # Essa é a ação da minha função, ela pega o argumento que eu vou chamar e eleva ele ao cubo.
    
print(cubo(3)) # Retorna none. Pois a gente atribuiu um valor para a função, porém não pedimos para esse valor ser retornado.

# Até aqui o 27 EXISTE. MAS ELE ESTÁ PRESO DENTRO DA FUNÇÃO. O print não enxerga dentro dela! Só enxerga o que ela retorna para fora.
# Retornar = jogar o valor para fora da função, podendo ser usado por pint, variáveis, contas etc.

def cubo(num): # Defino uma função chamada cubo que receberá argumentos para preencherem o parâmetro denominado de num.
    return num ** 3 # Essa é a ação da minha função. Dps q concluir a ação ela RETORNA esse valor
print(cubo(3)) # A função retorna 27, e o print exibe esse valor na tela.

# 1. Executar cubo(3)
# 2. Pegar o valor retornado
# 3. Colocar esse valor no print

# Função que retorna V ou F, dependendo se é par ou ímpar.
def épar(x):
    return x % 2 == 0 # O operador "==" tem efeito de comparação. Pergunta se o resto de x por 2 é igual a 0. 
# Tem como resposta dessa comparação True ou False, e essa resposta é retornada para fora da função pra ser usada depois no print.

print(épar(2)) # True, porque é par.
print(épar(3)) # False, porque é ímpar.
print(épar(10)) # True, porque é par.

# Função que retorna a palavra se é par ou ímpar.
def épar(x):
    return x % 2 == 0

def par_ou_impar(x):
    if épar(x): # O python primeiro executa a função épar, caso ela for True, ela entra no bloco e retorna "par".
        return "par"
    else: # Após executar a função épar, caso ela for False, ele roda esse bloco, retornando "ímpar".
        return "ímpar"
   
print(par_ou_impar(4))
print(par_ou_impar(5))

# Segunda forma:
while True:
    num = int(input("Números (0 para sair): "))
    if num == 0:
        break
    else:
       def épar(x):
           return x % 2 == 0
       i = épar(num)
       if i:
           print(f"{num} é par")
       else:
           print(f"{num} é ímpar") 
           
# Exercício 8.1: Escreva uma função que retorne o maior de dois números.

a = int(input("Número 1: "))
b = int(input("Número 2: "))

def f(a, b):
    if a > b:
        return a
    else:
        return b 

print(f"O maior número é: {f(a, b)}")

# Exercício 8.2: Escreva uma função que receba dois números e retorne True 
# se o primeiro número for múltiplo do segundo.

a = int(input("Número 1: "))
b = int(input("Número 2: "))

def f(mult, num):
    return mult % num == 0

print(f(a, b))

# Exercício 8.3: Escreva uma função que receba o lado de um quadrado e retorne sua área (A = lado²).
a = int(input("Lado do quadrado: "))

def área(m):
    return m * m

print(f"A área do quadrado de lado {a} é igual a {área(a)}")

# Exercício 8.4: Escreva uma função que receba a base e a altura de um triângulo e retorne sua área. 
base = int(input("Base do triângulo: "))
altura = int(input("Altura do triângulo: "))

def área(m, n):
    return (m * n / 2)

print(f"A área do triângulo de base {base} e altura {altura} é de {área(base, altura)}")

# Programa 8.1: Pesquisa em uma lista.

def pesquise (lista, valor):
    for x, e in enumerate (lista):
        if e == valor:
            return x # O return marca o fim de execução de uma função, quando isso é executado o for para imediatamente.
    return None # O Python só chega aqui se o FOR terminar inteiro e NÃO encontrar o valor que está sendo porcurado.
L = [10, 20, 25, 30]

print(pesquise(L, 25))
print(pesquise(L, 27))

# Exemplo cálculo de média:

L = [10, 20, 25, 30]

def soma (L): # Ela recebe uma lista no parâmetro L. (Funções podem receber literalmente qualquer coisa: conjuntos, dicionários etc.)
    total = 0
    for e in L:
        total += e
    return total # A função soma retorna total, ou seja: joga 85 pra fora da função.
def média (L):
    return soma (L) / len (L) # Aqui acontece MUITA coisa ao mesmo tempo.
# O Python resolve primeiro: soma(L). Então ele chama a função soma e já vimos que: soma(L) devolve 85.
# Depois disso ele calcula o comprimento de L e vê que é igual a 4. Após isso a expressão virou simplismente 85/4
# Depois disso ele ainda RETORNA 21.25 para fora da função média.

print(média(L))

# Programa 8.2: O que NÃO fazer!!!

def soma(L):
    total = 0
    x = 0
    while x < 5:
        total += L[x]
        x += 1
    return total

L = [1, 7, 2, 9, 15]
print(soma(L))
print(soma([7, 9, 12, 3, 100, 20, 4])) # Não printou o valor correto! Porque? Porque esse exemplo só funciona
# para listas com 5 elementos, por causa do while x < 5. Isso não é uma função genérica e ela funciona em 
# pouquíssimos casos. A intenção é fazer uma função genérica, a qual poderá ser reutilizada outras vezes em outros programas.

# Programa 8.3: Cálculo de fatorial:
num = int(input("Número: "))

def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat

print(f"O fatorial de {num} é {fatorial(num)}")


# Programa 8.4: Outra forma de calcular o fatorial
num = int(input("Número: "))


def fatorial(n):
    fat = 1
    x = 1
    while x <= n:
        fat *= x
        x += 1
    return fat

print(f"O fatorial de {num} é {fatorial(num)}")

# Exercício 8.5: Reescreva a função do Programa 8.1 de forma a utilizar
# os métodos de pesquisa em lista, vistos no Capítulo 7.

def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor) 
    return None


L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))

# index() é um método das listas que serve para
# descobrir em qual posição um elemento está. Ela percorre a lista do começo ao fim:
# 25 == 10 ? False. 25 == 20 ?. False 25 == 25 ?. True. Retorna p índice em que achou, ou seja = 2.
# O 2 foi retornado para fora da função. Se o valor não existir na lista, ocorre um erro
# Por isso é obrigatório para usar o index, antes colocar a condição do valor in lista!
# Primeiro verifica se o valor existe e só depois chama index().
# Não precisa colocar "else" antes do return None, pois o return encerra a função imediatamente
# sem nem olhar para as linhas subsequentes.

# Exercício 8.6: Reescreva o Programa 8.2 de forma a utilizar for em vez de while.

def soma(lista):
    total = 0
    for i in lista:
        total += i
    return total

L = [1, 7, 2, 9, 15]
print(soma(L))
print(soma([7, 9, 12, 3, 100, 20, 4]))

# Python tem funções para calcular a soma, o máximo e o mínimo de uma lista.

L = [5, 7, 8]
print(sum(L)) # 20
print(max(L)) # 8
print(min(L)) # 5

# 8.1 - Variáveis locais e globais. 

# uando seu programa começa a rodar, o Python cria um ambiente principal.
# Tudo que você escreve fora de funções é colocado nesse ambiente principal, chamado escopo global.
# Por exemplo:
# x = 10
# y = 20
# Após executar essas linhas, o Python possui um ambiente que podemos imaginar assim:
# GLOBAL: x → 10, y → 20. Pense que existe um nome chamado x que aponta para um objeto cujo valor é 10.

# Agora imagine que o Python encontra uma função:
def teste():
    print("Olá")

# Nesse momento ele não executa o código da função. 
# Ele apenas cria um objeto função e o registra no ambiente global:
# GLOBAL: x → 10, y → 20, teste → função.
# A parte interessante começa quando você chama a função:

teste()

# esse instante o Python cria uma sala privada
# temporária exclusivamente para aquela execução da função. Esse ambiente é chamado de escopo local.

# x → 10
# y → 20
# teste → função

# ----------------

# LOCAL DA FUNÇÃO teste

# (vazio)

# A função começa a executar dentro desse ambiente local. Se a função criar uma variável:

def teste():
    z = 50
    
# o resultado será: LOCAL: z → 50. Observe que z não foi criada no ambiente global. 
# Ela foi criada somente dentro da sala privada da função.

x = 10

def teste():
    print(x)

teste()

# O Python segue uma espécie de protocolo mental. Primeiro ele procura o nome no ambiente local atual.
# Se encontrar, usa aquele valor. Se não encontrar, sobe para o ambiente global e procura lá.
# Se também não encontrar no global, gera erro. Nesse caso, ele nn achou no ambiente local, porém encontrou no global.

x = 10

def teste():
    x = 20
    print(x)

teste()

# Muita gente imagina que a função modificou o x global. Na verdade ela não fez isso.
# GLOBAL: x → 10
# LOCAL: x → 20
# São duas variáveis distintas que apenas possuem o mesmo nome. Nesse caso ele vai achar a variável local primeiro e imprimi-la: 20.
# Depois que a função termina, acontece algo extremamente importante:o ambiente local é destruído.
# O computador fica apenas com o ambiente global, por isso que:

x = 10

def teste():
    x = 20

teste()

print(x) 

# mostra 10 e não 20. O x local existiu apenas durante a execução da função.
# Quando a função terminou, ele deixou de existir.

# Resumo: Uma função não executa dentro do mesmo ambiente do programa
# principal. Ela ganha seu próprio ambiente temporário. Quando
# precisa de uma variável, procura primeiro nesse ambiente local. Se
# não encontrar, procura no global. Quando a função termina, o ambiente local é destruído.

# Exemplo do livro: 