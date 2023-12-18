#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
from time import sleep
print('-'*60)
cor = {'limpa':'\033[m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'amarelo':'\033[33m',
       'ciano':'\033[36m'}
n = int(input('Digite um número inteiro: '))

print('ESCOLHA UMA DAS OPÇÕES ABAIXO: ')
print('-'*60)
sleep(1)
print('''{}[1] CONVERTER PARA BINÁRIO{} 
{}[2] CONVERTER PARA OCTA{}
{}[3] CONVERTER PARA HEXADECIMAL{}
{}[4] SAIR{}'''.format(cor ['ciano'],cor['limpa'], cor ['verde'], cor['limpa'], cor ['amarelo'], cor ['limpa'], cor ['vermelho'], cor ['limpa']))
print('-'*60)
sel = int(input('Digite a opção que você deseja: '))
if sel == 1:
    print('{} convertindo em Binário é {}'.format(n, bin(n)[2:]))
elif sel == 2: 
    print('{} convertido em Octa é {}'.format(n, oct(n)[2:]))
elif sel == 3:
    print('{} convertido em Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inexistente!')
print('-'*60)
print('Programa finalizado!')
print('-'*60)
input('')