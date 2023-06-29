#
# autores: Michel e Cristiano

# data: 29/06/2023

# 10 - Escreva um programa que solicite ao usuário que digite
# um número e verifique se é um número perfeito. Um número 
# perfeito é aquele cuja soma dos seus divisores, excluindo 
# ele mesmo, é igual ao próprio número. 
# Por exemplo, o número 6 é perfeito (1 + 2 + 3 = 6).

# entrada de dados
num = int(input("Digite um número: "))
soma_divisores = 0 # acumulador de divisores (excluindo o próprio número)
divisor = 1 # contador de divisores (excluindo o próprio número)

# processamento
while divisor < num: # enquanto o divisor for menor que o número digitado pelo usuário (excluindo o próprio número)
    if num % divisor == 0: # se o resto da divisão do número pelo divisor for zero (divisor é divisor de num)
        soma_divisores += divisor # soma o divisor ao acumulador de divisores (excluindo o próprio número)
    divisor += 1 # incrementa o divisor em 1 (excluindo o próprio número)

if soma_divisores == num: # se a soma dos divisores (excluindo o próprio número) for igual ao número digitado pelo usuário
    print("É um número perfeito.")
else:
    print("Não é um número perfeito.")
