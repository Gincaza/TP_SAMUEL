variavel
    tabuleiro: vetor[1..9] de inteiro
    jogador: inteiro
    jogada, i: inteiro
    ganhou: logico

procedimento ExibirTabuleiro()
inicio
    escreval(tabuleiro[1], " | ", tabuleiro[2], " | ", tabuleiro[3])
    escreval("--|---|--")
    escreval(tabuleiro[4], " | ", tabuleiro[5], " | ", tabuleiro[6])
    escreval("--|---|--")
    escreval(tabuleiro[7], " | ", tabuleiro[8], " | ", tabuleiro[9])
fimalgoritmo

funcao VerificarVitoria(): logico
inicio
    // Verifica linhas, colunas e diagonais
    se (tabuleiro[1] = tabuleiro[2]) e (tabuleiro[2] = tabuleiro[3]) entao
        retorne verdadeiro
    fimse
    se (tabuleiro[4] = tabuleiro[5]) e (tabuleiro[5] = tabuleiro[6]) entao
        retorne verdadeiro
    fimse
    se (tabuleiro[7] = tabuleiro[8]) e (tabuleiro[8] = tabuleiro[9]) entao
        retorne verdadeiro
    fimse
    se (tabuleiro[1] = tabuleiro[4]) e (tabuleiro[4] = tabuleiro[7]) entao
        retorne verdadeiro
    fimse
    se (tabuleiro[2] = tabuleiro[5]) e (tabuleiro[5] = tabuleiro[8]) entao
        retorne verdadeiro
    fimse
    se (tabuleiro[3] = tabuleiro[6]) e (tabuleiro[6] = tabuleiro[9]) entao
        retorne verdadeiro
    fimse
    se (tabuleiro[1] = tabuleiro[5]) e (tabuleiro[5] = tabuleiro[9]) entao
        retorne verdadeiro
    fimse
    se (tabuleiro[3] = tabuleiro[5]) e (tabuleiro[5] = tabuleiro[7]) entao
        retorne verdadeiro
    fimse
    retorne falso
fimalgoritmo

inicio
    // Inicializando o tabuleiro
    para i de 1 ate 9 faca
        tabuleiro[i] <- i
    fimpara

    jogador <- 1
    ganhou <- falso

    // Loop do jogo
    enquanto (ganhou = falso) faca
        limpatela
        ExibirTabuleiro()

        escreva("Jogador ", jogador, ", escolha uma posição: ")
        leia(jogada)

        // Verifica se a posição é válida
        se (tabuleiro[jogada] <> 'X') e (tabuleiro[jogada] <> 'O') entao
            se jogador = 1 entao
                tabuleiro[jogada] <- 'X'
                jogador <- 2
            senao
                tabuleiro[jogada] <- 'O'
                jogador <- 1
            fimse
        senao
            escreval("Posição inválida, tente novamente.")
        fimse

        // Verifica se alguém ganhou
        ganhou <- VerificarVitoria()
    fimenquanto

    limpatela
    ExibirTabuleiro()
    escreval( O jogador ", 3 - jogador, " venceu!")
fimalgoritmo


