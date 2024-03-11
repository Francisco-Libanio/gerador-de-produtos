from random import randint

quantidade = 97
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

for i in range(quantidade):
    nome_completo = ()
    nome = tipo[randint(0, 26)]
    nome_completo += (nome,)
    marca = Marca[randint(0, 34)]
    nome_completo += (marca,)
    variacao = Tamanho[randint(0, 7)]
    nome_completo += (variacao,)

    nome_completo_str = ' '.join(nome_completo)

    if nome_completo_str not in combinacoes_geradas:
        lista_de_nomes.append(nome_completo)
        combinacoes_geradas.add(nome_completo_str)


resultados = [' '.join(item) for item in lista_de_nomes]

for i in resultados:
    print(i)
