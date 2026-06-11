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

EMPRESA = "Unidos Venceremos Ltda"
def imprime_cabeçalho():
    print(EMPRESA)
    print("-" * len(EMPRESA))
    
imprime_cabeçalho()

# Esse caso de utilização de variável global está correto, pois o nome da empresa é algo fixo
# Informações fixas que poderão ser utilizadas em diversas funções ao decorrer do meu código
# devem ser declaradas de forma global.

# agora irei mostrar um exemplo claro de um código com excelente encapsulamento, isto é 
# carregada consigo tudo aquilo que ela precisa para trabalhar. Não precisa de informações externas a ela.

def imprime_cabecalho(nome_empresa):
    print(nome_empresa)
    print("-" * len(nome_empresa))
    
# imediatamente entendo: "Essa função precisa receber o nome da empresa." Ela não depende de nenhuma variável secreta fora dela.
# a função é independente do resto do programa.

EMPRESA = "Loja Azul"

def imprime_cabecalho():
    print(EMPRESA)

def gera_relatorio():
    print("Relatório da", EMPRESA)

def salva_backup():
    print("Backup de", EMPRESA)
    
# Você tem três funções usando a mesma variável global. Mas agora alguém faz isto:
# EMPRESA = "Loja Verde", De repente:

# imprime_cabecalho mudou
# gera_relatorio mudou
# salva_backup mudou

# Todas as funções foram afetadas. Mesmo sem modificar nenhuma delas. O comportamento das funções depende de algo externo.
# Ou seja se em um programa que possua 50 funções, eu encontrar um erro, tipo: o nome da empresa aparece errado.
# Eu não consigo saber qual função que possui o erro, pois todas elas utilizam a mesma variável global.

EMPRESA = "Loja Azul"

def imprime_cabecalho():
    print("Empresa:", EMPRESA)

def gera_relatorio():
    print("Gerando relatório da", EMPRESA)

def trocar_empresa():
    global EMPRESA # "Quando eu falar EMPRESA nessa função, não quero criar uma variável local. Quero mexer na variável global."
    EMPRESA = "Loja Verde"

trocar_empresa()

imprime_cabecalho()
gera_relatorio()

# Vai imprimir: Empresa: Loja Verde, Gerando relatório da Loja Verde. Pois o valor da variável GLOBAL foi alterado.

# Exemplo do livro:

a = 5

def muda_e_imprime():
    a = 7
    print(f"a dentro da função: {a}") # 7
print(f"a antes de mudar: {a}") # 5

muda_e_imprime()
print(f"a depois de mudar: {a}") # 5. Impirme a global novamente. A local já foi destruída quando a função encerrou.

# Exemplo da instrução global do livro: 

a = 5

def muda_e_imprime():
    global a # Python, preste atenção. Quando eu falar "a" aqui dentro, não quero criar uma variável local. Quero usar a variável global.
    a = 7 # NÃO CRIOU VARIÁVEL LOCAL, agora ele só alterou o valor da variável global.
    print(f"a dentro da função: {a}") # 7. Procura no local e não acha. Pega o valor global que acabou de ser alterado.
    
print(f"a antes de mudar: {a}") # 5. Esse daqui é a primeira coisa que imprime, porque vem antes de eu chamar a função;
muda_e_imprime()
print(f"a depois de mudar: {a}") # 7. Imprime a variável global após a modificação.

# 8.2 - Funções recursivas: A "escadinha".

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(4))


# Primeira coisa que acontece quando a função é chamado com o valor 4 passado:

# LOCAL 1
# n → 4

# Depois a função é executada e quando chega nessa linha: 
# return 4 * fatorial(3). O python pensa Eu sei quanto vale 4. Mas ainda não sei quanto vale fatorial(3). 
# Então não posso multiplicar ainda. Por isso ele interrompe temporariamente a execução atual e vai descobrir quanto vale: fatorial(3)

# Agora nasce uma segunda execução da função.

# LOCAL 1
# n → 4

# ----------------

# LOCAL 2
# n → 3

# Agora a segunda execução também chega em: return 3 * fatorial(2)
# Mas o python pensa: "Ainda não sei quanto vale fatorial(2)." E começa a terceira execução.

