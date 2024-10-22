numero = int(input("digite um número: "))
if numero < 2:
    primo = False
elif numero > 2:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i ==0:
            primo = False
            break
if primo:
    print("numero",numero," é primo")
else:
    print("não é primo ")




























