'''Desenvolva um programa que leia QUATRO VALORES pelo TECLADO e guarde-os em uma TUPLA.
No final, mostre: 
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números PARES'''

a = (int(input('Digite o 1º valor: ')),
    int(input('Digite o 2º valor: ')),
    int(input('Digite o 3º valor: ')),
    int(input('Digite o 4º valor: ')))
print('-' * 30)
print(f'Quantidade de vezes que o número NOVE foi digitado: {a.count(9)}')
if 3 in a:
    print(f'Posição do número TRÊS: {a.index(3) + 1}ª posição')
else:
    print('O número TRÊS não foi digitado.')
print(f'Os valores PARES digitados foram:', end=' ')
for n in a:
    if n % 2 == 0:
        print(n, end=' ')