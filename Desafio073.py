'''Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da tabela do CAMPEONATO BRASILEIRO DE FUTEBOL.
Na ordem de colocação, depois mostre:
A) Apenas os 5 PRIMEIROS colocados.
B) Os ÚLTIMOS 4 colocados da tabela.
C) Uma lista com os TIMES EM ORDEM ALFABÉTICA.
D) Em que POSIÇÃO na tabela está o TIME da CUIABÁ.'''

times = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Atlético-PR', 'São Paulo', 'Fluminense', 'Bragantino', 'Fortaleza', 'Internacional', 'Cruzeiro', 'Cuiabá', 'Atlético-MG', 'Santos', 'Corinthians', 'Goiás', 'Bahia', 'Coritiba', 'América-MG', 'Vasco da Gama')

print('{:^40}'.format('BRASILEIRÃO 2023'))
print('-' * 40)
print()
print(f'Os times em ordem de colocada: {times}')
print('=' * 40)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print('=' * 40)
print(f'Os últimos 4 colocados: {times[-4:]} ')
print('=' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 40)
print(f'O Cuiabá está na {times.index("Cuiabá") + 1}º Posição.')