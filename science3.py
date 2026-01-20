# Qestion 1
"""
try:
    a = float(input('entre un nb1 : '))
    b = float(input('entre un nb2 : '))
    resultat1 = a/b
    print(f'{a} / {b} = {resultat1:.2f}')

except ZeroDivisionError:
    print('devision par 0 est imposible : ')

"""
"""
# Question 2
import logging 
# Configuration du logging (écrit dans un fichier)
logging.basicConfig(
    filename='erreurs.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def devision(a, b):
    if b == 0:
        raise ZeroDivisionError("Detirminateur null : division impossible ")
    return a / b 
try:
    a = float(input('entre nb1 : '))
    b = float(input('entre nb2 : '))
    resultat2 = devision(a, b)
    print(f"{a} / {b} = {resultat2:.2f}")
except ZeroDivisionError as e:
    print(f'error :' , e)
    logging.error(f"ZeroDivisionError interceptée : {e}")
except ValueError:
    print("Erreur : veuillez entrer des nombres valides.")
    logging.error("ValueError : saisie non numérique.")
"""
"""
# Qestion 3
while True:
    try:
        a = float(input('entre la valeur de nb1 : '))
        b = float(input('entre la valeur de nb2 : '))

        resultat = a/b 
        print(f"{a} / {b} = {resultat:.2f}")
        break
    except ZeroDivisionError:
        print('Erreur : division par zéro ! Réessayez avec un dénominateur différent.')
    except ValueError:
        print('Erreur : veuillez entrer des nombres valides.')
"""

def safe_exec(default_value=None):
    # Décorateur paramétré : on choisit une valeur par défaut
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Erreur dans {func.__name__} : {e}")
                return default_value
        return wrapper
    return decorator


@safe_exec(default_value=0)
def division(a, b):
    return a / b

print(division(10, 2))  # 5.0
print(division(10, 0))  # affiche erreur + retourne 0
