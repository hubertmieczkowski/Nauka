"""
Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
zmieniać wartości
"""

class Uzytkownik:
    def __init__(self, wiek):
        self._wiek = wiek

    @property
    def wiek(self):
        return self._wiek
    
    @wiek.setter
    def wiek(self, nowy_wiek):
        if 0 <= nowy_wiek <= 120:
            self._wiek = nowy_wiek
        else:
            print("Wiek musi mięścić się w zakresie od 0 do 120!")

u1 = Uzytkownik(25)
print(u1.wiek)   

u1.wiek = 35
print(u1.wiek)   

u1.wiek = 150    
print(u1.wiek)   

    