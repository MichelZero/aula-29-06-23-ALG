#
# autores: Michel e Cristiano

# data: 29/06/2023




# criar a classe PessoaIMC
class PessoaIMC():
    situacao = ''
        
    def __init__(self, nome1, nascimento, peso, altura) -> None:
        self.nome = nome1
        self.nascimento = nascimento
        self.peso = peso
        self.altura = altura
        
    
    def calculaIMC(self):
        # calculadora
        # return valor FLOAT resultIMC()
        valorIMC = self.peso / (self.altura**2)
        return valorIMC
    
    def  resultIMC(self):
        # chamar a calculaICM() e receber um FLOAT
        # IMC = self.calculaIMC()
        # if 16 <= IMC <= 16.99:
        #   imprima(f'seu IMC foi de {IMC} - Baixo peso Grau II')
        # elif 17 <= IMC <= 18.49:
        #   imprima(f'seu IMC foi de {IMC} - Baixo peso Grau I')
        IMC = self.calculaIMC()
        if 16 <= IMC <= 16.99:
            #print(f'seu IMC foi de {IMC} - Baixo peso Grau II')
            self.situacao = f'seu IMC foi de {IMC} - Baixo peso Grau II'
        elif 17 <= IMC <= 18.49:
            # print(f'seu IMC foi de {IMC} - Baixo peso Grau I')
            self.situacao = f'seu IMC foi de {IMC} - Baixo peso Grau I'
        # – 18,50 a 24,99 - Peso ideal 
        # – 25,00 a 29,99 - Sobrepeso 
        # – 30,00 a 34,99 - Obesidade Grau I 
        # – 35,00 a 39,99 - Obesidade Grau II >
        else:
            #print('você está flutuando')
            self.situacao = 'você está flutuando'
            
        return self.situacao
    
    