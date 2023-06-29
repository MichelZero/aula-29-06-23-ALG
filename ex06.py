#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# 6 - Escreva um programa que solicite ao usuário que digite números
# positivos e imprima a soma desses números. 
# Encerre a leitura quando o usuário digitar um número negativo.

# entrada de dados
num = int(input("Digite um número positivo (ou negativo para encerrar): "))
soma = 0

# processamento
while num >= 0:
    soma += num
    num = int(input("Digite um número positivo (ou negativo para encerrar): "))
print(soma)
