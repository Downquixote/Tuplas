lanche = ('Burguer', 'Refri', 'Batata', 'Sorvete')
# TUPLAS são IMUTÁVEIS

# Para mostrar apenas o primeiro valor da variável
print(lanche[1])
# Para mostrar o valor da variável da direita para a esquerda
print(lanche[-2])
# Para mostrar a partir do valor da variável desejado até outro valor escolhido 
print(lanche[1:3])
# Para declarar o primeiro valor a ser mostrado até o valor escolhido
print(lanche[:3])
# Para mostrar do primeiro valor da variável até o valor escolhido
print(lanche[1:])
# Para mostrar todos os valores da variável
print(lanche)


'''Comando errado nas TUPLAS

lanche[1] = "Suco"

Lembre-se que TUPLAS SÃO IMUTÁVEIS'''

print()
print('=' * 30)
print()

# Exemplo com FOR
for comida in lanche:
    print(f'Eu vou comer {comida}!')
print('Comi demais!')

print()
print('=' * 30)
print()

# Exemplo de uma maneira de utilizar o FOR (se eu precisar da posição)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi demais!')

print()
print('=' * 30)
print()

# Exemplo da mesma maneira acima, só que mais complexa
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi demais!')

print()
print('=' * 30)
print()

# Para organizar os valores em ordem
print(sorted(lanche))
print(lanche)

print()
print('=' * 30)
print()

# Para juntar duas variáveis com diversos valores
a = (6, 4, 3, 7)
b = (5, 7, 2, 4, 1)
c = a + b
print(c)