# 1
lista = [10, 20, 30, 40, 50]
print("Lista inicial:", lista)

# 2 
print("Primeiro elemento:", lista[0])
print("Elemento do meio:", lista[len(lista)//2])
print("Último elemento:", lista[-1])

# 3 
lista[2] = 99 
print("Lista após modificação:", lista)

# 4 
novo_numero = int(input("Digite um número para adicionar à lista: "))
lista.append(novo_numero)
print("Lista após adicionar o número:", lista)

# 5 
remover = int(input("Digite um número para remover da lista: "))
if remover in lista:
    lista.remove(remover)
else:
    print("O número não está na lista.")
print("Lista final:", lista)