import csv
from math import sqrt

CSV_FILE_PATH = './Stores_edited.csv'


def min_of(items):
    # Retorna o menor valor da lista
    return min(items)


def max_of(items):
    # Retorna o maior valor da lista
    return max(items)


def average_of(items):
    # Retorna o valor médio da lista
    average = float(sum(items) / len(items))
    return round(average, 2)


def get_std_deviation_of(items):
    # Retorna o valor do desvio padrao da lista
    len_of = len(items)
    average = average_of(items)

    dist_avg = 0
    for item in items:
        dist_avg += pow((item - average), 2)

    std_dev = sqrt(dist_avg / (len_of - 1))

    return round(std_dev, 2)


def split_csv_file():
    # le e processa os dados do arquivo
    with open(CSV_FILE_PATH, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        items = []

        for index, row in enumerate(csv_reader):
            if index > 0:
                items.append(row)

        return items


def show_formatted_data(name, media, menor_valor_da_lista, maior_valor_da_lista, desvio_padrao):
    # Imprime as mensages com os valores formatados
    print(f"- O valor médio de {name} é: {media}")
    print(f"- O valor mínimo de {name} é: {menor_valor_da_lista}")
    print(f"- O valor máximo de {name} é: {maior_valor_da_lista}")
    print(f"- O desvio padrão de {name} é: {desvio_padrao}\n")


if(__name__ == "__main__"):
    print("\n## Desempenho das lojas\n")

    # Lista os elementos do arquivo .csv
    items = split_csv_file()

    # Separa os items em 3 listas
    available_items = []
    daily_visits = []
    store_sales = []

    # popula os items nas respectivas listas
    for line in items:
        available_items.append(float(line[2]))
        daily_visits.append(float(line[3]))
        store_sales.append(float(line[4]))

    # Para cada lista, calcula os valores de média, máx, min e desvio padrao
    average_av_items = average_of(available_items)
    min_of_av_items = min_of(available_items)
    max_of_av_items = max_of(daily_visits)
    std_dev_of_av_items = get_std_deviation_of(daily_visits)

    # Mostra os dados formatados
    show_formatted_data(
        "Produtos",
        average_av_items,
        min_of_av_items,
        max_of_av_items,
        std_dev_of_av_items
    )

    average_daily_visits = average_of(daily_visits)
    min_of_daily_visits = min_of(daily_visits)
    max_of_daily_visits = max_of(daily_visits)
    std_dev_of_daily_visits = get_std_deviation_of(daily_visits)

    show_formatted_data(
        "Visitas",
        average_daily_visits,
        min_of_daily_visits,
        max_of_daily_visits,
        std_dev_of_daily_visits
    )

    average_store_sales = average_of(store_sales)
    min_of_store_sales = min_of(store_sales)
    max_of_store_sales = max_of(store_sales)
    std_dev_of_store_sales = get_std_deviation_of(store_sales)

    show_formatted_data(
        "Vendas",
        average_store_sales,
        min_of_store_sales,
        max_of_store_sales,
        std_dev_of_store_sales
    )
