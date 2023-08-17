notas = {
    '1T': 8.5,
    '2T': 9.5,
    '3T': 7,
}

soma = 0

for nota in notas.values():
    soma += nota

print(soma)

somatorio = sum(notas.values())

print(somatorio)

qtd_notas = len(notas)

media = somatorio/qtd_notas

media = round(media, 1)

print(media)
