from random import randint

import pandas as pd
from sqlalchemy import create_engine


lista_de_nomes = []
tipo = [
    'Camiseta',
    'Bermuda',
    'Saia',
    'Regata',
    'Vestido',
    'Calça',
    'Shorts',
    'Blusa',
    'Moleton',
    'Casaco',
    'moletinho',
    'Blazer',
    'Blusa de lã',
    'Camisola',
    'Jaqueta',
    'Kimono',
    'Luva',
    'Maio',
    'Sunga',
    'Mini-saia',
    'Meia',
    'Poncho',
    'Regata',
    'Cardigã',
    'Maga Longa',
    'T-Shirt',
    'Legging',
]

Marca = [
    'Balenciaga',
    'Gucci',
    'Louis Vuitton',
    'Prada',
    'Valentino',
    'Dior',
    'Moncler',
    'Bottega Veneta',
    'Fendi',
    'Miu Miu',
    'Off-White',
    'Burberry',
    ' Loewe',
    'Versace',
    'Diesel',
    'Rick Owens',
    'Adidas',
    'Saint Laurent',
    'Nike',
    'Alexander McQueen',
    'Pacalolo',
    'LiuLiu',
    'Fiorucci',
    'Bad boy',
    'Converse',
    'Zoomp',
    'Fido Dido',
    'Benetton',
    'Company',
    'Cantão',
    'Forum',
    'Hang Loose',
    'Redley',
    'M.Officer',
    'Keds',
]
Tamanho = ['PP', 'P', 'M', 'G', 'GG', 'EXG', '2XX', '3XX']

combinacoes_geradas = set()


def gerador_de_produto(quantidade):
    for i in range(quantidade):
        nome_completo = ()
        nome = tipo[randint(0, 26)]
        nome_completo += (nome,)
        marca = Marca[randint(0, 34)]
        nome_completo += (marca,)
        variacao = Tamanho[randint(0, 7)]
        nome_completo += (variacao,)

        combinacoes_geradas.add(nome_completo)

    return combinacoes_geradas


estoque = gerador_de_produto(5)
print(estoque)
# breakpoint()

dataframe = pd.DataFrame(estoque, columns=['Nome', 'Marca', 'Variação'])

conexao_str = 'sqlite:///base.db'
engine = create_engine(conexao_str)

# Enviar o DataFrame para o banco de dados SQLite
dataframe.to_sql('produtos', con=engine, if_exists='replace', index=False)

print('DataFrame enviado para o banco de dados com sucesso!')
