#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# 7 - Escreva um programa que solicite ao usuário 
# que digite uma sequência de números e calcule a média

# entrada de dados
num = int(input("Digite um número (ou zero para encerrar): "))
soma = 0
quantidade = 0

# processamento
while num != 0: # enquanto o número for diferente de zero
    soma += num # soma = soma + num
    quantidade += 1 # quantidade = quantidade + 1
    num = int(input("Digite um número (ou zero para encerrar): ")) 
    
if quantidade > 0: # se a quantidade de números for maior que zero
    media = soma / quantidade # calcula a média dos números digitados 
    print("A média dos números é:", media)
else:
    print("Nenhum número foi digitado.")
    
    