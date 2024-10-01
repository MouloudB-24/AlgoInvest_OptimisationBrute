"""
Optimisation de l'algorithme brute force :
1) read_csv() : utilisation d'une compréhension de liste, transformer les nombres
2) Utilisation de l'algorithme de sac à dos dynamique avec précision de 100
"""

import csv
from pathlib import Path
import time


# Function to retrieve data from a CSV file
def read_csv(file_name):
    """
    Retrieve data from a CSV file.

    :param file_name: Name file.
    :return: Data in list form.
    """
    folder = Path("data") / file_name
    with open(folder, "r", newline="", encoding="utf-8") as file:
        raw_data = csv.reader(file)
        next(raw_data)
        return [(row[0], float(row[1]), float(row[2])) for row in raw_data if float(row[1]) > 0]


def dynamic_algorithme(budget, shares, precision):
    budget = budget * precision
    shares = [(share[0], int(share[1] * precision), share[2], share[1] * share[2]/100) for share in shares]

    matrix = [[0 for _ in range(budget + 1)] for _ in range(len(shares) + 1)]

    for i_share in range(1, len(shares) + 1):
        for remaining_budget in range(1, budget + 1):
            share_price = shares[i_share - 1][1]
            share_profit = shares[i_share - 1][3]

            if share_price <= remaining_budget:
                matrix[i_share][remaining_budget] = max(
                    share_profit + matrix[i_share - 1][remaining_budget - share_price],
                    matrix[i_share - 1][remaining_budget])
            else:
                matrix[i_share][remaining_budget] = matrix[i_share - 1][remaining_budget]

    remaining_budget = budget
    n_shares = len(shares)
    selected_shares = []

    while remaining_budget >= 0 and n_shares >= 0:
        current_share = shares[n_shares - 1]
        share_price = current_share[1]
        share_profit = current_share[3]

        if matrix[n_shares][remaining_budget] == matrix[n_shares - 1][remaining_budget - share_price] + share_profit:
            selected_shares.append(current_share)
            remaining_budget -= share_price
        n_shares -= 1

    selected_shares = [(share[0], share[1] / precision, share[2]) for share in selected_shares]

    return sum([share[1] for share in selected_shares]), matrix[-1][-1], selected_shares


if __name__ == "__main__":
    budget = 500
    precision = 100
    shares = read_csv("dataset2.csv")
    start_time = time.time()
    cost, profit, best_combination = dynamic_algorithme(budget, shares, precision)
    end_time = time.time()
    print(f"Temps : {end_time-start_time} Secondes\nCoût : {cost}€\nBénéfice : {profit}€\nActions : {best_combination}")
