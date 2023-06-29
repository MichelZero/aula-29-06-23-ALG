#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# 4 - Programa que calcule o fatorial de um número.

# entrada de dados
numero = int(input("Digite um número: "))

# variável para armazenar o fatorial
fatorial = 1

# processamento
while numero > 0:
    fatorial *= numero # fatorial = fatorial * numero
    numero -= 1 # numero = numero - 1
    
# saída de dados
print(f"O fatorial é: {fatorial}")