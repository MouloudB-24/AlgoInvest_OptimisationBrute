"""
Optimisation de l'algorithme brute force :
1) read_csv() : utilisation d'une compréhension de liste, transformer les nombres
2) Ecrire les deux fonctions find_all_combinations et get_target_combinations en une seule en utilisant
   l'algorithme de "Branch and Bound".
"""
import csv
import time
from pathlib import Path
from tqdm import tqdm


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
        return [(row[0], float(row[1]), float(row[2].strip("%"))/100) for row in tqdm(raw_data, desc="Reading CSV data")]


# Function to calculate all possible combinations, using the Branch and Bound algorithm
def find_target_combinations(data, target):
    """
    Calculate the sub-lists target combinations in the data list.

    :param data: The list whose possible sub-lists are to be calculated.
    :param target: The target of the combinations chosen, which represents a sum.
    :return: The list containing the sub-lists.
    """
    # Trier les actions par ordre décroissant
    data = sort_data(data, 1)

    # Initialize the list of combinations
    combinations = []

    # pile
    possible_combinations = [(0, 0, [])]

    with tqdm(total=0, desc="Generating target combinations", unit="iteration") as pbar:
        while possible_combinations:
            index, current_sum, current_combination = possible_combinations.pop()

            if current_sum <= target:
                combinations.append(current_combination)

            if index < len(data):
                current_action = data[index]
                current_action_price = data[index][1]

                remaining_sum = sum([action[1] for action in data[index:]])

                # Couper les branches ou la somme totale est < target
                if current_sum + remaining_sum >= target:
                    possible_combinations.append((index+1, current_sum, current_combination))

                    # Couper la branche dès que la somme dépasse target
                    if current_sum + current_action_price <= target:
                        possible_combinations.append((index+1, current_sum + current_action_price, current_combination + [current_action]))
            pbar.update(1)

        return combinations


# Function to calculate profit for each combination
def get_best_combination(combinations):
    """
    Calculates the best combination.

    :param combinations: The list of the combinations.
    :return: The best combinations with his profit.
    """
    best_combination = []
    best_profit = 0
    for combination in tqdm(combinations, desc="Finding the best combination"):
        profit = 0
        for action in combination:
            profit += action[1] * action[2]
        if profit > best_profit:
            best_profit = profit
            best_combination = combination
    return f"The best combination : {best_combination}\nThe best profit: {best_profit}€"


def sort_data(data, n):
    """
    Sort data.
    :param data: The list of data to be sorted.
    :param n: Index of sort element.
    :return: The sorted list.
    """
    return sorted(data, key=lambda x: x[n], reverse=True)


if __name__ == "__main__":
    # Début de l'éxecution de l'algorithme
    start_time = time.time()
    data = read_csv("actions.csv")
    combinations = find_target_combinations(data, 500)
    combination = get_best_combination(combinations)
    end_time = time.time()
    print(end_time - start_time)
    print(combination)


