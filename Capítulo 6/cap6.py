# 6. - Listas, dicionários, tuplas e conjuntos.
# Para compor umam lista, utiliza-se os colchetes []
# Os índices de uma lista de tamanho n, variam de 0 até n - 1.

z = [15, 8, 9]
print(z[0]) # Mostra o número 15, pois está no índice 0.

# Podemos alterar o conteúdo de uma lista dessa forma
z[0] = 7
print(z) # Irá printar: [7, 8, 9] -> Substitui o primeiro valor.

# Programa 6.1: Cálculo de média.
notas = [6, 7, 5, 8, 9]
soma = 0
índice = 0
while índice < 5:
    soma += notas[índice]
    índice += 1
print(f"Média: {soma / índice:.2f} ")

# Programa 6.2: Cálculo de média com notas digitadas
notas = [0, 0, 0, 0, 0]
soma = 0
índice = 0
while índice < 5:
    notas[índice] = float(input(f"Nota {índice + 1}: "))
    soma += notas[índice]
    índice += 1
índice = 0
while índice < 5:
    print(f"Nota {índice + 1}: {notas[índice]:.2f}")
    índice += 1
print(f"Média: {soma / índice:.2f}")

# Exercício 6.1 - Modifique o Programa 6.2 para ler 7 notas em vez de 5.
notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
índice = 0
while índice < 7:
    notas[índice] = 1
    soma += notas[índice]
    índice += 1
índice = 0
while índice < 7:
    print(f"Nota {índice + 1}: {notas[índice]:.2f}")
    índice += 1
print(f"Média: {soma / índice:.2f}")


# Programa 6.3: Apresentação de números
números = [0, 0, 0, 0, 0]
contador = 0
while contador < 5:
    números[contador] = int(input(f"Número {contador + 1}: "))
    contador += 1
while True:
    escolhido = int(input("Que posição você quer imprimir ou 0 para sair: "))
    if escolhido == 0:
        break
    else:
        print(f"Número de posição {escolhido}: {números[escolhido - 1]}")

# 6.2 - Cópia e fatiamento de listas
L = [1, 2, 3]
V = L
L[0] = 8
V[1] = 7
print(L)
print(V)

# Nesse caso, eles printam a mesma coisa!! QUando eu fiz essa cópia, eu basicamente
# chamei uma mesma lista, só que com 2 nomes diferentes: V e L.
# Tem como criar cópias independentes, assim, podendo altera-las de forma diferentes? SIM

# Cópia independente -> [:]

L = [1, 2, 3, 4, 5]
V = L[:]
V[0] = 6
L[0] = 7
print(V)
print(L)

# AGora sim! Eles printam coisas distintas, pois eu realizei uma cópia independente.

# Fatiamento de listas funcionam da mesma forma que as de string.
L = [1, 2, 3, 4 ,5 ,6, 7]
print(L[0:5]) # Vai da posição 0 até a 4 (a quinta posição é EXCLUÍDA) -> [1, 2, 3, 4, 5,]
print(L[:5]) # Mostra os cinco primeiros elementos da lista -> [1, 2, 3, 4, 5]
print(L[:-1]) # Todos menos o último -> [1, 2, 3, 4, 5, 6]
print(L[2:4]) # Vai da posição 2 até a posição 3 (o 4 é EXCLUÍDO) -> [3, 4]
print(L[3:]) # Só a partir da posição 3 -> [4, 5, 6, 7]
print(L[-1]) # O último elemento -> [7]
print(L[-2]) # O penúltimo elemento -> [6]

#6.3 - Tamanho de listas -> Função len -> o valor retornado é igual ao número de caracteres da lista.
L = [12, 9, 5]
print(len(L)) # Retorna 3
V = []
print(len(V)) # Retorna 0

# Programa 6.4: Repetição com tamanho fixo da lista
L = [1, 2, 3, 4]
índice = 0
while índice < 4:
    print(L[índice])
    índice += 1
    
# Programa 6.5: Repetição com tamanho da lista usando len
L = [1, 2, 3, 4]
índice = 0
while índice < len(L):
    print(L[índice])
    índice += 1
    
# 6.4 - Adição de elementos:
# Método (propriedade interna e exclusiva de determinado objeto) append:
# è um método exclusivo das listas, adiciona um iten no final da lista;

L = []
L.append("A")
print(L)
L.append("B")
print(L)
print(len(L))

# resumo dos prints:
# [A]
# [A, B]
# 2

# Programa 6.6: Adição de elementos à lista:
L = []
while True:
    n = int(input("Digite um número para a lista ou 0 para sair: "))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1
    
# Dá para fazer esse programa também utilizando a adição de listas.
# Ao utilizar o operador "+" você pode somar coisas iguais, ou seja lista + lista.

L = []
L += [1]
print(L)
L += [2]
print(L)
L += [3]
print(L)

# [1]
# [1, 2]
# [1, 2, 3]

# Diferença entre append e extend.
# o extend é basicamente um append porém que você pode adicionar mais de 1 elementos de uma vez.
# O extend funciona com ([]), já o append somente com ()

L = ["a"]
L.append("b")
print(L) # ['a', 'b']
L.extend(["c"]) # Quando a lista só tem 1 elemento, vai funcionar igual ao append.
print(L) # ['a'. 'b', 'c']
L.append(["d", "e"])
print(L) # ['a', 'b', 'c', ['d', 'e']] -> Criei uma sublista, na qual ['d', 'e'] é considerado SOMENTE 1 ELEMENTO, pois foi utilizado o append.
L.extend(["f", "g", "h"])
print(L) # ['a', 'b', 'c', ['d' 'e'], 'f', 'g', 'h'] -> Nesse caso adicionou os 3 itens separadamente ao final da lista;

# Exercício 6.2 - Faça um programa que leia duas listas e que gere uma trerceira com os elementos das duas primeiras.

