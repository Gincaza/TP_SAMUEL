lista_n = []
numero_elementos = int(input("digite número de elementos da lista: "))
for i in range(0,numero_elementos):
    valor = int(input("digite um número: "))
    lista_n.append(valor)

print(lista_n)
valor_procurado = int(input("digite o valor que procura: "))
if valor_procurado in lista_n:
    print(valor)
else:
    print("valor não encontrado")

