# Exercícios de Python para hoje.
# Cada exercício é um programa que iremos escrever.

'''1. Programa de boas-vindas
     (a) Mostre uma mensagem de boas vindas na tela 
     (b) Pergunte o nome do usuário e dê boas vindas com o nome fornecido
'''
print('Bem Vindo!')

print('Qual o seu nome?')
nome = input()
print(f'Olá, {nome}! Bem-vindo ao meu programa !' )

'''# 2. Programa "calculadora" (com operações fixas por enquanto).
Peça a entrada de dois números.
    (a) Mostre a soma entre os números fornecidos
    (b) Mostre outras três operações à sua escolha
'''
x = int(input(' Qual o Valor de X = '))
y = int(input(' Qual o Valor de Y = '))

print('A soma de x+y= ',x+y)
print('A multiplicação x*y= ',x*y)
print('A divisão de x/y= ',x/y)
print('A subtração de x-y= ',x-y)


'''3. Conversão de anos em meses e dias.
Peça ao usuário que digite uma quantidade de anos.
(Pode ser a idade do usuário, se quiser)
    (a) Mostre esse tempo em meses
    (b) Mostre esse tempo em dias
'''
print('Qual a sua idade em anos?')

temp_anos = int(input())
print(temp_anos, 'anos equivalente a:')

tempo_meses = temp_anos*12
print(tempo_meses, 'meses')

tempo_dias = temp_anos*365
print(tempo_dias, 'dias')

'''4. Mostrar o tamanho de um texo.
Peça ao usuário que digite seu nome.
Informe quantas letras tem o nome fornecido.
(Para isso usaremos o comando "len" -- pergunte ao prof!)
'''

print('Qual seu nome?')
nome = input()
print('Número de letras nesse nome :' ,len(nome))


'''5. Conversão de temperatura.
    (a) Pergunte a temperatura em Fahrenheit;
        Mostre o valor da temperatura em Celsius
    (b) Pergunte a temperatura em Celsius;
        Mostre o valor a temperatura em Fahrenheit.

(Pesquise a fórmula de conversão!)
'''

print('Qual a temperatura em Fahrenheint ?')
TempEmFahrenheit = int(input())
Conv_F_para_C = ((TempEmFahrenheit-32)*5/9)



''' 6. Cálculo de área e valor.
    (a) Peça ao usuário que informe comprimento e largura
    de um terreno retangular.

    Informe a área total do terreno.

    (b) Peça ao usuário que informe o preço total do terreno.
    Calcule e mostre qual o preço por metro quadrado.
'''