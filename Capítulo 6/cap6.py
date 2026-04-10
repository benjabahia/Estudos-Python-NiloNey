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
