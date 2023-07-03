# 1
print("1 - Programa que imprime a quantidade de números pares de 100 até 200, incluindo-os.")

valor1 = 100
valor2 = 200

while valor1 <= valor2:
    if valor1 % 2 == 0:
        print(valor1, end=" ")
    valor1 += 1
    
# 2
print()
print("2 - Programa que imprime a soma dos números ímpares de 100 até 200, incluindo-os.")

valor1 = 100
valor2 = 200
somaImpar = 0

while valor1 <= valor2:
    if valor1 % 2 != 0:
        somaImpar += valor1
    valor1 += 1
    
print(f"A soma dos números ímpares de 100 até 200 é: {somaImpar}")