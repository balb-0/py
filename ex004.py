# 1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica, use as funções built-in sum() e len().

# gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
# somatorio = int(sum(gastos))
# tamanho = int(len(gastos))

# print(somatorio, tamanho)
# media = somatorio / tamanho
# print(f'a média é {media}')

# 2) Com os mesmos dados da questão anterior, defina quantas compras foram acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

# gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
# passou = 0


# for acima in gastos:
#     if acima > 3000:    
#         print(acima)
#         passou += 1

# porcentagem = (passou / len(gastos)) * 100

# print(f'foram {passou} compras acima de 3000 reais.')
# print(f'a porcentagem dos valores que passaram de 3000 foi de {porcentagem}%')


# 3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].

# contagem = 1
# lista = []

# for _ in range(5):
#     while contagem < 6:
#         numero = int(input('Digite um número: '))
#         lista.append(numero)
#         contagem += 1
        
# print(lista)

# 4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

# contagem = 1
# lista = []

# for _ in range(5):
#     while contagem < 6:
#         numero = int(input('Digite um número: '))
#         lista.append(numero)
#         contagem += 1
        
# reverse = list(reversed(lista))

# print(reverse)

# 5) Faça um programa que, ao inserir um número qualquer, criará uma lista contendo todos os números primos entre 1 e o número digitado.

# 6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é uma data válida para uma análise.

# Momento dos projetos
# 7) Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias multiplicadas por dia e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

# numero = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
# porcentagem = []

# for i in range(1, len(numero)):
#     crescimento = (numero[i] - numero[i-1])/numero[i-1]
#     porcentagem.append(crescimento)

# print(f'a porcentagem de crescimento por dia foi de {porcentagem}')


# 8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros, sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

'''
contagem = 1
lista_par = []
lista_impar = []

for i in range(10):
    i = int(input('Digite um número: '))
    if i%2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(f'A lista de IDs pares é {lista_par} e tem {len(lista_par)} itens')
print(f'A lista de IDs impares é {lista_impar} e tem {len(lista_impar)} itens')


9) Desenvolva um programa que informa a nota de um aluno de acordo com suas respostas. Ele deve pedir a resposta de um aluno para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem alternativas: A, B, C ou D.

resultado = []
gabarito = {
    '1': 'D',
    '2': 'A',
    '3': 'C',
    '4': 'B',
    '5': 'A',
    '6': 'D',
    '7': 'C',
    '8': 'C',
    '9': 'A',
    '10': 'B',
}


for i in range(1, 11):
    respostas = input(f'Digite a sua resposta para a questão {i}: ')
    resultado.append(respostas)
    
pontuacao = 0
for i in range(1, 11):
    if resultado[i - 1] == gabarito[f'{i:01d}']:
        pontuacao += 1

print(f"Sua pontuação final é: {pontuacao}")


10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram, mostrando os meses por extenso: Janeiro, Fevereiro, etc.


'''