# Na quarta execução, quando o n = 1. A linha if n == 0 or n == 1: da True.
# E ele retorna 1. Quando fatorial(1) dá 1. A execução acima dela, que no caso é (fatorial(2)
# já recebe seu valor, automaticamente a execução acima dela, que é fatorial(3) é resolivida e assim por diante.
# O núemro 24 finalmente é retornado e impresso na tela.
 
# Resumo:
# Uma função recursiva não é uma única função "girando em círculo".
# O que realmente existe são várias execuções independentes da mesma
# função, cada uma com seu próprio escopo local, empilhadas umas sobre as outras.

# Programa 8.7: Função recursiva de Fibonacci.
# Sequeência de fibonacci é a seq de números que é igual a soma de seus últimos 2 antecessores:
# 0, 1, 1, 2, 3, 5. Aqui nessa seq, estão os números de fibonacci 0 até o fibonacci 5. F(0) -> F(5).

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(5))

# Para calcular F5, preciso saber quem é F4 e F3, mas para calcular F4 preciso saber quem é F3 e F2.
# MAs para calcular F3 preciso saber quem é F2 e F1. Mas para calcular F2 preciso saber quem e F1 e F0.

# Quando vou calcular o F1, vejo que o if n <= 1: True, logo retorno 1. F1 = 1
# Então só falta calcular o F0 para saber quem é o F2. O F0 retorna 0 pq cai no if também
# Logo, F2 = 1 + 0. 
# F3 = F2 + F1 e eu já sei os valores disso, logo: F3 = 1 + 1. E assim chegamos até descobrir quanto valor F5, o qual é printado na tela.

# Se desenharmos apenas a estrutura das chamadas para fibonacci(5), temos: 

# fibonacci(5)
# ├─ fibonacci(4)
# │  ├─ fibonacci(3)
# │  │  ├─ fibonacci(2)
# │  │  │  ├─ fibonacci(1)
# │  │  │  └─ fibonacci(0)
# │  │  └─ fibonacci(1)
# │  └─ fibonacci(2)
# │     ├─ fibonacci(1)
# │     └─ fibonacci(0)
# │
# └─ fibonacci(3)
#    ├─ fibonacci(2)
#    │  ├─ fibonacci(1)
#    │  └─ fibonacci(0)
#    └─ fibonacci(1)

# Observe algo curioso. fibonacci(3) foi calculada mais de uma vez. Isso vai ser importante na parte de eficiência.

# Exercício 8.7: Defina uma função recursiva que calcule o maior
# divisor comum (M.D.C.) entre dois números a e b, em que a > b.

# A fórmula que o livro mostra diz que o MDC de dois números é igual ao MDC do menor número com o resto da divisão de ambos.
# MDC(a, b) = MDC(b, a % b). Caso a > b
# Ele também falo que o MDC(a, 0) = a.

# Exemplo: MDC(48, 18) = MDC(18, 12)
# Porém, MDC(18, 12) = MDC(12, 6) = MDC(6, 0) = 6. Logo MDC(48, 18) = 6.

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

def mdc (a, b):
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    if menor == 0:
        return maior
    else:
        return mdc (menor, maior % menor)

print(f"MDC({num1}, {num2}): {mdc(num1, num2)}") 

# Exercício 8.8: Usando a função mdc definida no exercício anterior, defina uma função
# para calcular o menor múltiplo comum (M.M.C.) entre dois números.
# mmc(a, b) = |a × b| / mdc(a, b)
# Em que |a × b| pode ser escrito em Python como: abs(a * b).

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

def mdc (a, b):
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    if menor == 0:
        return maior
    else:
        return mdc (menor, maior % menor)
 
def mmc (a, b):
    return abs(a * b) / mdc (a, b)

print(f"MMC({num1}, {num2}): {mmc(num1, num2)}") 

# Exercício 8.9: Rastreie o Programa 8.6 e compare o seu resultado com o apresentado

