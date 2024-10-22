tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
jogador_atual = 'X'
jogando = True
vencedor = None
jogadas = 0

# mostrar o tabuleiro
while jogando:
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--|---|--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--|---|--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

    # pede uma jogada
    jogada = input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")

    # checar se a jogada é válida
    if jogada in tabuleiro:
        tabuleiro[int(jogada) - 1] = jogador_atual
        jogadas = jogadas + 1

        # checar se há um vencedor
        if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] or  # Linha 1
            tabuleiro[3] == tabuleiro[4] == tabuleiro[5] or  # Linha 2
            tabuleiro[6] == tabuleiro[7] == tabuleiro[8] or  # Linha 3
            tabuleiro[0] == tabuleiro[3] == tabuleiro[6] or  # Coluna 1
            tabuleiro[1] == tabuleiro[4] == tabuleiro[7] or  # Coluna 2
            tabuleiro[2] == tabuleiro[5] == tabuleiro[8] or  # Coluna 3
            tabuleiro[0] == tabuleiro[4] == tabuleiro[8] or  # Diagonal 1
            tabuleiro[2] == tabuleiro[4] == tabuleiro[6]):   # Diagonal 2
            vencedor = jogador_atual
            jogando = False
        elif jogadas == 9:
            jogando = False  # empate

        #trocar jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    else:
        print("Posição inválida, tente novamente.")

# mostrar resultado
print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
print("--|---|--")
print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
print("--|---|--")
print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

if vencedor:
    print(f"Parabéns!  jogador {vencedor} venceu!")
else:
    print("Empate!")
