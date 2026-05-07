# 7.2 Contagem - O método count serve para contar as ocorreências de algo na sua string.
t = "um tigre, dois tigres, três tigres"
print(t.count("tigre")) # 3
print(t.count("tigres")) # 2
print(t.count("t")) # 4

# Esse método também funciona em listas.
L = [1, 1, 1, 2]
print(L.count(1)) # 3