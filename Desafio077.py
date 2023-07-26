'''Crie um programa que tenha uma TUPLA com VÁRIAS PALAVRAS(não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas VOGAIS.'''
palavras = ('Aprender', 'Python', 'Programacao', 
            'Desenvolvedor', 'Trabalho', 'Curso')
for p in palavras:
    print(f'\nNa palavra {p.upper()}:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
