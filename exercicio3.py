import csv
from itertools import product
from math import sqrt

CSV_FILE_PATH = './Stores_edited.csv'


def get_standard_deviation_of(list):
    return 0


def min_of(items):
    return min(items)


def max_of(items):
    return max(items)


def average_of(items):
    return float(sum(items) / len(items))


def get_std_deviation_built_in_lib(items):
    # import statistics
    # return statistics.stdev(items)
    return None


def get_std_deviation_of(items):
    len_of = len(items)
    average = average_of(items)

    dist_avg = 0
    for item in items:
        dist_avg += pow((item - average), 2)

    std_dev = sqrt(dist_avg / (len_of - 1))

    return std_dev


def split_csv_file():
    with open(CSV_FILE_PATH, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        items = []

        for index, row in enumerate(csv_reader):
            if index > 0:
                items.append(row)
        return items


def show_formatted_data(name, avg, min_of, max_of, std_dev):
    print(f"- O valor médio de {name} é: {avg}")
    print(f"- O valor mínimo de {name} é: {min_of}")
    print(f"- O valor máximo de {name} é: {max_of}")
    print(f"- O desvio padrão de {name} é: {std_dev}\n")


if(__name__ == "__main__"):
    print("\n## Desempenho das lojas\n")

    items = split_csv_file()

    available_items = []
    daily_visits = []
    store_sales = []

    for line in items:
        available_items.append(float(line[2]))
        daily_visits.append(float(line[3]))
        store_sales.append(float(line[4]))

    average_av_items = average_of(available_items)
    min_of_av_items = min_of(available_items)
    max_of_av_items = max_of(daily_visits)
    std_dev_of_av_items = get_std_deviation_of(daily_visits)

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


# https://pt.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step
