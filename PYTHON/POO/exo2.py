from abc import ABC, abstractmethod

# Classe principale
class Vehicule(ABC):
    #Constructeur
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.vitesse = 0

    # Méthode abstraite
    @abstractmethod
    def accelerer(self):
        pass

    def arreter(self):
        self.vitesse = 0

    #Méthode de classe
    @classmethod
    def from_factory(cls, type_vehicule, *args, **kwargs):
        if type_vehicule == "voiture":
            return Voiture(*args, **kwargs)
        if type_vehicule == "moto":
            return Moto(*args, **kwargs)
        raise ValueError("Véhicule inconnu")

        
# Classe fille Voiture
class Voiture(Vehicule):
    # Constructeur
    def __init__(self, marque, modele, annee, nb_portes: int):
        super().__init__(marque, modele, annee)
        self.nb_portes = nb_portes

    def accelerer(self):
        self.vitesse += 1

# Classe fille Moto
class Moto(Vehicule):
    def __init__(self, marque, modele, annee):
        super().__init__(marque, modele, annee)

    def accelerer(self):
        self.vitesse += 2

    def acrobaties(self):
        print("Wheel_in !")


v1 = Vehicule.from_factory("voiture", "Renault", "Clio", 2020, nb_portes=3)
v2 = Vehicule.from_factory("moto", "Yamaha", "MT-07", 2000)

v1.accelerer()
v2.accelerer()
v2.acrobaties()

print(v1.vitesse)
print(v2.vitesse)
    