# O programa calcula o fatorial de 4
# Pelas mensagens de saída impressas e pelo rastreamento do programa,
# podemos concluir que o fatorial de 4 é calculado com chamadas recursivas
# na linha: fat = n * fatorial(n-1)
#
# Como a chamada do fatorial precede a impressão da linha Fatorial de,
# podemos visualizar a sequencia em forma de pilha, onde o cálculo é feito de fora
# para dentro: Cálculo do fatorial de 4, 3 , 2 e 1
# para então prosseguir na linha seguinte, que faz a impressão dos resultados:
# fatorial de 1,2,3,4

# Exercício 8.10: Reescreva a função para cálculo da sequência de Fibonacci, sem utilizar recursão.

# Minha forma:
fib = int(input("Número de fibonacci: "))
i = 2
L = [1, 1]
rodando = True


while rodando:
    if fib > 0:
        if fib == 1:
            print(f"A sequência de fibnacci até o termo {fib} é: 1")
            rodando = False
        elif fib == 2:
            print(f"A sequência de fibnacci até o termo {fib} é: {L}")
            rodando = False
        else:
            prox = L[i - 1] + L[i - 2]
            L.append(prox)
            i += 1
            if i == fib:
                break
    else:
        print("O número precisa ser positivo.")
        rodando = False

if rodando:
    print(f"A sequência de fibonacci até o termo {fib} é: {L}")
    
# Forma do livro:

def fibonacci(n): # Na memória global: fibonacci ─────► [objeto função]
    atual = 0 # número atual da sequência
    próximo = 1 # próximo número da sequência
    while n > 0:
        atual, próximo = próximo, próximo + atual # O Python primeiro calcula tudo à direita. atual, atual + prox = 1, 1 + 0 = (1, 1). É como se fosse guardasse como TEMP = (1,1)
        # Depois atribui tudo à esquerda. p = TEMP[0] = 1. s = TEMP[1] = 1.
        n -= 1
    return atual


for x in range(10): # Para cada x em [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"fibonacci({x}) = {fibonacci(x)}")
    
# Essa questão tráz o interessantíssimo conceito de desempacotamento.

# Quando escrevemos a, b = 10, 20, o Python primeiro avalia todo o lado
# direito da atribuição, formando internamente uma estrutura temporária equivalente a
# (10, 20), e somente depois distribui seus elementos para as variáveis do lado esquerdo.    

# Esse mecanismo é amplamente utilizado para atribuições múltiplas, troca de
# valores (a, b = b, a), recebimento de múltiplos retornos de funções 
# (q, r = dividir(10, 3))

# O que garante que operações como p, s = s, s + p, usadas no algoritmo de Fibonacci,
# funcionem corretamente sem a necessidade de variáveis temporárias.

# Uma boa forma de visualizar o desempacotamento é imaginar que o Python
# rimeiro coloca todos os valores do lado direito dentro de uma "caixa temporária" e,
# somente depois, distribui cada item dessa caixa para as variáveis do lado esquerdo.

# 8.3: Validação.

# Programa 8.9: Exemplo de validação sem usar uma função.

while True:
    v = int(input("Digite um valor entre 0 e 5: "))

    if v < 0 or v > 5:
        print("Valor inválido.")
    else:
        break

print("Valor aceito:", v)
    
# Porque seria útil transformar isso em função?
# Imagine um programa grande. Você precisa pedir: idade entre 0 e 120, nota entre 0 e mês entre 1 e 12.
# Iriam precisar de vários laços while e uma combinação grande de breaks. Você repetiria a mesma lógica vaaaaaaarias vezes.


# Podemos transformar isso em uma função que receba a pergunta e os valores de
# máximo e mínimo.        

# Programa 8.10: Validação de inteiro usando função:

def faixa_int(pergunta, mínimo, máximo): # faixa_int ───► [função]
    while True:
        v = int(input(pergunta))
        if v < mínimo or v > máximo:
            print(f"Valor inválido. Digite um valor entre {mínimo} e {máximo}")
        else:
            return v

idade = faixa_int("Digite sua idade: ", 0, 120) # Segunda linha que ele lê, agora sim a função é chamda.

print("Idade digitada:", idade)

# Sem função, você acabaria copiando aquele mesmo bloco de código várias vezes
# A função é como uma máquina especializada: você coloca uma pergunta, um mínimo e um máximo,
# e ela devolve um valor validado. Agora você pode reutilizar esse comportamento quantas vezes quiser sem reescrever o código.
# Com a função, a lógica existe em um único lugar. Você altera uma vez e todos os pontos do programa passam a usar a nova versão.

