# Heritage Simple 
# class Animal:
#     def Speak(self):
#         print('the animale speak')

# class Dog(Animal):
#     def speak(self):
#         super.Speak()
#         print("Specifically, the dog barks")


# dog = Dog();
# dog.Speak()
# -----------------------------Heritage Mutiple -------------------------------------------
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def info(self):
        return f"Nom: {self.nom}, Âge: {self.age}"


class Employe(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)      # use parent (Personne)
        self.salaire = salaire

    def info_employe(self):
        return f"{self.info()}, Salaire: {self.salaire} MAD"


class Etudiant(Personne):
    def __init__(self, nom, age, niveau):
        super().__init__(nom, age)      # use parent (Personne)
        self.niveau = niveau

    def info_etudiant(self):
        return f"{self.info()}, Niveau: {self.niveau}"


# Child that inherits from BOTH Employe and Etudiant
class EmployeEtudiant(Employe, Etudiant):
    def __init__(self, nom, age, salaire, niveau):
        Personne.__init__(self, nom, age)  # initialize shared parent once
        self.salaire = salaire
        self.niveau = niveau

    def info_complete(self):
        return f"{self.info()}, Salaire: {self.salaire} MAD, Niveau: {self.niveau}"


# ---- test ----
p = Personne("Sara", 30)
e = Employe("Amine", 28, 6000)
et = Etudiant("Youssef", 20, "Licence")
ee = EmployeEtudiant("Khadija", 24, 4000, "Master")

# print(p.info())
# print(e.info_employe())
# print(et.info_etudiant())
# print(ee.info_complete())


# -----------------------------Exercice 1 ----------------------------
class Compte:
    def __init__(self,username):
        self.username = username
    def access(self):
        print('Access utilisateur stander')
    
class Admin(Compte):
    def access(self):
       print("Access administrateur compte ")
    
# ---- Tests ----
user = Compte('aymane_user')
admin = Admin("aymane_admin")

user.access()
admin.access()

      