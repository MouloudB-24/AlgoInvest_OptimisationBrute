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


def get_target_combinations(target, all_combinations):
    combinations = []
    for combination in all_combinations:
        if sum(combination) == target:
            combinations.append(combination)
    return combinations


def calculate_profit(combinations):
    pass


if __name__ == "__main__":
    actions = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 38, 14, 18, 8, 4, 10, 24, 114]
    profit = [0.05, 0.1, 0.15, 0.2, 0.17, 0.25, 0.07, 0.11, 0.13, 0.27, 0.17, 0.09, 0.23, 0.01, 0.03, 0.08, 0.12, 0.14, 0.21]
    target = 500
    all_combinations = get_combinations(actions)
    print(f"Nomber of possible combinations is: {len(all_combinations)}")
