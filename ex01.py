#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer os programas usando o for e o while.

# 1 - Programa que imprime a quantidade de números pares de 100 até 200, incluindo-os.

# 2 - Programa que imprime a soma dos números ímpares de 100 até 200, incluindo-os.

# usando o for
# 1
print("1 - Programa que imprime a quantidade de números pares de 100 até 200, incluindo-os.")

valor1 = 100 # valor inicial
valor2 = 200 # valor final

for i in range(valor1, valor2 + 1): # +1 para incluir o valor final
    if i % 2 == 0: # se o resto da divisão por 2 for igual a 0, então é par
        print(i, end=" ") # end=" " para imprimir na mesma linha
        
# 2
print("2 - Programa que imprime a soma dos números ímpares de 100 até 200, incluindo-os.")

valor1 = 100
valor2 = 200
somaImpar = 0 # variável para armazenar a soma dos números ímpares de 100 até 200

for i in range(valor1, valor2 + 1):
    if i % 2 != 0: # se o resto da divisão por 2 for diferente de 0, então é ímpar
        somaImpar += i # somaImpar = somaImpar + i
        
print(f"A soma dos números ímpares de 100 até 200 é: {somaImpar}")


# usando o while
# 1
print("1 - Programa que imprime a quantidade de números pares de 100 até 200, incluindo-os.")

valor1 = 100
valor2 = 200

while valor1 <= valor2:
    if valor1 % 2 == 0:
        print(valor1, end=" ")
    valor1 += 1
    
# 2
print("2 - Programa que imprime a soma dos números ímpares de 100 até 200, incluindo-os.")

valor1 = 100
valor2 = 200
somaImpar = 0

while valor1 <= valor2:
    if valor1 % 2 != 0:
        somaImpar += valor1
    valor1 += 1
    
print(f"A soma dos números ímpares de 100 até 200 é: {somaImpar}")