# Meu jeito:
L1 = []
L2 = []
while True:
    a = int(input("Adicone um termo para a primeira lista (ou 0 para sair): "))
    if a == 0:
        break
    L1.append(a)
while True:
    b = int(input("Adicone um termo para a segunda lista (ou 0 para sair): "))
    if b == 0:
        break
    L2.append(b)
L3 = L1 + L2
print(L3)

# Jeito do livro:

L1 = []
L2 = []
while True:
    a = int(input("Adicone um termo para a primeira lista (ou 0 para sair): "))
    if a == 0:
        break
    L1.append(a)
while True:
    b = int(input("Adicone um termo para a segunda lista (ou 0 para sair): "))
    if b == 0:
        break
    L2.append(b)
L3 = L1[:] # Copia os elementos da primeira lista para a terceira lista.
L3.extend(L2)
x = 1
while x <= len(L3):
    print(f"Índice {x}: {L3[x - 1]}")
    x += 1
    
# Exercício 6.3 - Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

# Meu jeito + ajuda grande do gemini;
L1 = []
L2 = []
while True:
    a = int(input("Termos da primeira lista (0 para sair): "))
    if a == 0:
        break      
    L1.append(a)
while True:
    b = int(input("Termos da segunda lista (0 para sair): "))
    if b == 0:
        break
    L2.append(b)
L3 = L1[:]
y = 0
repetidos = []
while y < len(L2):
    x = 0
    encontrou_repetido = False
    while x < len(L1):
        if L2[y] == L1[x]:
            repetidos.append(L2[y])
            encontrou_repetido = True
            break
        x += 1
    if encontrou_repetido == False:
        L3.append(L2[y])
    y += 1
print(f"Lista sem repetidos: {L3}")
print(f"Itens repetidos: {repetidos}")

# Jeito do livro:

primeira = []
segunda = []
while True:
    e = int(input("Digite um valor para a primeira lista (0 para sair): "))
    if e == 0:
        break
    primeira.append(e)
while True:
    e = int(input("Digite um valor para a segunda lista (0 para sair): "))
    if e == 0:
        break
    segunda.append(e)
terceira = []

# Aqui vamos criar uma outra lista, com os elementos da primeira
# e da segunda. Existem várias formas de resolver este exercício.
# Nesta solução, vamos pesquisar os valores a inserir na terceira
# lista. Se não existirem, adicionaremos à terceira. Caso contrário,
# não copiaremos, evitando assim os repetidos.

duas_listas = primeira[:]
duas_listas.extend(segunda)
x = 0
while x < len(duas_listas):
    y = 0
    while y < len(terceira):
        if duas_listas[x] == terceira[y]:
            break
        y += 1
    if y == len(terceira)
    terceira.append(duas_listas[x])
    x += 1
x = 0
while x < len(terceira):
    print(f"{x}: {terceira[x]}")
    x += 1

# 6.5 - Remoção de elementos da lista:
# Instrução del:
L = ["a", "b", "c"]
del L[1]
print(L) # ['a', 'c']
del L[0]
print(L) # ['c']

# List, range e pop;
# A função pop faz você retirar um elemento da fila e ao mesmo tempo obter o elemento retirado.
# Ou seja, o método pop permite vc ARMAZENAR o valor retirado dentro de uma variável e o exclui da fila. 

# Range cria uma sequeência de números, porém só a lógica deles, não os armazena de fato.
# List pega a lógica criada por range e de fato cria uma lista com esses números.


# Programa 6.7 - Simulação de uma fila de banco:
último = 10
fila = list(range(1, último + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}.")
    print("Digite 'F' para adicionar um cliente ao fim da fila.")
    print("Ou 'A' para realizar um atendimento. 'S' para sair.")
    operação = input("Operação (F, A ou S): ")
    if operação == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")    
    elif operação == "F":
        último += 1
        fila.append(último)
    elif operação == "S":
        break
    else:
        print("Operação inválida, clique apenas 'F', 'A' ou 'S'.")

# Exercício 6.4 - O que acontece quando não verificamos se a lista está 
# vazia antes de chamarmos o método pop?
# Vai dar erro, pois eu estaria pedindo para retirar e exibir o valor retirado, 
# Sendo que a lista não possui nenhu valor sequer, ela está vazia.

# Exercício 6.5 - Altere o Programa 6.7 de forma a poder trabalhar
# com vários comandos digitados de uma só vez.
# Atualmente, apenas um comando pode ser inserido por vez.
# ltere-o de forma a considerar operação como uma string.
# Exemplo: FFFAAAS significaria três chegadas de novos clientes,
# três atendimentos e, finalmente, a saída do programa.

x = 0  
último = 10
fila = list(range(1, último + 1))
rondando = True
while rodando:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}.")
    operação = input("Operação (F, A ou S), \nPode ser em formato de texto (ex: FFAAS): ")
    lista_de_termos = list(operação) # # Transforma "FFA" em ['F', 'F', 'A']
    i = 0
    while i < len(lista_de_termos):
        comando = lista_de_termos[i]
        if comando == "A":
            if len(fila) > 0:
               atendido = fila.pop(0)
               print(f"Cliente {atendido} atendido")
            else:
               print("Fila vazia! Ninguém para atender.")
        elif comando == "F":
            último += 1
            fila.append(último)
            print(f"Cliente {último} chegou.")   
        elif comando == "S":
            print("Saindo do programa...")
            rodando = False
            break
        else:
           print("Operação inválida, clique apenas 'F', 'A' ou 'S'.")
        i += 1     

    

# Exercício 6.6 - Modifique o programa para trabalhar com duas filas.
# Para facilitar seu trabalho, considere o comando A para atendimento da fila 1;
# e B, para atendimento da fila 2. 
# O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.

# Forma longa: 

