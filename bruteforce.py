"""
un algorithme qui maximise le profit realisé par un client après 2 ans d'invertissement.
suggérer les actions plus rentables à acheter.

Contraintes :
1) Une action ne peut être achetée q'une fois
2) Pas d'achat d'une fraction d'une action
3) 500€ de dépense max par client

Le programme :
- essaie toutes les différentes combinaisons d'actions, et choisisse la meilleure.
- Lire le fichier contenant des informations sur les actions.

Données d'entrée :
 --> Liste actions (fichier cvs)
 --> cible = 500€

Objectif :
--> Trouver toutes les combinaisons possibles d'actions dont la valeur == 500€

Stratégie :
--> Trouver toutes les combinaisons possible dans la liste d'actions.

--> Parcouris toutes les combinaisons trouvée, garder uniquement celles dont la valeur <= 500€

--> Claculer pour chaque combinaison les bénéfices en mutipliant par le pourcentage %

--> Comparer les bénéfices en choisissant la meilleure combinaisons d'actions
"""
import csv
import time
from pathlib import Path


# Function to retrieve data from a CSV file
def read_csv(file_name):
    """
    Retrieve data from a CSV file.

    :param file_name: Name file.
    :return: Data in list form.
    """
    shares = []
    folder = Path("data") / file_name
    with open(folder, "r", newline="", encoding="utf-8") as file:
        raw_data = csv.reader(file)

        for row in raw_data:
            percentage = row[2].strip("%")
            shares.append([row[0], row[1], percentage])

    # Delete headers
    shares.pop(0)
    return shares


# Function to calculate all possible combinations
def brute_force_algorithm(shares):
    """
    Calculate all possible sub-lists combinations in the data list.

    :param shares: The list whose possible sub-lists are to be calculated.
    :return: The list containing all sub-lists.
    """
    # Initialize the list of combinations
    all_combinations = [[]]

    for element in shares:
        new_combinations = []

        for combination in all_combinations:
            new_combinations.append(combination)
            new_combinations.append(combination + [element])

        # Update the list of combinations
        all_combinations = new_combinations
    return all_combinations


# Function to calculate all target combinations
def get_target_combinations(all_combinations, budget):
    """
    Obtain the target combinations from the list of all possible combinations.

    :param all_combinations: The list of th all possible combinations.
    :param budget: The target of the combinations chosen, which represents a sum.
    :return: The list containing the target combinations
    """
    target_combinations = []
    for combination in all_combinations:
        current_target = 0
        for share in combination:
            current_target += int(share[1])
            if current_target > budget:
                break
        if current_target <= budget:
            target_combinations.append(combination)
    return target_combinations


# Function to calculate profit for each combination
def calculate_profit_combination(target_combinations):
    """
    Calculates profit for each combination.

    :param target_combinations: The list of the combinations.
    :return: The list of combinations with profits.
    """
    profit_combinations = []
    for combination in target_combinations:
        new_combination = []
        for share in combination:
            new_combination.append((share[0], int(share[1]), int(share[1]) * int(share[2]) / 100))
        profit_combinations.append(new_combination)
    return profit_combinations


# Function to obtain the best combinations of actions
def get_best_combination(combinations):
    """
    Get the best combination of action.

    :param combinations: The list of the combinations.
    :return: The best combinations if action list and benefits
    """
    cost = 0
    profit = 0
    best_combination = []
    for combination in combinations:
        current_cost = 0
        current_profit = 0
        for share in combination:
            current_cost += share[1]
            current_profit += share[2]
        if current_profit > profit:
            profit = current_profit
            cost = current_cost
            best_combination = combination
    return cost, profit, best_combination


if __name__ == "__main__":
    start_time = time.time()
    data = read_csv("actions.csv")
    all_combinations = brute_force_algorithm(data)
    combinations = get_target_combinations(all_combinations, 500)
    profit_per_combinations = calculate_profit_combination(combinations)
    cost, profit, best_combination = get_best_combination(profit_per_combinations)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds.")
    print(f"Coût : {cost}€\nBénéfice : {profit}€\nActions : {best_combination}")

