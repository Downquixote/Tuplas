'''Crie um programa que tenha uma TUPLA única com NOMES DE PRODUTOS e seus respectivos PREÇOS, na sequência.
No final, mostre uma listagem de preços organizando os dados em forma TABULAR.'''
lista = ('Playstation 5', 3.500, 
        'Xbox Series X', 4.000,
        'Civic 2015', 70.000,
        'Golf TSI', 75.000)
print('-' * 40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else: 
        print(f'R${lista[pos]:>7.3f}')
print('-' * 40)