"""
Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie
usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij
stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy

# Przykład: Klasa z narzędziami matematycznymi
class MathHelper:
@staticmethod
def dodaj(a, b):
"Ta metoda nie potrzebuje 'self'. Działa jak zwykła funkcja."
return a + b
@staticmethod
def pomnoz(a, b):
"Możemy ją wywołać bezpośrednio na klasie."
return a * b
"""

class KalkulatorWalut:

    @staticmethod
    def usd_na_pln(kwota_usd):
        kurs = 4
        return kwota_usd * kurs
    

wynik = KalkulatorWalut.usd_na_pln(100)
print(f"100 USD to {wynik} PLN")