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
--> Trouver toutes les combinaisons de liste possible dans la liste d'actions.

--> Parcouris toutes les combinaisons trouvée, garder uniquement celles dont la valeur <= 500€

--> Claculer pour chaque combinaison les bénéfices en mutipliant par le pourcentage %

--> Comparer les bénéfices en choisissant la meilleure combinaisons d'actions
"""
import csv
import time
from pathlib import Path
from tqdm import tqdm
from memory_profiler import profile


# Function to retrieve data from a CSV file
#@profile
def read_csv(file_name):
    """
    Retrieve data from a CSV file.

    :param file_name: Name file.
    :return: Data in list form.
    """
    data = []
    folder = Path("data") / file_name
    with open(folder, "r", newline="", encoding="utf-8") as file:
        raw_data = csv.reader(file)

        for row in tqdm(raw_data, desc="Reading CSV data"):
            percentage = row[2].strip("%")
            data.append([row[0], row[1], percentage])

    # Delete headers
    data.pop(0)
    return data


# Function to calculate all possible combinations
#@profile
def find_all_combinations(data):
    """
    Calculate all possible sub-lists combinations in the data list.

    :param data: The list whose possible sub-lists are to be calculated.
    :return: The list containing all sub-lists.
    """
    # Initialize the list of combinations
    all_combinations = [[]]

    for element in tqdm(data, desc="Generating all combinations"):
        new_combinations = []

        for combination in all_combinations:
            new_combinations.append(combination)
            new_combinations.append(combination + [element])

        # Update the list of combinations
        all_combinations = new_combinations
    return all_combinations


# Function to calculate all target combinations
#@profile
def get_target_combinations(all_combinations, target):
    """
    Obtain the target combinations from the list of all possible combinations.

    :param all_combinations: The list of th all possible combinations.
    :param target: The target of the combinations chosen, which represents a sum.
    :return: The list containing the target combinations
    """
    target_combinations = []
    for combination in tqdm(all_combinations, desc="Obtain target combinations"):
        current_target = 0
        for action in combination:
            current_target += int(action[1])
            if current_target > target:
                break
        if current_target <= target:
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
    for combination in tqdm(target_combinations, desc="Calculating profits"):
        new_combination = []
        for action in combination:
            new_combination.append((action[0], int(action[1]), int(action[1]) * int(action[2]) / 100))
        profit_combinations.append(new_combination)
    return profit_combinations


# Function to obtain the best combinations of actions
def get_best_combination(combinations):
    """
    Get the best combination of action.

    :param combinations: The list of the combinations.
    :return: The best combinations if action list and benefits
    """
    best_cost = 0
    best_profit = 0
    best_combination = []
    for combination in tqdm(combinations, desc="Finding the best combination"):
        profit = 0
        cost = 0
        for action in combination:
            cost += action[1]
            profit += action[2]
        if profit > best_profit:
            best_profit = profit
            best_cost = cost
            best_combination = combination
    return f"The best cost: {best_cost}€\nThe best profit: {best_profit}€\nThe best combination : {best_combination}"


if __name__ == "__main__":
    # Début de l'éxecution de l'algorithme
    start_time = time.time()
    data = read_csv("actions.csv")
    all_combinations = find_all_combinations(data)
    #print(f"Nomber of possible combinations is: {len(all_combinations)}\n{all_combinations[77]}")
    combinations = get_target_combinations(all_combinations, 500)
    #print(f"Combinaisons ciblée : {len(combinations)}")
    #print(f"Les données : {data}")
    profit_per_combinations = calculate_profit_combination(combinations)
    #print(f"Les combinaisons avec le bénéfice: {profit_per_combinations}")
    best_combination = get_best_combination(profit_per_combinations)
    # Début de l'éxecution de l'algorithme
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds.")
    print(best_combination)
