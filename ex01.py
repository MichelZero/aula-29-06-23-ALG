#
# autores: Michel e Cristiano

# data: 29/06/2023

# 1 - Programa que imprime a quantidade de números pares de 100 até 200, incluindo-os.

# 2 - Programa que imprime a soma dos números ímpares de 100 até 200, incluindo-os.

# usando o for
# 1
print("1 - Programa que imprime a quantidade de números pares de 100 até 200, incluindo-os.")

valor1 = 100
valor2 = 200

for i in range(valor1, valor2 + 1):
    if i % 2 == 0:
        print(i, end=" ")
        
# 2
print("2 - Programa que imprime a soma dos números ímpares de 100 até 200, incluindo-os.")

valor1 = 100
valor2 = 200
somaImpar = 0

for i in range(valor1, valor2 + 1):
    if i % 2 != 0:
        somaImpar += i
        
print(f"A soma dos números ímpares de 100 até 200 é: {somaImpar}")