x = 0  
último1 = 10
fila1 = list(range(1, último1 + 1))
último2 = 10
fila2 = list(range(1, último2 + 1))
rodando = True
while rodando:
    print(f"\nExistem {len(fila1)} clientes na fila 1\ne {len(fila2)} clientes na fila 2.")
    print(f"Fila 1 atual: {fila1}.")
    print(f"Fila 2 atual: {fila2}.")
    operação1 = input("Operação (F, A ou S) para a fila 1, \nPode ser em formato de texto (ex: FFAAS): ")
    operação2 = input("Operação (G, B ou S) para a fila 2, \nPode ser em formato de texto (ex: GGBBS): ")
    lista_de_termos1 = list(operação1) # # Transforma "FFA" em ['F', 'F', 'A']
    lista_de_termos2 = list(operação2)
    i = 0
    while i < len(lista_de_termos1):
        comando1 = lista_de_termos1[i]
        if comando1 == "A":
            if len(fila1) > 0:
               atendido1 = fila1.pop(0)
               print(f"Cliente {atendido1} atendido na fila 1")
            else:
               print("Fila vazia! Ninguém para atender.")
        elif comando1 == "F":
            último1 += 1
            fila1.append(último1)
            print(f"Cliente {último1} chegou na fila 1.")   
        elif comando1 == "S":
            print("Saindo do programa...") 
        i += 1   
    i = 0
    while i < len(lista_de_termos2):
        comando2 = lista_de_termos2[i]
        if comando2 == "B":
            if len(fila2) > 0:
               atendido2 = fila2.pop(0)
               print(f"Cliente {atendido2} atendido na fila 2")
            else:
               print("Fila vazia! Ninguém para atender.")
        elif comando2 == "G":
            último2 += 1
            fila2.append(último2)
            print(f"Cliente {último2} chegou na fila 2.")   
        elif comando2 == "S":
            print("Saindo do programa...")
            rodando = False
            break
        i += 1   
        
# Forma ideal:
último = 0
fila1 = []
fila2 = []
while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} na fila 2.")
    print("Fila 1 atual:", fila1)
    print("Fila 2 autal:", fila2)
    print("Digite F para adicionar um cliente ao fim da fila 1 (ou G para fila 2),")
    print("ou A para realizar o atendimento a fila 1 (ou B para fila 2")
    print("S para sair.")
    operação = input("Operação (F, G, A, B ou S):")
    x = 0
    sair = False
    while x < len(operação):
        # Aqui vamos usar fila como referência a fila 1
        # ou a fila 2, dependendo da operação.
        if operação[x] == "A" or operação[x] == "F":
            fila = fila1
        else:
            fila = fila2
        if operação[x] == "A" or operação[x] == "B":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[x] == "F" or operação[x] == "G":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == "S":
            sair = True
            break
        else:
            print(
                f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!"
            )
        x = x + 1
    if sair:
        break
         
# 6 .7 - uso de listas como pilhas(analogia de pilhas de pratos)
# O elemento a ser retiado é sempre o último (o de cima) e o adicionado, também é adicionado no final.

