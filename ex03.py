#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# 3 - Programa que imprime a soma de todos os números 
# pares entre dois números quaisquer, incluindo-os.

# entrada de dados
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

# variável para armazenar a soma dos números pares
# entre os dois valores
somaPares = 0

# processamento
# tratamento para o valor1 ser sempre menor que o valor2
if valor1 > valor2: # se o valor1 for maior que o valor2
    temp1 = valor2 # para usar no print de saída
    aux = valor1 # variável auxiliar para armazenar o valor1
    valor1 = valor2 # valor1 recebe o valor2
    valor2 = aux # valor2 recebe o valor1
    
while valor1 <= valor2:
    if valor1 % 2 == 0:
        somaPares += valor1
    valor1 += 1
    
# saída de dados
print(f"A soma dos números pares entre {temp1} e {valor2} é: {somaPares}")

