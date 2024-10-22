
valores_inteiros = []
par = 0
impar = 0
for i in range(0,10):
    valor = int(input("digite um número: "))
    valores_inteiros.append(valor)
    if valor % 2 == 0:
        par = par + 1
    else:
        impar = impar+1

print(valores_inteiros)
diferenca = max(valores_inteiros) - min(valores_inteiros)
print("a diferença entre o maior e menor é: ",diferenca)
print("a quantidade de números pares é: ",par)
print(" a quantidade de números ímpares é: ",impar)




