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

--> Parcouris toutes les combinaisons trouvée, garder celles dont la valeur == 500€

--> Claculer pour chaque combinaison les bénéfices en mutipliant par le %

--> Comparer les bénéfices en choisissant la meilleure combinaisons d'actions
"""


# Utilisation de l'algorithme Powerset
def get_combinations(target, actions):
    result = []

    # Initialise la liste des combinaisons avec un combinaison vide
    combinations = [[]]

    for action in actions:
        # Créer une nouvelle liste pour stocker les combinaisons générées
        new_combinations = []

        for combination in combinations:
            # On ajoute uniqument la combinaisons
            new_combinations.append(combination)

            # On ajoute la combinaison + l'élément actuel
            new_combinations.append(combination + [action])

        # Mettre à jour les combinaisons pour inclure les nouvelles
        combinations = new_combinations

    for combination in combinations:
        if sum(combination) == target:
            result.append(combination)

    return result


def calculate_profit(combinations):
    pass


if __name__ == "__main__":
    actions = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 38, 14, 18, 8, 4, 10, 24, 114]
    target = 500
    combinations = get_combinations(target, actions)
    print(f"Nomber of possible combinations is: {len(combinations)}\n{combinations}")
