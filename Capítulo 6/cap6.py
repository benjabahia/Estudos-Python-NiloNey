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
    