# Exercício 8.11: Escreva uma função para validar uma variável string. Essa função
# recebe como parâmetro a string, o número mínimo e máximo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo, e falso, caso contrário.

# Minha forma:
def f(string, mínimo, máximo):
    while True:
        v = string
        if len(v) < mínimo or len(v) > máximo:
            return False
        return True
    
print(f("Ornitorrinco", 5, 17))
print(f("Olá", 4, 10))
print(f("Sabão", 3, 4))

# Forma do livro:
def f(s, mín, máx):
    tamanho = len(s)
    return mín <= tamanho <= máx # Esses opersdores de ==, >, <= etc são operadores de COMPARAÇÃO, os quais automaticamente já retornam True ou False.


print(f("", 1, 5))
print(f("ABC", 2, 5))
print(f("ABCEFG", 3, 5))
print(f("ABCEFG", 1, 10))

# Exercício 8.12: Escreva uma função que receba uma string e uma lista.
# A função deve comparar a string passada com os elementos
# da lista, também passada como parâmetro.
# Retorne verdadeiro se a string for encontrada dentro da lista, e
# falso, caso contrário.

def f(s, lista):
    return s in lista # O operador in retorna True ou False automaticamente.


L = ["AB", "CD", "EF", "FG"]

print(f("AB", L))
print(f("CD", L))
print(f("EF", L))
print(f("FG", L))
print(f("XYZ", L))

# Exercício 8.13: Escreva uma função que receba uma string com as opções
# válidas a aceitar (cada opção é uma letra). Converta as opções
# válidas para letras minúsculas.
# Utilize input para ler uma opção, converter o valor para letras
# minúsculas e verificar se a opção é válida. Em caso de opção
# inválida, a função deve pedir ao usuário que digite novamente outra opção.

def f(string):
    string = string.lower()
    while True:
        letra = input("Digite uma letra: ").lower()
        if len(letra) != 1:
            print("Digite apenas uma letra.")
        elif letra in string:
            print(f"A letra {letra} está presente na string.")
            break  
        else:
            print(f"A letra {letra} não está presente na string\nVocê terá que tentar novamente!\n")

f("AEiou")
f("bOlA")

# 8.4 - Parâmetros opcionais:

def barra():
    print("*" * 40)
    
# Essa função, a qual não apresente parâmetros:
# sempre faz exatamente a mesma coisa: imprime 40 asteriscos. 
# Não importa a situação, o resultado será sempre igual.
# Se em algum momento você quiser imprimir 20 asteriscos ou 50 traços (-),
# precisará alterar a própria função.

# É aí que entram os parâmetros, para flexibilizar o código. Porém às vezes tem um valor 
# que é muito usado na maiora das situações e ficaria chato, ficar pedindo pra passar esse valor
# óbvio o tempo todo como parâmetro. Por isso existem parâmetros opcionais:

def barra(n=40, caractere="*"):
    return (caractere * n)

print(barra()) # barra(40, "*"), é o "padrão de fábrica".
print(barra(10))
print(barra(15, "-"))

# Se ninguém me informar um valor para n, use 40. Se ninguém me informar um
# valor para caractere, use *."
# A diferença é que agora ela já possui valores prontos guardados como padrão.

# Programa 8.11: Função soma com parâmetros obrigatórios e opcionais;

def soma(a, b, imprime=False):
    s = a + b
    if imprime:
        print(s)
    return s 

soma(2, 3) # Aqui eu retornei 5, porém não o imprimi, pois o valor padrão diz que não é p imprimir;
soma(2, 3, True) # Aqui eu retorno e printo 5, pois passei o parametro opcinal para printar.

# Nesse exemplo a e b são obrigatórios e imprime é opcinal.
# O opcional SEMPRE terá que ser o último na fila, veja uma fução escrita de forma INVÁLIDA.

def soma (imprime=True, a, b):
    s = a + b
    if imprime:
        print(s)
    return s 

# Da mensagem de erro!!!

