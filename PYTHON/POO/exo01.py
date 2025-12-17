from abc import ABC, abstractmethod

# DEFINITION DE LA CLASSE
class Animal(ABC):
    # ATTRIBUT STATIQUE
    population = 0

    # AJOUT DU CONSTRUCTEUR
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age
        Animal.population += 1

    
    # AJOUT DE LA METHODE CRIER
    @abstractmethod
    def crier(self):
        pass

    # AJOUT D'UNE METHODE STATIQUE
    @staticmethod
    def nombre_animaux():
        return Animal.population

    # AJOUT METHODE STR
    def __str__(self):
        return f"Animal(nom={self._nom}, age={self._age})"

    # GETTER ET SETTER
    def get_age(self):
        return self._age

    def get_nom(self):
        return self._nom

    def set_age(self, age):
        self._age = age

    def set_nom(self, nom):
        self._nom = nom

# SOUS CLASSE
class Chien(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)

    def crier(self):
        print("Woof !")

    @classmethod
    def from_factory(cls, nom, age):
        if len(nom) <= 3 or age <= 0:
            raise ValueError("erreur")
        return cls(nom, age)


chien = Chien.from_factory("Rexou", 1)
chien.crier()

