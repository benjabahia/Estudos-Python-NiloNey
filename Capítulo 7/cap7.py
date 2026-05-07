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
L.count(1) # 3

# 7.3 Pesquisa de strings.