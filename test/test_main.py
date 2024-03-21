from main import gerador_de_produto
from random import seed


def testa_geração_de_produto():
    seed(1)  # Configura a semente para reproduzir os mesmos resultados

    gerador = gerador_de_produto(5)  # Quantidade pequena para facilitar o teste

    # Verifica se a quantidade de combinações geradas está correta
    assert len(gerador) == 10

