#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# 4 - Programa que calcule o fatorial de um número.
# 0! = 1
# 1! = 1
# 2! = 2*1 = 2
# 3! = 3*2*1 = 6
# 4! = 4*3*2*1 = 24
# 5! = 5*4*3*2*1 = 120

# entrada de dados
numero = int(input("Digite um número: "))

# variável para armazenar o fatorial
fatorial = 1

# processamento
while numero > 0:
    print(f"{numero}*{fatorial}={numero*fatorial}")
    fatorial *= numero # fatorial = fatorial * numero
    numero -= 1 # numero = numero - 1
    
# saída de dados
print(f"O fatorial é: {fatorial}")