
"""
from typing import List, Union
import math

# a) Fonction moyenne
def moyenne(notes: List[Union[int, float]]) -> float:
    '''
    Calcule la moyenne d'une liste non vide de notes.
    '''
    assert isinstance(notes, list), "L doit être une liste"
    assert len(notes) > 0, "La liste ne doit pas être vide"
    assert all(isinstance(x, (int, float)) for x in notes), "Tous les éléments doivent être numériques"
    
    return sum(notes) / len(notes)


# b) Fonction écart_type
def ecart_type(notes: List[Union[int, float]]) -> float:
    '''
    Calcule l'écart-type d'une liste non vide de notes.
    '''
    assert isinstance(notes, list), "L doit être une liste"
    assert len(notes) > 0, "La liste ne doit pas être vide"
    assert all(isinstance(x, (int, float)) for x in notes), "Tous les éléments doivent être numériques"
    
    n = len(notes)
    mu = moyenne(notes)  # utilisation de la fonction moyenne
    
    variance = sum((x - mu) ** 2 for x in notes) / n
    return math.sqrt(variance)


# c) Fonction moy avec annotations complètes
def moy(L: List[Union[int, float]]) -> float:
    '''
    Calcule la moyenne des éléments de la liste L.
    
    Paramètres:
    L -- liste non vide de nombres réels (entiers ou flottants)
    
    Retourne:
    La moyenne des éléments de L
    '''
    # Vérifications avec assertions
    assert isinstance(L, list), "L doit être une liste"
    assert len(L) > 0, "La liste ne doit pas être vide"
    assert all(isinstance(x, (int, float)) for x in L), "Tous les éléments doivent être numériques"
    
    return sum(L) / len(L)


# Exemple d'utilisation
# if __name__ == "__main__":
notes_test = [12, 14, 16, 10, 8.5]
    
print("Liste de notes:", notes_test)
print(f"Moyenne: {moyenne(notes_test):.2f}")
print(f"Ecart-type: {ecart_type(notes_test):.2f}")
print(f"Moyenne (fonction moy): {moy(notes_test):.2f}")

# Test avec la fonction moy
print("\nTest de la fonction moy avec annotations:")
resultat = moy(notes_test)
print(f"Resultat: {resultat}")
"""

"""
    Calcule la factorielle de n de manière itérative.
    n : entier naturel
    retourne : n! (factorielle de n)
"""
def fact(n):

    if n < 0:
        return "Erreur : n doit être un entier naturel"
    
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

# Exemples d'utilisation
"""
print(fact(0))  # 1
print(fact(1))  # 1
print(fact(5))  # 120
print(fact(10)) # 3628800
"""
print(fact(3))  # 1