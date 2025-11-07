import csv
import os

class Movie:
    """Représente un film."""

    def __init__(self, titre: str, annee_production: int, genre: str, age_limite: int, id: int = None):
        self.id = int(id) if id is not None else None
        self.titre = titre
        self.annee_production = int(annee_production)
        self.genre = genre
        self.age_limite = int(age_limite)

    def __str__(self):
        return f"[{self.id}] {self.titre} ({self.annee_production}) - {self.genre} - Age limite : {self.age_limite}"

    @staticmethod
    def next_id_from_csv(csv_path: str):
        """Renvoie le prochain ID disponible dans le CSV."""
        if not os.path.exists(csv_path):
            return 1
        max_id = 0
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    i = int(row["id"])
                    if i > max_id:
                        max_id = i
                except ValueError:
                    continue
        return max_id + 1
