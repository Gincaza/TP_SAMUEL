lista_n = []
numero_elementos = int(input("Digite o número de elementos da lista: "))
for i in range(numero_elementos):
    valor = int(input("Digite um número: "))
    lista_n.append(valor)

print(lista_n)

valor_procurado = int(input("Digite o valor que procura: "))
if valor_procurado in lista_n:
    print(f"Valor {valor_procurado} encontrado.")
else:
    print("Valor não encontrado.")