# 8.5 - Nomeando parâmetros.
# Programa 8.2: Função retângulo com parâmetros obrigatórios e opcionais.
def retângulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for i in range (altura):
        print(linha)

retângulo(3, 4) # Aqui, vai na ordem certinha
retângulo(largura=3, altura=4) # Mesma coisa, mas não precisava já que já ta na ordem certa.
retângulo(altura=4, largura=3) # Mesma coisa, mas agora eu quis inverter a ordem da chamda dos parãmetros.
retângulo(caractere="-", altura=4, largura=3) # Também funciona, posso colocar em qualquer ordem que eu quiser.

# Se especificar um parâmetro, é obrigatório especificar todos.

# Isso aqui é errado: retângulo(largura=3, 4)
# Isso aqui também: retângulo(largura=3, altura=4, "-")

# 8.6: Funções como parâmetros;
# Programa 8.13:

def soma(a, b):
    return a + b
def subtração(a, b):
    return a - b
def imprime(a, b, foper):
    print(foper(a, b))

imprime(5, 4, soma)
imprime(10, 1, subtração)

# TEMPO 1: Inicialização do Programa
# ┌──────────────────────────────────────────────────────────┐
# │ MEMÓRIA GLOBAL                                           │
# │                                                          │
# │  soma       ───► [Objeto Função: calcula a + b]          │
# │  subtração  ───► [Objeto Função: calcula a - b]          │
# │  imprime    ───► [Objeto Função: gerencia a impressão]   │ 
# │

# Passo 2: Chamada de imprime(5, 4, soma)
# TEMPO 2: Execução de 'imprime'
# ┌──────────────────────────────────────────────────────────┐
# │ MEMÓRIA GLOBAL                                           │
# │  soma       ───► [Objeto Função: calcula a + b] ◄────┐   │
# │  subtração  ───► [Objeto Função: calcula a - b]      │   │
# │  imprime    ───► [Objeto Função: ... ]               │   │
# └──────────────────────────────────────────────────────║───┘
#                                                        ║
#     ┌──────────────────────────────────────────────────▼───┐
#     │ ESCOPO LOCAL: imprime                                │
#     │                                                      │
#     │  a ───► 5                                            │
#     │  b ───► 4                                            │
#     │  foper ──────────────────────────────────────────────┘
#     └──────────────────────────────────────────────────────┘

# Passo 3: O cálculo interno foper(a, b)
# Dentro de imprime, o interpretador avalia foper(a, b)
# Como foper aponta para a função de soma, o Python cria um segundo escopo local,
# temporário, especificamente para a função soma. Os valores de a (5) e b (4) são passados para lá.

# TEMPO 3: Execução de 'soma' (Escopo Aninhado)
# ┌──────────────────────────────────────────────────────────┐
# │ MEMÓRIA GLOBAL                                           │
# │  soma       ───► [Objeto Função: calcula a + b] ◄────┐   │
# └──────────────────────────────────────────────────────║───┘
#                                                        ║
#     ┌──────────────────────────────────────────────────║───┐
#     │ ESCOPO LOCAL: imprime                            ║   │
#     │  a ───► 5                                        ║   │
#     │  b ───► 4                                        ║   │
#     │  foper ──────────────────────────────────────────┘   │
#     └──────────────────────────────────────────────────────┘
#         │      │
#         │      └──────────────┐
#         ▼                     ▼
#     ┌──────────────────────────────┐
#     │   ESCOPO LOCAL: soma                           │
#     │  a ───► 5                    │
#     │  b ───► 4                    │
#     │  Operação: 5 + 4 = 9         │
#     └──────────────────────────────┘

# A função soma retorna o valor 9. Após isso a linha print(foper(a, b)), fica = print(9).


# Programa 8.14: Configuração de funções com funcões.

def imprime_lista(L, fimpressão, fcondição):
    for e in L:
        if fcondição(e):
            fimpressão(e)


def imprime_elemento(e):
    print(f"Valor: {e}")


def épar(x):
    return x % 2 == 0


def éimpar(x):
    return not épar(x)


L = [1, 7, 9, 2, 11, 0]
imprime_lista(L, imprime_elemento, épar)
imprime_lista(L, imprime_elemento, éimpar)

# 8.7 - Empacotamento e desempacotamento de parâmetros.

