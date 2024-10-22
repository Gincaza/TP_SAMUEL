n = int(input("Digite o número de alunos da turma: "))
soma_altura = 0
soma_idade = 0
idade_min = 120
idade_max = 0
altura_max = 0 
altura_min = 230

for i in range(n):
    altura = int(input("Digite a altura do aluno em cm: "))
    idade = int(input("Digite a idade do aluno: "))
    
    soma_altura += altura
    soma_idade += idade
    
    if idade < idade_min:
        idade_min = idade
    if idade > idade_max:
        idade_max = idade
    if altura < altura_min:
        altura_min = altura
    if altura > altura_max:
        altura_max = altura

# Cálculo das médias fora do loop
media_altura = soma_altura / n
media_idade = soma_idade / n

print("Média de altura: ", float(media_altura))
print("Média de idade: ", float(media_idade))
print("Idade mais velha: ", idade_max)
print("Idade mais nova: ", idade_min)
print("Altura máxima: ", altura_max)
print("Altura mínima: ", altura_min)
