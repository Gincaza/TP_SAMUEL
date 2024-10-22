valores_inteiros = []
par = 0
impar = 0

for i in range(10):
    valor = int(input("Digite um número: "))
    valores_inteiros.append(valor)
    if valor % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Lista de valores: {valores_inteiros}")
diferenca = max(valores_inteiros) - min(valores_inteiros)
print(f"A diferença entre o maior e o menor número é: {diferenca}")
print(f"A quantidade de números pares é: {par}")
print(f"A quantidade de números ímpares é: {impar}")