def soma(a, b):
    print(a + b)

L = [2, 3]
soma(*L) # O * antes vem pra dizer que tu quer desempacotar a lista;
# Nesse caso, após desempacotar o L[0] será atribuído a "a" e L[1] a "b".
# Evitando a construção do tipo: soma(L[0], L[1])

def barra(n=10, c="*"): # Parâmetros que se eu não passar, ele já vai utilizar esses como padrão.
    print(c * n)

L = [[5, "-"], [10, "*"], [5], [6, "."]]
for e in L:
    barra(*e) # o "e" vai assumir o valor de [5, "-"]. Ao desempacotar, L[0] = 5, será o parâmetro n
# e o L[1] = "-" ocupa o parâmetro "c".

# 8.8 - Desempacotamento de parâmetros
# Programa 8.15: Função soma com número indeterminado de parâmetros.

def soma(*args): # "Não importa quantos argumentos o usuário envie, pegue todos eles,
# coloque dentro de uma tupla e atribua essa tupla ao nome args".
    s = 0
    for x in args: # Na primeira volta do laço, o Python extrai o primeiro elemento da tupla, que é 1, e cria a variável temporária x apontando para ele. Na segunda volta: x --> 3.
        s += x
    return s 

soma(1, 3) # O interpretador olha para os valores 1 e 3 que você enviou. Ele percebe o *args na definição da função e imediatamente cria uma tupla na memória contendo esses dois números.
# Em seguida, ele aponta a variável local args para essa tupla.
#  args -----> (1, 3)

soma(2) 
soma(5, 6, 7, 8)
soma()

# Programa 8.16: Função impreme_maior com número indeterminado de parâmetros.

def imprime_maior(mensagem, *números): # 
    maior = None
    for e in números:
        if maior is None or maior < e:
            maior = e
    print(mensagem, maior)
        
imprime_maior("Maior:", 5, 4, 3, 1)
imprime_maior("Maior:", *[1, 7, 9]) # Esse asterisco na chamada é uma instrução de desempacotamento
# Ele ordena ao interpretador: "Abra esta lista e espalhe os elementos dela como se eu tivesse digitado cada um separadamente".
# a chamada imprime_maior("Maior:", *[1, 7, 9]) exatamente em: imprime_maior("Maior:", 1, 7, 9)
# A lista original deixa de existir para a função; agora restam apenas quatro argumentos independentes.

# Quando esses quatro argumentos chegam à definição def imprime_maior(mensagem, *números):
# O asterisco na definição captura todos os argumentos restantes (1, 7 e 9) e os empacota novamente, mas desta vez em uma tupla.
# Agora entramos no laço for e in números:. O interpretador vai iterar sobre a tupla (1, 7, 9)
# Primeiro e = 1, depois e = 7... etc.

# 8.9 - Funções lambda.

a = lambda x: x * 2
print(a(3)) 

# # Escopo Global:
# a ---> [Objeto Função Lambda (parâmetro: x)]

#  Escopo Local da Lambda:
# x ---> 3

# Agora, o interpretador executa o corpo da lambda: x * 2
# Ele busca o valor de x (3) e realiza a multiplicação = 6.

# Como a função lambda possui o RETORNO AUTOMÁTICO (NÃO PRECISA DA INSTRUÇÃO RETURN) o Python pega esse valor 6
# encerra imediatamente o escopo local da lambda (apagando a variável x da memória)
# e envia o 6 de volta para o escopo global, substituindo a expressão a(3).
# A linha agora se torna efetivamente print(6)

aumento = lambda a, b: (a * b / 100)
print(aumento(100, 5)) # o primeiro valor (100) será mapeado para o primeiro parâmetro (a), e o segundo valor (5) será mapeado para o segundo parâmetro (b).

# Escopo Global:
# aumento ---> [Objeto Função Lambda (parâmetros: a, b)]

# Escopo Local da Lambda:
# a -------> 100
# b -------> 5

# O processador executa 100 * 5 / 100 = 5. Por causa do RETORNO IPLÍCITO, ele pega esse valor 5 e ao excluir o escolo local envia o 5 para o escopo global.
# Então aumento(100, 5) = 5. Logo: print(5).

