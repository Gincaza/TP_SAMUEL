while True:
    a = int(input("Digite a nota de Geografia: "))
    b = int(input("Digite a nota de Matemática: "))
    c = int(input("Digite a nota de Inglês: "))
    d = int(input("Digite a nota de Português: "))
    
    #verifica se as notas são válidas (entre 0 e 20)
    if (0 <= a <= 20) and (0 <= b <= 20) and (0 <= c <= 20) and (0 <= d <= 20):
        media = (a + b + c + d) / 4
        
        if media < 9.5:
            print("Reprovado")
            break
        elif media >= 9.5:
            print("Aprovado")
            break
    else:
        print("Digite outra nota válida (entre 0 e 20).")
