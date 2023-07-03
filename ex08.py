#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# 8 - Escreva um programa que solicite ao usuário que digite 
# um número entre 1 e 10 e repita a solicitação até que o número 
# digitado esteja dentro desse intervalo.

# entrada de dados
num = int(input("Digite um número entre 1 e 10: "))

# processamento
while num < 1 or num > 10:
    num = int(input("Número inválido. Digite novamente: "))

print(f"o número foi {num}")
print("fim do programa!")