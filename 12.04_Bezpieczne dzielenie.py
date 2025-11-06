"""
Napisz funkcję bezpieczne_dzielenie(a, b), która zwraca wynik dzielenia a / b. Użyj bloku
try...except, aby obsłużyć błąd ZeroDivisionError. Jeśli wystąpi ten błąd, funkcja powinna
zwrócić None i wyświetlić komunikat "Błąd: Dzielenie przez zero!"
"""

def bezpieczne_dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Błąd, dzielenie przez 0!")
        return None
    
a = float(input("Podaj pierwszą cyfrę: "))
b = float(input("Podaj drugą cyfrę: "))

print(bezpieczne_dzielenie(a, b))