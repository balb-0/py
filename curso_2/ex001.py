"""
import matplotlib.pyplot as plt


estudantes = ['João', 'Maria', 'José']
notas = [8, 9, 10]


plt.bar(x = estudantes, height = notas)
plt.show()


estudantes2 = ['João', 'Maria', 'José', 'Ana']

from random import choice

estudante = choice(estudantes2)
print(estudante)


1) Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.

pip install matplotlib==3.7.1


2) Escreva um código para importar a biblioteca numpy com o alias np.

import numpy as np

3) Crie um programa que lê a seguinte lista de números e escolha um número desta aleatoriamente.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

import matplotlib.pyplot as plt
from random import choice

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

print(choice(lista))

4) Crie um programa que sorteia aleatoriamente um número inteiro menor que 100.

from random import *

print((randrange(100)))

5) Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

from math import pow

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = pow(n1,n2)
print(n3)   

6) Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes.

Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.

from random import *

participantes = int(input('Quantas pessoas participaram do sorteio? '))

print(randrange(participantes))

7) Você recebeu uma demanda para gerar números de token para o acesso ao aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.

"Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

from random import *

nome = input('Qual é o seu nome? ')
token = randrange(1000, 9999, 2)


print(f'Olá {nome}, o seu tokn de acesso é {token}! Seja bem-vindo(a)!')

8) Para diversificar e atrair novos clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente.

Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

from random import *

frutas = ["maçã", "banana", "uva", "pêra", 
"manga", "coco", "melancia", "mamão", "laranja", "abacaxi", "kiwi", "ameixa"]

surpresa = sample(frutas, 3)
print(surpresa)

9) Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:

numeros = [2, 8, 15, 23, 91, 112, 256]

from math import *

numeros = [2, 8, 15, 23, 91, 112, 256]

for numero in numeros:
    raiz = sqrt(numero)
    if raiz.is_integer():
        print(f"A raiz quadrada de {numero} é {int(raiz)} e é um número inteiro.")

10) Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.

Dica: use a variável pi e o método pow() da biblioteca math. O cálculo da área de um círculo é de: A = π*r^2 (lê-se pi vezes raio ao quadrado).

from math import *

raio = float(input('Qual é o raio em metros da área circular? '))
total = pi*(pow(raio, 2))
valor = 25*(total)

print(valor)
"""

