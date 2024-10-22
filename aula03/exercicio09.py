idade_novo = 120  # aluno mais novo
idade_velho = 0   # aluno mais velho
nota_maior = 0
mulheres = 0
turma_maior = 0  # turma de maior nota
genero_maior = 0 # gênero de maior nota
turma_velho = 0
turma_novo = 0
numero_turmas = int(input("Digite o número de turmas: "))

for i in range(numero_turmas):
    turma = int(input("Digite o número da turma: "))
    alunos = int(input("Digite o número de alunos: "))

    for j in range(alunos):
        idade = int(input("Digite a idade do aluno: "))
        genero = int(input("Digite 1 para masculino e 0 para feminino: "))
        nota = int(input("Digite a nota de entrada: "))

        #verificar a maior nota
        if nota > nota_maior:
            nota_maior = nota
            turma_maior = turma
            genero_maior = genero

        #verificar o aluno mais novo
        if idade < idade_novo:
            idade_novo = idade
            turma_novo = turma

        #verificar o aluno mais velho
        if idade > idade_velho:
            idade_velho = idade
            turma_velho = turma

        #contar o número de mulheres
        if genero == 0:
            mulheres += 1

if genero_maior == 1:
    genero_maior = "masculino"
else:
    genero_maior = "feminino"

print(f"A turma com o aluno mais novo é a turma {turma_novo}")
print(f"A turma com o aluno mais velho é a turma {turma_velho}")
print(f"O número total de mulheres é {mulheres}")
print(f"A maior nota é {nota_maior}, da turma {turma_maior}")
print(f"O gênero do aluno com a maior nota ({nota_maior}) foi {genero_maior}")
