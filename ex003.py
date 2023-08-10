""" 
Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

n1 = int(input('insira um número: '))
n2 = int(input('insira outro número maior: '))

while n2-1 > n1:
    print(n1+1)
    n1 += 1

Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a colônia B com 10 elementos.

n1 = 4
n2 = 10

c1 = 0.03
c2 = 0.015
dias = 0

while n1 < n2:
    n1 *= 1 + c1
    n2 *= 1 + c2
    dias += 1
    print(f'levará {dias} dias para que a colonia a alcance a colonia b')


Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

i = 1

while i < 16:
    nota = int(input(f'Digite uma nota de 0 a 5 para o dado {i}: '))
    if nota < 0 or nota > 5:
        erro = int(input(f'Digite uma nota válida para o dado {i}: '))
        while erro < 0 or erro > 5:
            erro = int(input(f'Digite uma nota válida para o dado {i}: '))
    i += 1

Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e faça uma análise. Portanto, escreva um programa que leia temperaturas e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.

contagem = 0
soma = 0


while True:
    temp = int(input('Digite uma temperatura: '))
    
    if temp == -273:
        break

    soma += temp
    contagem += 1

if contagem > 0:
    media = soma/contagem
    print(f'A média das temperaturas que você digitou é: {media}')


Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. O fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.


n1 = int(input('Digite um número: '))
n2 = 1
i = n1

while i > 1:
    n2 *= i
    i -= 1

print(f'O fatorial de {n1} é {n2}')


"""
