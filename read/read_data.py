# read/read_data.py
import csv
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "movies.csv")


def read_all():
    movies = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies.append(row)
    return movies


def get_by_title(titre):
    return [m for m in read_all() if m["titre"].lower() == titre.lower()]


def get_by_age_limit(max_age):
    return [m for m in read_all() if int(m["age_limite"]) <= int(max_age)]


def get_by_genre(genre):
    return [m for m in read_all() if m["genre"].lower() == genre.lower()]


def get_by_year_range(start, end):
    return [
        m
        for m in read_all()
        if int(start) <= int(m["annee_production"]) <= int(end)
    ]


def menu():
    while True:
        print("\n=== Menu Read ===")
        print("1. Rechercher par titre")
        print("2. Films par limite d'âge")
        print("3. Films par genre")
        print("4. Films par période (entre deux années)")
        print("5. Quitter")

        choice = input("Choix : ")

        if choice == "1":
            titre = input("Titre : ")
            print(get_by_title(titre))
        elif choice == "2":
            age = input("Âge maximum : ")
            print(get_by_age_limit(age))
        elif choice == "3":
            genre = input("Genre : ")
            print(get_by_genre(genre))
        elif choice == "4":
            start = input("Année de début : ")
            end = input("Année de fin : ")
            print(get_by_year_range(start, end))
        elif choice == "5":
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    menu()
