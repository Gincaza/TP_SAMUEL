i = 0
idade_nova = 999
nome_nova = ""

while i <= 999:
    numcartão = int(input("digite seu número de cartão: "))
    nome = (input("digite seu nome: "))
    idade = int(input("digite a idade: "))
    if idade == 999:
        break
    if idade < idade_nova:
        idade_nova = idade
        nome_nova = nome

print("O nome mais novo é", nome_nova, " idade é:", idade_nova)




