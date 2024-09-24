"""
Optimisation de l'algorithme brute force :
1) read_csv() : utilisation d'une compréhension de liste, transformer les nombres
2) Ecrire les deux fonctions find_all_combinations et get_target_combinations en une seule en utilisant
   lialgorithme de "Branch and Bound".
"""
import csv
import time
import timeit


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


# Function to calculate all possible combinations
def find_all_combinations(data, target):
    """
    Calculate all possible sub-lists combinations in the data list.

    :param data: The list whose possible sub-lists are to be calculated.
    :return: The list containing all sub-lists.
    """
    # Initialize the list of combinations
    all_combinations = [[]]

    for element in data:
        new_combinations = []

        for combination in all_combinations:
            new_combinations.append(combination)

            new_combination = combination + [element]

            new_combination_sum = sum(action[1] for action in new_combination)

            if new_combination_sum > target:
                continue
            new_combinations.append(new_combination)

        # Update the list of combinations
        all_combinations = new_combinations
    return all_combinations


if __name__ == "__main__":
    # Début de l'éxecution de l'algorithme
    #execution_time = timeit.timeit(test_function, number=100)
    #print(execution_time/100)
    start_time = time.time()
    data = read_csv("liste-actions.csv")
    all_combinations = find_all_combinations(data, 500)
    print(len(all_combinations))
    #print(f"Nomber of possible combinations is: {len(all_combinations)}\n{all_combinations[77]}")
    #combinations = get_target_combinations(all_combinations, 500)
    #combinations = calculate_profit_combination(combinations)
    #print(get_best_combination(combinations))
    #print(f"Combinaisons ciblée : {len(combinations)}")
    end_time = time.time()
    print(end_time - start_time)
    #print(f"Execution time read_csv : {end_time - start_time} seconds.")


