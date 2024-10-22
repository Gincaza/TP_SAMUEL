while True:
    a = int(input("digite nota geografia: "))
    b = int(input("digite a nota em mtm: "))
    c = int(input("digite a nota em inglês: "))
    d = int(input("digite a nota em português: "))
    media = (a + b + c + d) / 4
    if media >= 0 and media < 9.5:
        print("reprovado")
        break
    elif media >= 9.5 and media <= 20:
        print("aprovado")
    else:
        print("digite outra nota")