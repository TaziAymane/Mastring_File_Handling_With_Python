"""
class Personne:
    def __init__(self , n, p, a):
        self.name = n
        self.prenome = p
        self.age = a
    def affichage(self):
        return f" name : {self.name}\n Prenom : {self.prenome}\n Age : {self.age}"

p = Personne("aymane", "tazi", 20)  
print(p.affichage())
"""
"""
class Utilisateur:
    def __init__(self, u, p):
        self.username = u
        self.password = p

    def authentifier(self, mdp):
        return self.password == mdp

user1 = Utilisateur('aymane', "20252026")
user2 = Utilisateur('ahmes', "121212")


print(user1.authentifier("20252026"))
print(user2.authentifier("123123123"))


class PasswordSecurity:
    def est_fort(self, mdp):
        if len(mdp) < 8:
            return "password must be 8 character"
        if not any(i.isdigit() for i in mdp):
            return 'password must chiffre '
        if not any(i.isupper() for i in mdp):
            return 'password must be UpperCase'
        return 'password succssefuly'

psw1 = PasswordSecurity()
psw2 = PasswordSecurity()
psw3 = PasswordSecurity()
print(psw1.est_fort("Aymane2026"))
print(psw2.est_fort("Aymane"))
print(psw3.est_fort("aymane2025"))
"""

class SecurityLog:
    def _init_(self):
        self.evenements = []  
    def ajouter_evenement(self, message):
        self.evenements.append(message)
    def afficher_logs(self):
        if not self.evenements:
            print("Aucun événement enregistré.")
            return
        print("Security Logs")
        for i, event in enumerate(self.evenements, start=1):
            print(f"{i}. {event}")
log = SecurityLog()
log.ajouter_evenement("Tentative de connexion échouée")
log.ajouter_evenement("Connexion réussie")
log.ajouter_evenement("Changement de mot de passe")
log.ajouter_evenement("Changemene")
log.afficher_logs()