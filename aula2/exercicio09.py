n = int(input("digite o número de alunos da turma: "))
soma_altura = 0
soma_idade = 0
aluno_velho = 0
aluno_novo = 0
idade_min = 0
idade_max = 120
altura_max = 230
altura_min = 0
for i in range(0, n):
    altura = int(input("digite altura do aluno em cm: "))
    idade = int(input("digite a idade do aluno: "))
    soma_altura = soma_altura + altura
    soma_idade = soma_idade + idade
    media_altura = soma_altura / n
    media_idade = soma_idade / n
    if idade < idade_min  or idade_min ==0 :
        idade_min = idade
    if idade > idade_max:
        idade_max = idade
    if altura < altura_min or altura_min == 0:
        altura_min = altura
    if altura > idade_max:
        altura_max = altura

print("media altura: ",float(media_altura))
print(" media de idade é: ",float(media_idade))
print(" idade mais alta,",idade_max)
print("idade minima é: ",idade_min)
print("altura maxima é: ",altura_max)
