# EXERCICE 1 - TITANIC

import csv

# LECTURE DU FICHIER
def lire_csv():
    with open("titanic_survival.csv", newline="", encoding="utf-8") as fichier:
        return list(csv.DictReader(fichier))

# CALCUL DE LA MOYENNE D'AGE
def moyenne_age(colonnes):
    ages = [float(c["age"]) for c in colonnes if c["age"]]
    return sum(ages) / len(ages)

# CALCUL DU NOMBRE DE SURVIVANTS
def survie_par_classe(colonnes):
    total = {}
    survivants = {}

    # RECUPERATION DE LA CLASSE DE CHAQUE PASSAGER
    for c in colonnes:
        pclass = c["pclass"]
        if not pclass:
            continue

        # COMPTEUR DU NBRE DE SURVIVANTS
        total[pclass] = total.get(pclass, 0) + 1
        if c["survived"] == "1":
            survivants[pclass] = survivants.get(pclass, 0) + 1

    return {
        pclass: survivants.get(pclass, 0) / total[pclass] * 100
        for pclass in total
    }

# RECHERCHE DU BATEAU AYANT SAUVE LE PLUS DE PERSONNE
def bateau_plus_sauvetage(colonnes):
    bateaux = {}

    # COMPTE NBRE SURVIVANTS PAR BATEAU
    for c in colonnes:
        if c["boat"]:
            bateaux[c["boat"]] = bateaux.get(c["boat"], 0) + 1

    # RECHERCHE
    plus_utilise = max(bateaux, key=bateaux.get)
    return plus_utilise, bateaux[plus_utilise]



colonnes = lire_csv()

print(f"Moyenne d'âge des passagers:\n~{round(moyenne_age(colonnes))} ans")

print("\nPourcentage de survie par classe de passager:")
for pclass, rate in survie_par_classe(colonnes).items():
    print(f"Classe {pclass} : ~{round(rate)}%")

bateau, count = bateau_plus_sauvetage(colonnes)
print(f"\nBateau ayant sauvé le plus de passagers:\nBateau n°{bateau} : {count} passagers sauvés")