idade_novo = 120 #aluno mais novo
idade_velho = 0 #
nota_maior = 0
mulheres = 0
turma_maior = 0 # turma_maior = turma de maior nota
genero_maior = 0 # genero de maior nota
turma_velho = 0
turma_novo = 0
numero_turmas = int(input("digite o número de turmas: "))
idade_novo = 120  # aluno mais novo
idade_velho = 0  #
for i in range(0,numero_turmas):
    turma = int(input("digite sua turma: "))
    alunos = int(input("digite o número de alunos"))

    for j in range(0,alunos):
        idade = int(input("digite a sua idade: "))
        genero = int(input(" digite 1 para masculino e 0 para feminino: "))
        nota = int(input("digite a nota de entrada: "))
        if nota > nota_maior:
            nota_maior = nota
            turma_maior = turma
            genero_maior = genero
        if idade < idade_novo:
            idade_novo = idade
            turma_novo = turma
        if idade > idade_velho:
            idade_velho = idade
            turma_velho = turma
        if genero == 0:
            mulheres = mulheres + 1
        if genero_maior == 0:
            genero_maior = "mulher"

if genero_maior ==1:
    genero_maior = "masculino"
else:
    genero_maior = "feminino"
print(f" a turma com aluno mais novo é {turma_novo}")
print(f" a turma com aluno mais velho é {turma_velho} ")
print(f" o número de mulheres é {mulheres} ")
print(f" a nota mais alta é {nota_maior}")
print(f" a turma com nota maior é {turma_maior} ")
print(f" o genero de nota maior {nota_maior} foi {genero_maior}")