# Programa 6.8 - Pilhas de pratos:
prato = 5
pilha = list(range(1, prato + 1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha.")
    print(f"Pilha atual: {pilha}")
    print(f"Digite E para empilhar um novo prato\nou D para desempilhar. S para sair.")
    operação = input("Operação(D, E ou S)")
    if operação == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(len(pilha) - 1)    
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia! Nada para lavar;")
    elif operação == "E":
        prato += 1
        pilha.append(prato)
    elif operação == "S":
        break
    else:
        print("Operação inválida. Digite apenas D, E ou S.")

# Exercício 6.7 = Faça um programa que leia uma expressão com parênteses. 
# Usando pilhas, verifique se os parênteses foram abertos e fechados
# a ordem correta. Exemplo: (()) OK
# ()()(()()) OK
# ()) Erro
# Você pode adicionar elementos à pilha sempre que encontrar abre
# parênteses e desempilhá-la a cada fecha parênteses. Ao desempilhar,
# verifique se o topo da pilha é um abre parênteses. Se a expressão
# estiver correta, sua pilha estará vazia no final.


rodando = True
while rodando:
    entrada = input("Digite uma sequência de parênteses: ")
    
    lista_de_leitura = list(entrada)
    pilha = []
    i = 0
    erro_encontrado = False
    
    
    while i < len(lista_de_leitura):
        item = lista_de_leitura[i]
        
        if item == "(":
            pilha.append("(")
            print("Achei um '(', guardei na pilha.")
            
        elif item == ")":
            if len(pilha) > 0:
                pilha.pop()
                print("AChei um ')', encontrei o par e removi da pilha.")
            else:
                print("Erro! Você fechou um parênteses antes de abri-lo.")  
                rodando = False
                erro_encontrado = True
                break 
        i += 1
    
    
    if erro_encontrado == False:
        if len(pilha) == 0:
            print("Resultado OK! Tudo certo.")
        else:
            print("Erro! Sobraram parênteses abertos na pilha")
            rodando = False

# 6.8 - Pesquisa:
# Podemos pesquisar se um elemento está ou não em uma lista, verificando
# do primeiro ao último elemento se o valor procurado estiver presente.

# Programa 6.9: Pesquisa sequencial

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
achou = False
x = 0
while x < len(L):
    if L[x] == p:
        achou = True
        break
    x += 1
if achou:
    print(f"{p} acho na posição {x + 1}")
else:
    print(f"{p} não foi encontrado")

# Exercício 6.8: Modifique o primeiro exemplo (Programa 6.9) de forma a
# alizar a mesma tarefa, mas sem utilizar a variável achou. 
# Dica: observe a condição de saída do while.

# Minha forma:
x = 0
L = [15, 7, 27, 39]
rodando = True
while rodando:
    p = int(input("Digite o valor a procurar: "))
    while x < len(L):
        if L[x] == p:
            rodando = False
            break
        x += 1
if not rodando:
    print(f"{p} achado na posição {x + 1}")
else:
    print(f"{p} não foi encontrado")

# Forma qye o livro utiliza para diferenciar a quebra do while!
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
x = 0 
while x < len(L):
    if L[x] == p:
        break
    x += 1  
    
# Agora vem a dúvida, como saber se o loop parou porque i ficou maior que o len
# ou seja ele não achou o numero igual, ou se o loop parou porque achou alguem igual, 
# logo, o i seria menor que o len.

if x < len(L):
    print(f"{p} achado na posição {x + 1}")
else:
    print(f"{p} não encontrado")      
      

# Exercício 6.9 - Modifique o exemplo para pesquisar dois valores. Em vez de apenas p,
# eia outro valor v que também será procurado Na impressão, indique qual dos
# dois valores foi achado primeiro.

L = [15, 7, 27, 39]
rodandoP = True
rodandoV = True
while rodandoP:
    p = int(input("Digite o primeiro valor a procurar: "))
    xp = 0
    while xp < len(L):
        if L[xp] == p:
            break
        xp += 1
    rodandoP = False
while rodandoV:
    v = int(input("Digite o segundo valor a procurar: "))
    xv = 0
    while xv < len(L):
        if L[xv] == v:
            break
        xv += 1
    rodandoV = False

if xp < len(L):
    print(f"{p} achado na posição {xp + 1}")
else:
    print(f"{p} não foi encontrado")

if xv < len(L):
    print(f"{v} achado na posição {xv + 1}")
else:
    print(f"{v} não foi encontrado")

# Comparação de quem foi achado primeiro (apenas se ambos existirem)
if xp < len(L) and xv < len(L):
    if xp > xv:
        print("O segundo número foi achado primeiro.")
    else:
        print("O primeiro número foi achado primeiro.")

# 6.0 Utilizando for.

# O for percorre a lista do primeiro ao último elemento automaticamente.
# A variável após o for (ex: item) assume o valor do item atual em cada rodada.
# Use o break para parar a busca assim que encontrar o que quer.
# O else acoplado ao for é o seu "Plano B": ele só roda se a busca falhar totalmente.
# Exemplo:
L = [7, 9, 10, 12]
p = int(input("Digite um número para pesquisar: "))
for item in L:
    if e == p:
        print("Elemento encontrado")
        break
else:
    print("Elemento não encontrado")
    
# Exercício 6.11
# Modifique o Programa 6.6 usando for. Explique por que
# em todos os while podem ser transformados em for.

# Listagem 06-06: Adição de elementos à lista
L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
for x in L:
    print(x)    

# 6.10 - Range. É um limitador, delimita o intervalo de números que será executado.
# Exemplo 1:
for v in range(10):
    print(v) # Printa de 0 a 9. O último não conta.

for v in range(5, 8):
    print(v) # Printa 5, 6, 7

# Se acrescentarmos um terceiro parâmetro à função range, teremos como saltar
# entre os valores gerados, por exemplo:

for a in range(0, 10, 2):
    print(a) # Exibe os valores entre 0 e 10, dois a dois, ou seja os pares.
    
for a in range(0, 33, 3):
    print(a, end=" ") # Exibe os 10 primeiros múultiplos de 3.

# Essa função .end no print, faz com que a cada item não seja pulado uma linha.
# Assim, todos os itens ficam em sequência.

# Como transformar um range em uma lista?? FUNÇÃO LIST.

L = list(range(0, 110, 10))
print(L, end="") #Printei uma lista dos dez primeiros múltiplos de 10.

# 6.11 - Enumerate.
# Exemplo usando contador, para gerar uma lista com índices enumerados.
L = [5, 9, 13]
x = 0
for e in L:
    print(f"{[x]} {e}")
    x += 1

# Utilizando a função enumerate:
L = [5, 9, 13]
for x, e in enumerate(L):
    print(f"{[x]} {e}")
    

# o wue o enumerate faz? Ele pega a lista e a transforma em pares.
# (0, 5) (1, 9) (2, 13) - (índice, valor)
# Desempacotamento da tupla: se eu mando x, e = (0,5), ele desempacota em x = 0  e = 5.

# Desse jeito, eu desempacoto o par, depois de printa-lo.
L = [5, 9, 13]
for z in enumerate(L):
    x, e = z
    print(z)
    print(f"{[x]} {e}")
    
# 6.12 - Operações com listas.
# Programa 6.11: Verificação do maior valor
L = [1, 7, 2, 4]
máximo = L[0]
for e in L:
    if e > máximo:
        máximo = e
print(máximo)

# Exercício 6.12 - Altere o programa 6.11 de forma a imprimir o menor elemento da lista.

L = [1, 7, 2, 4]
mínimo = L[0]
for e in L:
    if e < mínimo:
        mínimo = e
print(mínimo)

# Exercício 6.13 - A lista de temperaturas de Mons, na Bélgica, foi armazenada
# na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que
# imprima a menor e a maior temperatura, assim como a temperatura média.

# Meu jeito:
T = [ -10, -8, 0, 1, 2, 5, -2, -4]
mínima = T[0]
for e in T:
    if e < mínima:
        mínima = e
print(f"A temperatura mínima foi de {mínima}")
máxima = T[0]
for e in T:
    if e > máxima:
        máxima = e
print(f"A temperatura máxima foi de {máxima}")
i = 0
soma = 0
while i < len(T):
    soma = soma + T[i]
    i += 1
print(f"A temepratura média foi de {soma / len(T)}")

# Jeito do livro:
T = [ -10, -8, 0, 1, 2, 5, -2, -4]
mínima = T[0]
máxima = T[0]
soma = 0
for e in T:
    if e < mínima:
        mínima = e
    if e > máxima:
        máxima = e
    soma += e
print(f"Temperatura máxima: {máxima} °C")
print(f"Temperatura mínima: {mínima} °C")
print(f"Temperatura média: {soma / len(T)} °C")

# 6.13 - Aplicações
# Programa 6.12: Cópia de elementos para outras listas
valores = [9, 8, 7, 12, 0, 13, 21]
pares = []
ímpares = []
for e in valores:
    if e % 2 == 0:
        pares.append(e)
    else:
        ímpares.append(e)
print("Pares: ", pares)
print("Ímpares: ", ímpares)    

# Como funciona a vírgula no print()?
# print("Pares: ", pares)
# Conversão Automática: O print é "inteligente" 
# o suficiente para converter quase qualquer objeto 
# (listas, números, dicionários) em texto para poder 
# mostrar no terminal, sem você precisar formatar nada manualmente.

# Programa 6.13: Controle da utilização de salas de um cinema

lugares_vagos = [10, 2, 1, 3, 0]
while True:
    sala = int(input("Sala (0 para sair): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos): "))
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
print("Utilização de salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")

# sala, vagos: São duas variáveis temporárias que criamos na hora.
# sala guarda o índice (0, 1, 2...) e vagos guarda o conteúdo daquela posição (10, 2, 1...).

# Exercício 6.14 - Modifique o Programa 6.13 de forma a mostrar quantos
# ingressos foram vendidos em cada sala. Utilize uma lista do
# mesmo tamanho da quantidade de salas e utilize seus
# elementos para contar quantos ingressos foram vendidos em
# cada sala. Imprima na tela o total das vendas no fim do programa;
# Meu jeito:

lugares_vagos = [10, 2, 1, 3, 0]
lugares_vagos_copia = [10, 2, 1, 3, 0]
while True:
    sala = int(input("Sala (0 para sair): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos): "))
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos_copia[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
i = 0            
while i < len(lugares_vagos):
    if lugares_vagos[i] == lugares_vagos_copia[i]:
         print(f"Nenhum ingresso vendido na sala {i + 1}")
    else:
        print(f"Foram vendido(s) {(lugares_vagos[i]) - (lugares_vagos_copia[i])} ingresso(s) na sala {i + 1}")
    i += 1
print("Utilização de salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")
    
# Jeito do livro:

lugares_vagos = [10, 2, 1, 3, 0]
vendidos = [0] * len(lugares_vagos) 
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(
            input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):")
        )
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            vendidos[sala - 1] += lugares
            print(f"{lugares} lugares vendidos")
print("\nUtilização das salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")
print("\nVendas por sala")
total_vendido = 0
for sala, vendas in enumerate(vendidos):
    print(f"Sala {sala + 1} - {vendas} ingressos vendido(s)")
    total_vendido += vendas
print(f"Total de ingressos vendidos: {total_vendido}")

# EXplicação de linhas, na linha 860, vendidos = [0] * len(lugares_vagos)
# Cria uma lista de zeros com o mesmo tamanho da lista de salas. vendidos = [0, 0, 0, 0, 0]
# Na linha 880, vendidos[sala - 1] += lugares: Quando a venda é confirmada, o código vai na lista de
# vendas, na posição daquela sala, e soma a quantidade comprada
# Na linha 887, for sala, vendas in enumerate(vendidos):
# O enumerate pega a lista de vendidos (ex: [2, 0, 5, 0, 0]).
# Ele entrega o índice (0, 1, 2...) para a variável sala.
# Ele entrega o valor guardado (quantos foram vendidos) para a variável vendas e peirnta os pares na tela.

# Exercício 6.15 - Modifique o Programa 6.13 de forma a perguntar o número de salas
# disponíveis no cinema, assim como a quantidade de lugares em cada
# uma delas.

# MEu jeito:
perg_quantidade_de_salas = int(input("Quantas salas vamos abrir no cinema hoje? "))
quantidade_de_salas = [0] * perg_quantidade_de_salas
ocupados = [0] * perg_quantidade_de_salas
i = 0
while i < len(quantidade_de_salas):
    assentos_por_sala = int(input(f"Quantos assentos tem disponível na sala {i + 1}? "))
    perg_ocupados = int(input(f"Quantos ingressos foram vendidos na sala {i + 1}? "))
    quantidade_de_salas[i] = assentos_por_sala
    ocupados[i] = perg_ocupados
    i += 1
lugares_vagos = [0] * perg_quantidade_de_salas
i = 0
while i < len(lugares_vagos):
    lugares_vagos[i] = quantidade_de_salas[i] - ocupados[i]
    i += 1
while True:
    sala = int(input("Sala (0 para sair): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos): "))
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
print("Utilização de salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")
    
    
# Jeito do livro:

n_salas = int(input("Número de salas: "))
lugares_vagos = []
for sala in range(n_salas):
    lugares_vagos.append(int(input(f"Lugares vagos na sala {sala + 1}: ")))

vendidos = [0] * len(lugares_vagos)
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(
            input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):")
        )
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            vendidos[sala - 1] += lugares
            print(f"{lugares} lugares vendidos")
print("\nUtilização das salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")
print("\nVendas por sala")
total_vendido = 0
for sala, vendas in enumerate(vendidos):
    print(f"Sala {sala + 1} - {vendas} ingressos vendido(s)")
    total_vendido += vendas
print(f"Total de ingressos vendidos: {total_vendido}")

# 6.14 Listas com strings:
S = ["maçãs", "peras", "kiwis"]
len(S) # 3
print(S[0]) # maçãs

# Programa 6.14: Lendo e imprimindo uma lista de compras
compras = []
while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    compras.append(produto)
for p in compras:
    print(p)
    
# 6.15 Listas dentro de listas
S = ["maçãs", "peras", "kiwis"]
print(S[0][0]) # m
print(S[0][1]) # a
print(S[1][2]) # r

# Programa 6.15: Impressão de uma lista de strings, letra a letra.
L = ["maçãs", "peras", "kiwis"]
for palavra in L:
    for letra in palavra:
        print(letra)

# 6.16: Listas com elementos de tipos diferentes:
produto1 = ["maçã", 10, 0.3]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]

