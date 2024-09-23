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

--> Parcouris toutes les combinaisons trouvée, garder uniquement celles dont la valeur == 500€

--> Claculer pour chaque combinaison les bénéfices en mutipliant par le pourcentage %

--> Comparer les bénéfices en choisissant la meilleure combinaisons d'actions
"""
import csv


# Récupérer les données : fichier csv
def read_csv(file_name):
    data = []
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        raw_data = csv.reader(file)

        for row in raw_data:
            percentage = row[2].strip("%")
            data.append([row[0], row[1], percentage])
    # Supprimer la ligne des entêtes
    data.pop(0)
    return data


# Utilisation de l'algorithme Powerset
def get_combinations(data):
    # Initialise la liste des combinaisons avec un combinaison vide
    all_combinations = [[]]

    for element in data:
        # Créer une nouvelle liste pour stocker les combinaisons générées
        new_combinations = []

        for combination in all_combinations:
            # On ajoute uniqument la combinaisons
            new_combinations.append(combination)

            # On ajoute la combinaison + l'élément actuel
            new_combinations.append(combination + [element])

        # Mettre à jour les combinaisons pour inclure les nouvelles combinaisons générées
        all_combinations = new_combinations

    return all_combinations


def get_target_combinations(all_combinations, target):
    combinations = []
    for combination in all_combinations:
        current_target = 0
        for action in combination:
            current_target += int(action[1])
        if current_target == target:
            combinations.append(combination)
    return combinations


# Cacluler le bénéfice pour chaque action
def calculate_profit_per_action(combinations):
    profit_per_combinations = []
    for combination in combinations:
        new_combination = []
        for action in combination:
            profit = int(action[1]) * int(action[2]) / 100
            new_combination.append([action[0], profit])
        profit_per_combinations.append(new_combination)
    return profit_per_combinations

# Obtenir la meilleire combinaisons d'actions
def get_best_combination(combinations):
    best_profit = 0
    best_combination = []
    for combination in combinations:
        profit = 0
        for action in combination:
            profit += action[1]
        if profit > best_profit:
            best_profit = profit
            best_combination = combination
    return f"The best combination : {best_combination}\nThe best profit: {best_profit}€"



if __name__ == "__main__":
    data = read_csv("liste-actions.csv")
    all_combinations = get_combinations(data)
    #print(f"Nomber of possible combinations is: {len(all_combinations)}\n{all_combinations[77]}")
    combinations = get_target_combinations(all_combinations, 500)
    #print(f"Combinaisons ciblée : {len(combinations)}")
    #print(f"Les données : {data}")
    profit_per_combinations = calculate_profit_per_action(combinations)
    #print(f"Les combinaisons avec le bénéfice: {profit_per_combinations}")
    best_combination = get_best_combination(profit_per_combinations)
    print(best_combination)
