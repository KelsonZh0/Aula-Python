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