from abc import ABC, abstractmethod

# Classe principale
class Vehicule(ABC):
    #Constructeur
    def __init__(self, marque, modele, annee):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._vitesse = 0

    # Getters / Setters
    def get_marque(self):
        return self._marque

    def set_marque(self, marque):
        self._marque = marque

    def get_modele(self):
        return self._modele

    def set_modele(self, modele):
        self._modele = modele

    def get_annee(self):
        return self._annee

    def set_annee(self, annee):
        self._annee = annee

    def get_vitesse(self):
        return self._vitesse

    def set_vitesse(self, vitesse):
        self._vitesse = vitesse

    # Méthode abstraite
    @abstractmethod
    def accelerer(self):
        pass

    def arreter(self):
        self._vitesse = 0

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
        self.__nb_portes = nb_portes

    def get_nb_portes(self):
        return self.__nb_portes

    def set_nb_portes(self, nb_portes):
        self.__nb_portes =nb_portes

    def accelerer(self):
        self._vitesse += 1

# Classe fille Moto
class Moto(Vehicule):
    def __init__(self, marque, modele, annee):
        super().__init__(marque, modele, annee)

    def accelerer(self):
        self._vitesse += 2

    def acrobaties(self):
        print("Wheel_in !")


v1 = Vehicule.from_factory("voiture", "Renault", "Clio", 2020, nb_portes=3)
v2 = Vehicule.from_factory("moto", "Yamaha", "MT-07", 2000)

v1.accelerer()
v2.accelerer()
v2.acrobaties()

print(v1.get_vitesse())
print(v2.get_vitesse())
print(v1.get_nb_portes())
print(v2.acrobaties)
    