# É possível criar listas, que contenham strings, inteiros e floats!

# Programa 6.17: Listas de listas
produto1 = ["maçã", 10, 0.3]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]
compras = [produto1, produto2, produto3] # Sim, é possível fazer uma lista de listas.
for e in compras:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: {e[2]}")
    
# Programa 6.19: Criação e impressão da lista de compras
compras = []
while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    quantidade = int(input("Quantidade: "))
    preço = float(input("Preço: "))
    compras.append([produto, quantidade, preço])
soma = 0
for e in compras:
    print(f"{e[0]:20s} x {e[1]:5d} {e[2]:5.2f} {e[1] * e[2]:6.2f}")
    soma += e[1] * e[2]
print(f"Total: {soma:7.2f}")
    
# Programa 6.20 - Ordenação pelo Bubble Sort
L = [7, 4, 3, 12, 8] # Cria a lista de números desordenados.
fim = 5 # Define o tamanho da "área de trabalho" inicial (5 elementos).
while fim > 1: # nquanto houver mais de um elemento para comparar, continue o trabalho.
    trocou = False # No início de cada rodada, assumimos que nada será trocado.
    x = 0 # O operário começa sempre na primeira posição (índice 0).
    while x < (fim - 1): # operário caminha do início até o penúltimo item da área de trabalho atual.
        if L[x] > L[x + 1]: # Pergunta: "O número da esquerda é maior que o da direita?".
            trocou = True # Se sim, acendemos o sinal de que houve mudança.
            temp = L[x] # Guardamos o número da esquerda numa "caixa temporária" para não perdê-lo.
            L[x] = L[x + 1] # Movemos o número menor para a esquerda.
            L[x + 1] = temp # Colocamos o número maior (que estava na caixa temporária) na direita
        x += 1 # O operário dá um passo à frente para comparar o próximo par.
    if not trocou: # Se após percorrer tudo, a luz trocou continuar apagada...
        break # paramos o código (a lista já está organizada).
    fim -= 1 # Diminuímos a área de trabalho, pois o último número já está no lugar certo.
