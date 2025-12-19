# EXERCICE 3 - GESTION DE FILMS

import json
import os
from datetime import datetime

class Movie:
    def __init__(self, titre, date_sortie, description, movie_id=None):
        self.id = movie_id
        self.titre = titre.title()
        self.date_sortie = self.valider_date(date_sortie)
        self.description = description

    def valider_date(self, date_str):
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return date_str
        except ValueError:
            print("Format de date invalide. Mettre JJ/MM/AAAA.")
            return date_str

    def __str__(self):
        return f"ID: {self.id}\nTitre: {self.titre}\nDate: {self.date_sortie}\nDescription: {self.description}"


class MovieManager:
    def __init__(self, filepath="data/movies.json"):
        self.filepath = filepath
        self.movies = []
        self.load_from_json()

    def load_from_json(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                for m in data:
                    self.movies.append(Movie(m['titre'], m['date_sortie'], m['description'], m['id']))

    def save_to_json(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump([vars(m) for m in self.movies], f, indent=4, ensure_ascii=False)

    def create_movie(self, titre, date_sortie, description):
        new_id = max([m.id for m in self.movies], default=0) + 1
        movie = Movie(titre, date_sortie, description, new_id)
        self.movies.append(movie)
        self.save_to_json()
        return movie

    def get_all_movies(self):
        return self.movies

    def get_movie_by_title(self, titre):
        for m in self.movies:
            if m.titre.lower() == titre.lower():
                return m
        return None

    def update_movie_by_title(self, titre, new_titre=None, new_date=None, new_description=None):
        movie = self.get_movie_by_title(titre)
        if not movie:
            return None
        if new_titre: movie.titre = new_titre.title()
        if new_date: movie.date_sortie = new_date
        if new_description: movie.description = new_description
        self.save_to_json()
        return movie

    def delete_movie_by_title(self, titre):
        movie = self.get_movie_by_title(titre)
        if movie:
            self.movies.remove(movie)
            self.save_to_json()
            return True
        return False

    def get_movies_sorted_by_date(self):
        return sorted(self.movies, key=lambda m: datetime.strptime(m.date_sortie, "%d/%m/%Y"))


class MovieCLI:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        while True:
            print("\n===== MENU =====")
            print("1. Ajouter un film")
            print("2. Afficher les films")
            print("3. Modifier un film")
            print("4. Supprimer un film")
            print("5. Quitter")
            choix = input("Choisissez : ").strip()
            if choix == "1": self.create_movie()
            elif choix == "2": self.read_movies()
            elif choix == "3": self.update_movie()
            elif choix == "4": self.delete_movie()
            elif choix == "5": break
            else: print("Option invalide.")

    def create_movie(self):
        titre = input("Titre : ").strip()
        date_sortie = input("Date (JJ/MM/AAAA) : ").strip()
        description = input("Description : ").strip()
        movie = self.manager.create_movie(titre, date_sortie, description)
        print("\nFilm créé :\n", movie)

    def read_movies(self):
        print("\n1. Afficher tous les films")
        print("2. Rechercher par titre")
        choix = input("Choisissez : ").strip()
        if choix == "1":
            for m in self.manager.get_movies_sorted_by_date():
                print("\n" + str(m))
        elif choix == "2":
            titre = input("Titre : ").strip()
            movie = self.manager.get_movie_by_title(titre)
            print(movie if movie else "Film non trouvé.")

    def update_movie(self):
        titre = input("Titre du film à modifier : ").strip()
        movie = self.manager.get_movie_by_title(titre)
        if not movie:
            print("Film non trouvé."); return
        new_titre = input("Nouveau titre: ").strip()
        new_date = input("Nouvelle date: ").strip()
        new_desc = input("Nouvelle description: ").strip()
        self.manager.update_movie_by_title(
            titre,
            new_titre if new_titre else None,
            new_date if new_date else None,
            new_desc if new_desc else None
        )
        print("Film mis à jour :")
        print(self.manager.get_movie_by_title(new_titre if new_titre else titre))

    def delete_movie(self):
        titre = input("Titre du film à supprimer : ").strip()
        if self.manager.delete_movie_by_title(titre):
            print("Film supprimé.")
        else:
            print("Film non trouvé.")



manager = MovieManager()
cli = MovieCLI(manager)
cli.run()
