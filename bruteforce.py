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
--> Parcourir toutes les combinaisons possibles de nombres dans la liste d'actions et
vérifier si leur somme == 500€
"""


def get_action_combinations(target, actions):
    number_actions = len(actions)
    combinations = []

    for n in range(number_actions):
        current_sum = actions[n]
        current_combination = [actions[n]]

        for k in range(n+1, number_actions):
            if current_sum + actions[k] <= target:
                current_combination.append(actions[k])
                current_sum += actions[k]

            if current_sum == target:
                combinations.append(current_combination[:])
                break

    return combinations


def calculate_profit(combinations):
    pass


if __name__ == "__main__":
    actions = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 38, 14, 18, 8, 4, 10, 24, 114]
    target = 500
    combinations = get_action_combinations(target, actions)
    print(f"Nomber of possible combinations is: {len(combinations)}\n{combinations}")