for e in L: 
    print(e)

# Imagine que o nosso operário x tem braços curtos.
#  Para trabalhar, ele precisa colocar a mão esquerda na caixa atual
# (L[x]) e a mão direita na caixa seguinte (L[x + 1]).

# Cada rodada serve para colocar somente O MAIOR no final. Depois
# diminuimos 1 unidade do fim para deixar o maior lá e rodamos novamente para achar o maior
# dentro daquele intervalo, que no caso seria o segundo maior da lista.

# Exercício 6.16 - O que acontece quando a lista já está ordenada? rastreie
# o programa 6.20, mas com a lista L = [1, 2, 3, 4, 5]
L = [1, 2, 3, 4, 5]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1 
for e in L:
    print(e)

# Se a lista já estiver ordenada, nenhum elemento é maior que o elemento seguinte.
# Desta forma, após a primeira verificação de todos os elementos,
# o loop externo é interrompido pela condição de "if not trocou = break" e o código já printa
# verificando, assim, o loop interno somente 1 vez.

# Exercício 6.17 - O que acontece quando dois valores são iguais? Rastreie o Programa
# 6.20, mas com a lista L = [3, 3, 1, 5, 4].
# Como utilizamos o método de bolhas, na primeira verificação, 3, 3 
# são considerados como na ordem correta. Quanto verificamos o segundo 3 com 1, ocorre uma troca.
# O mesmo vai ocorrer com o primeiro 3, mas apenas na próxima repetição
# Veja que o 1 subiu para a primeira posição como uma bolha de ar dentro d'água.

# Exercício 6.18 - Modifique o Programa 6.20 para ordenar a lista em ordem decrescente.
# L = [1, 2, 3, 4, 5] deve ser ordenada como L = [5, 4, 3, 2, 1].

L = [1, 2, 3, 4, 5]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] < L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1 
for e in L:
    print(e)
    
# Método sort ordena automaticamente uma lista
L = [6, 4, 2, 1, 9]
L.sort()
print(L)

# Função sorted ordena uma lista, porém sem alterar seus elementos.
Z = [4, 3, 1]
print(sorted(Z)) # [1, 3, 4]
print(Z) # [4, 3, 1]

# 6.17 - Dicionários.
tabela = {"Alface": 0.45,
          "Batata": 1.2,
          "Tomate": 2.3,
          "Feijão": 1.5}
# O dicionário é composto por chave + valor, aqui a chave é "Alface" e o valor é 0.45.
# Para saber o preço do tomate posso fazer isso:
print(tabela["Tomate"]) # 2.3
print(tabela)

# Posso alterar o valor de algum irem dessa forma:
tabela["Feijão"] = 1.8

# Também posso criar um novo valor que será adicionado a tabela
tabela["Cebola"] = 1.75
print(tabela)

# Operador in serve para verificar se uma chave pertence ao dicionário.
tabela = {"Alface": 0.45,
          "Batata": 1.2,
          "Tomate": 2.3,
          "Feijão": 1.5}
print("Manga" in tabela) # False
print("Batata" in tabela) # True

# Métodos keys() e values(), keys retorna as chaves e values retorna os valores
# Você pode utilizando a funcção list, transformar isso em uma lista.
tabela = {"Alface": 0.45,
          "Batata": 1.2,
          "Tomate": 2.3,
          "Feijão": 1.5}
print(tabela.keys()) # dict_leys(['Alface', 'Batata', 'Tomate', 'Feijão'])
print(tabela.values()) # dict_values([0.45, 1.2, 2.3, 1.5])

