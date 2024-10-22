INICIO
    // Variáveis
    turmaMaisNovo <- ""
    turmaMaisVelho <- ""
    turmaNotaMaisAlta <- ""
    idadeMaisNova <- 999
    idadeMaisVelha <- 0
    notamaisalta <- 0
    generoNotaMaisAlta <- -1
    totalRaparigas <- 0

    // número de turmas
    ESCREVA "Quantas turmas existem?"
    LEIA numTurmas

    // repetição para cada turma
    PARA i DE 1 ATÉ numTurmas FAÇA
        ESCREVA "Nome da turma ", i, ":"
        LEIA nomeTurma

        // Número de alunos na turma
        ESCREVA "Quantos alunos na turma ", nomeTurma, "?"
        LEIA numAlunos

        // repetição para cada aluno na turma
        PARA j DE 1 ATÉ numAlunos FAÇA
            ESCREVA "Idade do aluno ", j, " da turma ", nomeTurma, ":"
            LEIA idade
            ESCREVA "Género do aluno ", j, " da turma ", nomeTurma, " (1 para masculino, 0 para feminino):"
            LEIA genero
            ESCREVA "Nota de entrada do aluno ", j, " da turma ", nomeTurma, ":"
            LEIA notaEntrada

            // Verifica a idade mais nova
            SE idade < idadeMaisNova ENTÃO
                idadeMaisNova <- idade
                turmaMaisNovo <- nomeTurma
            FIMSE

            // Verifica a idade mais velha
            SE idade > idadeMaisVelha ENTÃO
                idadeMaisVelha <- idade
                turmaMaisVelho <- nomeTurma
            FIMSE

            // Conta o número de raparigas
            SE genero = 0 ENTÃO
                totalRaparigas <- totalRaparigas + 1
            FIMSE

            // Verifica a nota de entrada mais alta
            SE notaEntrada > notaMaisAlta ENTÃO
                notaMaisAlta <- notaEntrada
                generoNotaMaisAlta <- genero
                turmaNotaMaisAlta <- nomeTurma
            FIMSE
        FIMPARA
    FIMPARA

    // Resultados
    ESCREVA "A turma com o aluno mais novo é: ", turmaMaisNovo
    ESCREVA "A turma com o aluno mais velho é: ", turmaMaisVelho
    ESCREVA "O número total de raparigas nos TeSP-DEE é: ", totalRaparigas
    ESCREVA "A turma com o aluno com a nota de entrada mais alta é: ", turmaNotaMaisAlta
    ESCREVA "A nota de entrada mais alta é: ", notaMaisAlta, " e o género da pessoa é: ", SE (generoNotaMaisAlta = 1) ENTAO "Masculino" SENAO "Feminino" FIMSE
FIM
