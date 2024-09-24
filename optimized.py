"""
Optimisation de l'algorithme brute force :
1) read_csv() : utilisation d'une compréhension de liste, transformer les nombres
2) Ecrire les deux fonctions find_all_combinations et get_target_combinations en une seule en utilisant
   l'algorithme de "Branch and Bound".
"""
import csv
import time


# Function to retrieve data from a CSV file
def read_csv(file_name):
    """
    Retrieve data from a CSV file.

    :param file_name: Name file.
    :return: Data in list form.
    """

    with open(file_name, "r", newline="", encoding="utf-8") as file:
        raw_data = csv.reader(file)
        next(raw_data)
        return [(row[0], int(row[1]), float(row[2].strip("%"))/100) for row in raw_data]


def sort_data(data, n):
    return sorted(data, key=lambda x: x[n], reverse=True)


# Function to calculate all possible combinations
def find_target_combinations(data, target):
    """
    Calculate all possible sub-lists combinations in the data list.

    :param data: The list whose possible sub-lists are to be calculated.
    :return: The list containing all sub-lists.
    """
    # Trier les actions par ordre décroissant
    data = sort_data(data, 1)

    # Initialize the list of combinations
    combinations = []

    # pile
    possible_combinations = [(0, 0, [])]

    while possible_combinations:
        index, current_sum, current_combination = possible_combinations.pop()

        if current_sum == target:
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
    return combinations


# Function to calculate profit for each combination
def get_best_combination(combinations):
    """
    Calculates profit for each combination.

    :param target_combinations: The list of the combinations.
    :return: The list of combinations with profits.
    """
    best_combination = []
    best_profit = 0
    for combination in combinations:
        profit = 0
        for action in combination:
            profit += action[1] * action[2]
        if profit > best_profit:
            best_profit = profit
            best_combination = combination
    return f"The best combination : {best_combination}\nThe best profit: {best_profit}€"


if __name__ == "__main__":
    # Début de l'éxecution de l'algorithme
    start_time = time.time()
    data = read_csv("liste-actions.csv")
    combinations = find_target_combinations(data, 500)
    combination = get_best_combination(combinations)
    end_time = time.time()
    print(end_time - start_time)
    print(combination)


