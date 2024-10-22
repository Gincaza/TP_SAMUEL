
# iniciar o tabuleiro 6x7
tabuleiro = [[' ' for _ in range(7)] for _ in range(6)]
jogador_atual = 'X'
jogando = True
vencedor = None
jogadas = 0

# mostra o tabuleiro
while jogando:
    # mostra o tabuleiro
    for linha in tabuleiro:
        print(' | '.join(linha))
    print('-' * 29)

    # pede jogada
    coluna = int(input(f"Jogador {jogador_atual}, escolha uma coluna (0-6): "))

    # checa se a coluna é válida
    if 0 <= coluna <= 6 and tabuleiro[0][coluna] == ' ':
        # encontrar a linha mais baixa disponível na coluna
        for linha in range(5, -1, -1):
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogador_atual
                jogadas += 1
                break

        # checa vitória (linhas)
        for linha in range(6):
            for col in range(4):
                if (tabuleiro[linha][col] == tabuleiro[linha][col + 1] == tabuleiro[linha][col + 2] == tabuleiro[linha][
                    col + 3] == jogador_atual):
                    vencedor = jogador_atual
                    jogando = False

        # checa vitória (colunas)
        for linha in range(3):
            for col in range(7):
                if (tabuleiro[linha][col] == tabuleiro[linha + 1][col] == tabuleiro[linha + 2][col] ==
                        tabuleiro[linha + 3][col] == jogador_atual):
                    vencedor = jogador_atual
                    jogando = False

        # checa vitória (diagonais descendo)
        for linha in range(3):
            for col in range(4):
                if (tabuleiro[linha][col] == tabuleiro[linha + 1][col + 1] == tabuleiro[linha + 2][col + 2] ==
                        tabuleiro[linha + 3][col + 3] == jogador_atual):
                    vencedor = jogador_atual
                    jogando = False

        # checa  vitória (diagonais subindo)
        for linha in range(3, 6):
            for col in range(4):
                if (tabuleiro[linha][col] == tabuleiro[linha - 1][col + 1] == tabuleiro[linha - 2][col + 2] ==
                        tabuleiro[linha - 3][col + 3] == jogador_atual):
                    vencedor = jogador_atual
                    jogando = False

        # troca o jogador
        if vencedor is None:
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        # checa empate
        if jogadas == 42 and vencedor is None:
            jogando = False
    else:
        print("Coluna inválida, tente novamente.")

# mostrar o tabuleiro final
for linha in tabuleiro:
    print(' | '.join(linha))
print('-' * 29)

# mostrar o resultado
if vencedor:
    print(f" O jogador {vencedor} venceu!")
else:
    print("Empate!")
