'''Crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma TUPLA.
Depois disso, mostre a LISTAGEM DE NÚMEROS gerados e também indique o MENOR e o MAIOR valor que estão na TUPLA.'''
from random import sample
n = sample(range(11), 5)
print(n)
print(f'''
O maior valor: {max(n)}
O menor valor: {min(n)}''')
