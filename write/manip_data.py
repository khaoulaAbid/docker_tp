# write/manip_data.py
import csv
import os

from models.Movie import Movie
from exceptions.InvalidTitleException import InvalidTitleException
from exceptions.InvalidYearException import InvalidYearException
from exceptions.InvalidGenreException import InvalidGenreException
from exceptions.InvalidAgeLimitException import InvalidAgeLimitException

CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "movies.csv")


# -------------------- VALIDATION --------------------
def validate_title(titre: str):
    if not titre or titre.strip() == "":
        raise InvalidTitleException("Le titre ne peut pas être vide.")
    return titre.strip()


def validate_year(annee: str):
    try:
        annee = int(annee)
    except ValueError:
        raise InvalidYearException("L'année doit être un nombre.")
    if annee < 1888 or annee > 2100:
        raise InvalidYearException("L'année est invalide.")
    return annee


def validate_genre(genre: str):
    if not genre or genre.strip() == "":
        raise InvalidGenreException("Le genre ne peut pas être vide.")
    return genre.strip()


def validate_age_limit(age_limite: str):
    try:
        age_limite = int(age_limite)
    except ValueError:
        raise InvalidAgeLimitException("La limite d'age doit être un nombre.")
    if age_limite < 0 or age_limite > 120:
        raise InvalidAgeLimitException("Limite d'age invalide.")
    return age_limite


# -------------------- CSV HELPERS --------------------
def read_all():
    movies = []
    if not os.path.exists(CSV_PATH):
        return movies
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies.append(row)
    return movies


def write_all(movies):
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "titre", "annee_production", "genre", "age_limite"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for movie in movies:
            writer.writerow(movie)


# -------------------- ACTIONS --------------------
def add_movie():
    try:
        titre = validate_title(input("Titre : "))
        annee = validate_year(input("Année de production : "))
        genre = validate_genre(input("Genre : "))
        age = validate_age_limit(input("Limite d'âge : "))
    except Exception as e:
        print("Erreur :", e)
        return

    next_id = Movie.next_id_from_csv(CSV_PATH)
    m = Movie(titre, annee, genre, age, id=next_id)

    rows = read_all()
    rows.append(
        {
            "id": m.id,
            "titre": m.titre,
            "annee_production": m.annee_production,
            "genre": m.genre,
            "age_limite": m.age_limite,
        }
    )
    write_all(rows)
    print(" Film ajouté :", m)


def modify_movie():
    id_to_modify = input("ID du film à modifier : ")
    rows = read_all()
    found = False

    for row in rows:
        if row["id"] == id_to_modify:
            found = True
            print("Saisir les nouvelles informations :")
            try:
                titre = validate_title(input("Titre : "))
                annee = validate_year(input("Année de production : "))
                genre = validate_genre(input("Genre : "))
                age = validate_age_limit(input("Limite d'âge : "))
            except Exception as e:
                print("Erreur :", e)
                return
            row["titre"] = titre
            row["annee_production"] = annee
            row["genre"] = genre
            row["age_limite"] = age
            break

    if not found:
        print("Film non trouvé.")
        return

    write_all(rows)
    print(f"Film {id_to_modify} modifié.")


def delete_movie():
    id_to_delete = input("ID du film à supprimer : ")
    rows = read_all()
    new_rows = [r for r in rows if r["id"] != id_to_delete]

    if len(new_rows) == len(rows):
        print("Film non trouvé.")
        return

    write_all(new_rows)
    print(f"Film {id_to_delete} supprimé.")


# -------------------- MENU --------------------
def menu():
    while True:
        print("\n=== Menu Write ===")
        print("1. Ajouter un film")
        print("2. Modifier un film")
        print("3. Supprimer un film")
        print("4. Quitter")
        choice = input("Choix : ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            modify_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            print("Au revoir")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    menu()
