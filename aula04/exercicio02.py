lista_n = []
numero_elementos = int(input("Digite o número de elementos da lista: "))
for i in range(numero_elementos):
    valor = int(input("Digite um número: "))
    lista_n.append(valor)

# Ordenar a lista
lista_n.sort()

# Imprimir a lista já ordenada
print(lista_n)
