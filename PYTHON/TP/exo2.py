# EXERCICE 2 - CITATIONS D'ECRIVAINS

from quote import quote
from collections import Counter
import re

# RECUPERATION DES CITATIONS
citations = quote(search="Edgar Allan Poe", limit=50)

# RECUPERATION DES TITRES
titres = [c['book'] for c in citations if c['book']]

# COMPTEUR TITRES
compteur_titres = Counter(titres)

# TRI DECROISSANT
titres_tries = compteur_titres.most_common()

# RECUPERATION DES CITATIONS
textes = [c['quote'] for c in citations]

# CONCATENATION DES CITATIONS
text_complet = " ".join(textes).lower()

# SUPPRESSION DE LA PONCTUATION
mots = re.findall(r'\w+', text_complet)

# COMPTEUR FREQUENCE MOTS
compteur_mots = Counter(mots)

# FILTRES ET TRI DES MOTS
mots_frequents = [(mot, frequence) for mot, frequence in compteur_mots.most_common() if frequence >= 5]

# LISTE DES AUTEURS
auteurs = [
    "Edgar Allan Poe", "Arthur Schopenhauer", "Georges Orwell",
    "Victor Hugo", "Simone De Beauvoir", "Frank Herbert",
    "Gustave Flaubert", "Guy De Maupassant", "Isaac Asimov",
    "Ernest Hemingway", "Voltaire", "Tolkien",
    "Agatha Christie", "Emile Zola", "William Shakespeare",
    "Friedrich Nietzsche"
]

# MOTS COMMUNS
mots_par_auteur = {}
for auteur in auteurs:
    citations = quote(search=auteur, limit=10)
    words = set()
    for c in citations:
        words.update(re.findall(r'\w+', c['quote'].lower()))
    mots_par_auteur[auteur] = words

communs = set.intersection(*mots_par_auteur.values())



""" 
# EXO 1 -------------------------------------------
print("Inventaire des titres d'Edgar Allan Poe:\n")
for titre, frequence in titres_tries:
    print(f"{titre} : {frequence}")


# EXO 2 ------------------------------------------
print("Inventaire des mots d'Edgar Allan Poe:\n")
for mot, frequence in mots_frequents:
    print(f"{mot} : {frequence}") """

# EXO 3 ------------------------------------------
print(f"Mots présents dans les citations de tous les auteurs ({len(communs)} mots):")
print(communs)