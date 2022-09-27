import csv
from math import sqrt

CAMINHO_ARQUIVO_CSV = './Stores_edited.csv'


def arredondar_duas_casas(numero):
    return round(numero, 2)


def pegar_menor_valor_lista(lista_de_itens):
    # Retorna o menor valor da lista
    return arredondar_duas_casas(min(lista_de_itens))


def pegar_maior_valor_lista(lista_de_itens):
    # Retorna o maior valor da lista
    return arredondar_duas_casas(max(lista_de_itens))


def pegar_valor_medio_lista(lista_de_itens):
    # Retorna o valor médio da lista
    media = float(sum(lista_de_itens) / len(lista_de_itens))

    return arredondar_duas_casas(media)


def pegr_quadrado_numero(num):
    return pow(num, 2)


def pegar_desvio_padrao_lista(items):
    # Retorna o valor do desvio padrao da lista
    tamanho = len(items)
    media = pegar_valor_medio_lista(items)

    soma = 0
    for item in items:
        soma += pegr_quadrado_numero(item - media)

    desvio_padrao = sqrt(soma / (tamanho - 1))

    return arredondar_duas_casas(desvio_padrao)


def ler_arquivo_csv():
    # le e processa os dados do arquivo
    with open(CAMINHO_ARQUIVO_CSV, newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=',')

        lista = []

        for indice, linha in enumerate(leitor_csv):
            if indice > 0:
                lista.append(linha)

        return lista


def mostrar_valores_formatados(
        nome_lista,
        media,
        menor_valor_da_lista,
        maior_valor_da_lista,
        desvio_padrao):
    # Imprime as mensages com os valores formatados
    print(f"- O valor médio de '{nome_lista}' é: {media}")
    print(f"- O valor mínimo de '{nome_lista}' é: {menor_valor_da_lista}")
    print(f"- O valor máximo de '{nome_lista}' é: {maior_valor_da_lista}")
    print(f"- O desvio padrão de '{nome_lista}' é: {desvio_padrao}\n")


if(__name__ == "__main__"):
    print("\n## Desempenho das lojas\n")

    # Lista os elementos do arquivo .csv
    lista = ler_arquivo_csv()

    # Separa os items em 3 listas
    lista_itens_disponiveis = []
    lista_visitas_diarias = []
    lista_vendas = []

    # popula os items nas respectivas listas
    for linha in lista:
        lista_itens_disponiveis.append(float(linha[2]))
        lista_visitas_diarias.append(float(linha[3]))
        lista_vendas.append(float(linha[4]))

    # Para cada lista, calcula os valores de média, máx, min e desvio padrao
    valor_medio_itens = pegar_valor_medio_lista(lista_itens_disponiveis)
    valor_min_itens = pegar_menor_valor_lista(lista_itens_disponiveis)
    valor_max_itens = pegar_maior_valor_lista(lista_visitas_diarias)
    desv_pad_itens = pegar_desvio_padrao_lista(lista_visitas_diarias)

    # Mostra os dados formatados
    mostrar_valores_formatados(
        "Produtos",
        valor_medio_itens,
        valor_min_itens,
        valor_max_itens,
        desv_pad_itens
    )

    valor_medio_visitas = pegar_valor_medio_lista(lista_visitas_diarias)
    valor_min_visitas = pegar_menor_valor_lista(lista_visitas_diarias)
    valor_max_visitas = pegar_maior_valor_lista(lista_visitas_diarias)
    desv_pad_visitas = pegar_desvio_padrao_lista(lista_visitas_diarias)

    mostrar_valores_formatados(
        "Visitas",
        valor_medio_visitas,
        valor_min_visitas,
        valor_max_visitas,
        desv_pad_visitas
    )

    valor_medio_vendas = pegar_valor_medio_lista(lista_vendas)
    valor_min_vendas = pegar_menor_valor_lista(lista_vendas)
    valor_max_vendas = pegar_maior_valor_lista(lista_vendas)
    desv_pad_vendas = pegar_desvio_padrao_lista(lista_vendas)

    mostrar_valores_formatados(
        "Vendas",
        valor_medio_vendas,
        valor_max_vendas,
        valor_min_vendas,
        desv_pad_vendas
    )
