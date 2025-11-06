
"""
Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
(raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
testuje tę funkcję w bloku try...except.
"""


class InvalidPasswordError(Exception):
    pass


def ustaw_haslo(haslo):
    if len(haslo) < 8:
        raise InvalidPasswordError("Hasło musi mieć co najmniej 8 znaków!")
    else:
        print("Hasło zostało ustawione poprawnie.")


try:
    ustaw_haslo("abc123")      
    ustaw_haslo("bezpiecznehaslo")  
except InvalidPasswordError as e:
    print("Błąd:", e)
