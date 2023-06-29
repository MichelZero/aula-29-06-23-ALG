#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# 2 - programa para contar a quantidade de números pares 
# entre dois números quaisquer?

# entrada de dados
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

# variável para armazenar a quantidade de números pares
# entre os dois valores
qtdPares = 0

# processamento
# tratamento para o valor1 ser sempre menor que o valor2
if valor1 > valor2: # se o valor1 for maior que o valor2
    aux = valor1 # variável auxiliar para armazenar o valor1
    valor1 = valor2 # valor1 recebe o valor2
    valor2 = aux # valor2 recebe o valor1
    
while valor1 <= valor2:
    if valor1 % 2 == 0:
        qtdPares += 1
    valor1 += 1

# saída de dados
print(f"A quantidade de números pares entre {valor1} e {valor2} é: {qtdPares}")