'''Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por EXTENSO.'''
ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

n = int(input('Digite um valor entre 0 e 20: '))
if n < 0:
    print('Ops... Tente novamente: ')
    n = int(input('Digite um valor entre 0 e 20: '))
elif n > 20:
    print('Ops... Tente novamente: ')
    n = int(input('Digite um valor entre 0 e 20: '))
print(f'Você digitou o número {ext[n]}')