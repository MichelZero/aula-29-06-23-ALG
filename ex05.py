#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# 5 - Escreva um programa que solicite ao usuário 
# que digite um número e imprima se esse número é primo.

# entrada de dados
num = int(input("Digite um número: "))

# processamento
divisor = 2 # para encontrar um divisor de num entre 2 e num-1 (inclusive) 
while divisor < num: # enquanto o divisor for menor que num 
    if num % divisor == 0: # se o resto da divisão de num por divisor for 0 
        print("Não é primo") # num não é primo
        break # interrompe o laço 
    divisor += 1 # incrementa o divisor em 1 
else:
    print("É primo") # se o laço terminar sem interrupção, num é primo 
