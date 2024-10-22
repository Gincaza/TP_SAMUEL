n = int(input("Digite um número: "))
i = 2
fatores = []
while n > 1:
    if n % i == 0:
        fatores.append(i)
        n //=i
    else:
        i = i + 1
print(fatores)











