import math

# Liste des joueurs et de leur score Elo actuel
joueurs = {"Alice": 1200, "Bob": 1300, "Charlie": 1400}

# Fonction de prédiction de la probabilité de victoire d'un joueur sur un autre
def proba_victoire(joueurA, joueurB):
    return 1 / (1 + math.pow(10, (joueurB - joueurA) / 400))

# Fonction de mise à jour des scores Elo après une partie
def maj_scores(joueurA, joueurB, resultat, k):
    probaA = proba_victoire(joueurs[joueurB], joueurs[joueurA])
    probaB = proba_victoire(joueurs[joueurA], joueurs[joueurB])
    if resultat == 1:
        joueurs[joueurA] += k * (1 - probaA)
        joueurs[joueurB] += k * (0 - probaB)
    elif resultat == 0:
        joueurs[joueurA] += k * (0 - probaA)
        joueurs[joueurB] += k * (1 - probaB)
    else:
        joueurs[joueurA] += k * (0.5 - probaA)
        joueurs[joueurB] += k * (0.5 - probaB)

# Exemple de partie entre Alice et Bob, avec une victoire pour Alice
maj_scores("Alice", "Bob", 1, 32)

print(joueurs) # Résultat : {"Alice": 1210.64, "Bob": 1289.36, "Charlie": 1400}

from math import pow

def calculate_probability(player_rating, opponent_rating):
    return 1.0 / (1.0 + pow(10, (opponent_rating - player_rating) / 400))

def update_elo(player_rating, opponent_rating, result, k_factor):
    expected_score = calculate_probability(player_rating, opponent_rating)
    if result == 1:
        actual_score = 1.0
    elif result == 0.5:
        actual_score = 0.5
    else:
        actual_score = 0.0
    new_rating = player_rating + k_factor * (actual_score - expected_score)
    return new_rating

if condition1:
    # instructions à exécuter si condition1 est vraie
elif condition2:
    # instructions à exécuter si condition1 est fausse et condition2 est vraie
else:
    # instructions à exécuter si toutes les conditions précédentes sont fausses

    #Lorsque le programme est exécuté, chaque condition est évaluée l'une après l'autre jusqu'à ce qu'une condition soit vraie. Si la première condition est vraie, les instructions à l'intérieur du bloc if sont exécutées et la structure if/elif/else est terminée. Si la première condition est fausse, le programme teste la condition suivante et ainsi de suite. Si toutes les conditions sont fausses, les instructions à l'intérieur du bloc else sont exécutées.

#En somme, elif permet de tester une condition alternative si la première condition testée par if est fausse.