# Programa 6.21: Obtenção do preço com um dicionário.
tabela = {"alface": 0.45,
          "batata": 1.2,
          "tomate": 2.3,
          "feijão": 1.5}
while True:
    produto = input("Digite o nome do produto (fim para sair): ").lower() # Lower transforma a palavra inteira 100% em minuscula.
    if produto == "fim":
        break
    if produto in tabela:
        print(f"Preço: R${tabela[produto]:5.2f}")
    else:
        print("Produto não encontrado.")
# Para apagar uma chave, pode-se utilizar a instrução del.
del tabela["tomate"]
print(tabela)

# 6.18 - Dicinonários com listas;

estoque = {"alface": [500, 0.45],
          "batata": [2001, 1.2],
          "tomate": [1000, 2.3],
          "feijão": [100, 1.5]}
# Nesse caso, os itens são as chaves e os valores associados às chaves são listas.

# Programa 6.22 - Exemplo de dicionário com estoque e operações de venda
estoque = {"tomate": [1000, 2.30],
            "alface": [500, 0.45],
            "batata": [2001, 1.20],
            "feijão": [100, 1.50]}

venda = [["tomate", 5], ["batata", 10], ["alface", 5]] # Um papelzinho anotado com o que os clientes acabaram de comprar. Contém o nome do produto e quanto foi vendido.
total = 0
print("Vendas:\n")
for operação in venda: # Inicia um loop que vai ler cada "pedacinho" da lista de vendas.
    produto, quantidade = operação # Desempacotamento. Ele quebra a lista ["tomate", 5] e joga "tomate" na variável produto e 5 na variável quantidade.
    preço = estoque[produto][1] # Vai ao dicionário estoque, procura a chave (ex: "tomate") e pega o item na posição [1] da lista de valores (o preço), a qual está associada a chave "tomate".
    receita = preço * quantidade # Multiplica o valor unitário pela quantidade vendida.
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {receita:6.2f}")
    estoque[produto][0] -= quantidade
    total += receita # Soma o valor dessa venda ao valor total acumulado.
print(f" Receita total: {total:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items(): # O método items GERA pares de duplas, contendo a chave o valor associado a essa chave.
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
    
# Exercício 6.19 - ltere o Programa 6.22 de forma a solicitar ao usuário o produto e a quantidade vendida.
# Verifique se o nome do produto digitado existe no dicionário, e só então efetue a baixa em estoque.

# Meu jeito:
estoque = {"tomate": [1000, 2.30],
            "alface": [500, 0.45],
            "batata": [2001, 1.20],
            "feijão": [100, 1.50]}
i = 0
lista_venda_produto = []
lista_venda_quantidade = []
lista_fusão_das_duas = []
while i < len(estoque):
    venda_produto = input("Produtos vendidos (fim para sair): ").lower()
    if venda_produto in estoque:
        lista_venda_produto.append(venda_produto)
    elif venda_produto == "fim":
        break
    else:
        print("Produto indisponível!")
    venda_quantidade = int(input(f"Quantidade de {venda_produto}(s) comprados(as): "))
    lista_venda_quantidade.append(venda_quantidade)
    i += 1
for a in range(len(lista_venda_produto)):
    sublista = [lista_venda_produto[a], lista_venda_quantidade[a]]
    lista_fusão_das_duas.append(sublista) # Essa lista de fusão das duas, vai ficar assim, por exemplo: [['batata', 15], ['feijão', 3], ['alface', 12]]
total = 0
print("Vendas:\n")
for operação in lista_fusão_das_duas: 
    produto, quantidade = operação 
    preço = estoque[produto][1]
    receita = preço * quantidade 
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {receita:6.2f}")
    estoque[produto][0] -= quantidade
    total += receita 
print(f" Receita total: {total:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
    
# Jeito do livro:
estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50],
}
total = 0
print("Vendas:\n")
while True:
    produto = input("Nome do produto (fim para sair):")
    if produto == "fim":
        break
    if produto in estoque:
        quantidade = int(input("Quantidade:"))
        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade solicitada não disponível")
    else:
        print("Nome de produto inválido")
print(f" Custo total: {total:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")

# Exercício 6.20 - Escreva um programa que gere um dicionário, em que cada chave seja
# um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.
# Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}

frase = input("Digite uma frase para contar as letras:").replace(" ", "")
d = {}
for letra in frase:
    if letra in d: # OLha para ver se aquela letra já foi registrada antes no dicionário.
        d[letra] = d[letra] + 1 # Se a letra já existia, pegamos o valor que estava lá (ex: era 1) e somamos +1 (vira 2). 
    else:
        d[letra] = 1 # Criamos uma página nova no nosso livro para essa letra e anotamos que ela apareceu pela primeira vez (valor 1).
print(d)

# 6.19 - Dicionários com valor padrão
# Programa 6.23: Exemplo de dicionário sem valor padrão
d = {}
for letra in "abracadabra":
    if letra in d:
        d[letra] += 1
    else:
        d[letra] = 1
print(d) # {'a': 5, 'b': 2, 'r': 2, 'c': 'd': 1}

# É possível simplificar isso utilizando o método get.
# Programa 6.24: Exemplo de dicionário com valor padrão
d = {}
for letra in "abracadabra":
    d[letra] = d.get(letra, 0) + 1
print(d)

# 6.20 - Tuplas.
# É a mesma coisa que lista só que não pode alterra os valores e utiliza () ou nada (não precisa mas fica mais organizado com) no lugar de []
tupla = ("a", "b", "c")
tupla[0] = "D" # Vai dar ERRO!  

# Tuplas podem ser utilizadas para desempacotar valores.
a, b = 10, 20 # Aqui, por ex, não usei () pq não é obrigatório.
print(a) # 10
print(b) # 20

# TAmbém podemos trocar valores de variáveis sem precisar de uma variável intermediária.
a, b = 10, 20
a, b = b, a
print(a) # 20
print(b) # 10

