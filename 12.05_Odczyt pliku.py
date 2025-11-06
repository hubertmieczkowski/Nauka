"""
Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
użytkownikowi
"""

try:
    with open("nieistniejacy.txt", "r") as plik:
        zawartosc = plik.read()
        print(zawartosc)
except FileNotFoundError:
    print("Plik 'nieistniejacy.txt' nie został znaleziony.")
