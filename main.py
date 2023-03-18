#  12,83%  CDB ANO -- 18/03

valor_cdb = 12.83

valor = input('Quantos de dinheiro ira inverstir? ')
investimento = input('Quantos % do CDB? ')
tempo = input('Quantos tempo ira deixar o dinheiro? (Em meses) ')

juros = valor_cdb * int(investimento) // 100
porcentagem = (juros // 12) * int(tempo)

lucro = (int(valor) * porcentagem) // 100

print(f'\nVoce tera o valor total de R${lucro + int(valor)} após {tempo} Meses.')
print(f'O lucro seria de: R${lucro}')

#  github.com/LeonardoAlberto
#  S2