# para criar uma tupla com somente 1 elemento é preciso usar a vírgula no final
t1 = 1,
print(t1)
t1 = 1 # Aqui ele vai achar que é somente um número inteiro pq vc nn colocou a vírgula
print(t1) 

# É possível transformar listas em tuplas, com a função tuple.
L = [1, 2, 3]
T == tuple(L)
print(T) # (1, 2, 3,)

# É possível concantenar tuplas (obviamente sem alterar seus valores):
t1 = 1, 2, 3
t2 = 4, 5, 6
t3 = t1 + t2
print(t3)

# Se uma tupla possuir uma lista dentro dela, é possível alterar a lista e não alterar a tupla diretamente.
t = "a", ["b", "c", "d"]
len(t) # 2
t[1] # ['b', 'c'. 'd']
t[1].append("e")
print(t)

# Podemos utilizar o * para indicar vários valores a desempacotar.
*a, b = [1, 2, 3, 4, 5]
print(a) # [1, 2, 3, 4]
print(b) # 5

# 6.21 - Conjuntos:
# Não admite repetições e não mantém a ordem de seus elementos;

a = set() # Criei um conjunto vazio.
a.add(1)
a.add(2)
a.add(3)
print(a) # {1, 2, 3}
a.add(1)
print(a) # {1, 2, 3} Como o 1 já faz parte, a ação de adicionar ele denovo é ignorada.

# Podemos testar se um elemento faz parte de um conjunto usando o operador in do python
print(1 in a) # True
print(-2 in a) # False

# Um conjunto pode ser criado a partir de listas, tuplas e qualquer outra estrutura de dados enumerável.
b = set([2, 3])
print(b) # {2, 3}
len(b) # 2 (Sim a função len também funciona em conjuntos)

# 6.21.1 - União
# A união de conjuntos é realizada pelo operador | e resulta em um novo conjunto com todos os elementos.
a = {0, 1, 2, 3, -1}
b = {2, 3}
c = set([4, 5, 6]) 
print(a | b) # {0, 1, 2, 3, -1} # Ficou igual a "a" pois ele não admite repetições;
a.union(b) # TAmbém pode ser escrito assi, é a mesma coisa.
print(a | c) # {0, 1, 2, 3, 4, 5, 6, -1} 

#6.21.2 - Intersecção.
a = {1, 2, 3, 6}
b = {2, 4, 5, 6}
print(a & b) # {2, 6} - São os lementos em comum aos dois conjuntos;
a.intersection(b) # Mesma coisa

# 6.21.3 - DIferença.
a = {0, 1, 2, 3, -1}
b = {2, 3}
print(a - b) # {0, 1, -1} # Elementos de "a" que não estão presentes em "b".
a = {1, 2, 3, 6}
b = {2, 4, 5, 6}
print(a - b) # {1, 3}
a.difference(b)

# 6.21.4 - Diferença simétrica - É os elementos que não são comuns aos dois, ou seja  é tudo menos a intersecção.
a = {1, 2, 3, 6}
b = {2, 4, 5, 6}
print(a ^ b) # {1, 3, 4, 5}
a.symmetric_difference(b)

# 6.21.5 - Outras operações.
# Como saber se um conjunto contém outro?
a = {x for x in range(0, 10, 2)}
print(a) # {0, 2, 4, 6, 8}
b = {2, 4}

# Podemos verificar se um conjunto contém o outro usando o maior (>):
print(a > b) # True - Todos os elementos de "b" estão em "a".
print(b > a) # False - Nem todo elemento de "a" pertence a "b"
print(a > a) # False - Todos os elementos de "a" estão em "a". Porém os dois conjuntos são iguais.

# Podemos verificar se conjuntos possuem os mesmos elementos utilizando ==
print(a == a) # True
print(b == {2, 4}) # True
print(a != a) # False

# Testando se um conjunto é vazio.
if {}:
    print("Não vazio!") 
else:
    print("Vazio!")
print(bool({})) # False 
# Bool é uma função que converte qualquer coisa em verdadeiro ou falso., ex: bool(algo) retorna True se tiver conteúdo ou False se tiver vazio ou 0.
print(len({})) # 0

# Exemplos de usos de conjuntos:
e = [1, 2, 3, 4]
f = [3, 4, 5, 6]

# Juntando as duas listas, sem repetir os elmentos e sem garantia de ordem:
print(set(e) | set(f)) # {1, 2, 3, 4, 5, 6}

# Elementos da lista "e" que não estão em "f":
print(set(e) - set(f)) # {1, 2}

# Elementos que estão apenas em "e" ou "f" (tudo menos a intersecção):
print(set(e) ^ set(f)) # {1, 2, 5, 6}

# Elementos que estão tanto em "e" tant em "f" (intersecção):
print(set(e) & set(f)) # {3, 4}

# Exercício 6.21 - Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
# os valores comuns às duas listas:
# os valores que só existem na primeira:
# os valores que existem apenas na segunda:
# uma lista com os elementos não repetidos das duas listas:
# a primeira lista sem os elementos repetidos na segunda:

a = [1, 2, 3, 4, 5]
b = [3, 4, 6]
print(set(a) & set(b))
print(set(a) - set(b))
print(set(b) - set(a))
print(set(a) ^ set(b))
print(set(a) - set(b))

# Exercício 6.22 - Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e a segunda como a
# versão após alterações. Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações
# entre essas duas versões, listando:
# os elementos que não mudaram:
# os novos elementos:
# os elementos que foram removidos:

a = [5, 6 ,7, 8, 9, 10]
b = [5, 6, 9, 10, 11]
print("Lista de modificações:")
print(f"os elementos que não mudaram: {set(a) & set(b)}")
print(f"Os novos elementos: {set(b) - set(a)}")
print(f"Os elementos que foram removidos: {set(a) - set(b)}")