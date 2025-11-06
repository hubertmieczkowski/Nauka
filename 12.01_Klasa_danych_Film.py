"""
Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je
"""

from dataclasses import dataclass

@dataclass
class Film:
    tytul: str
    rezyser: str
    rok_produkcji: int

film1 = Film("Milczenie Owiec", "Jonathan Demme", 1991)
film2 = Film("Hannibal", "Ridley Scott", 2001)

print(film1)
print(film2)