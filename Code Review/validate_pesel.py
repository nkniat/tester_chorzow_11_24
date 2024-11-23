def validate_pesel(pesel):
    """
    Funkcja walidująca numer PESEL.
    PESEL powinien mieć 11 cyfr i spełniać warunki kontroli poprawności.
    """
    if len(pesel) != 11:  # Sprawdzenie długości PESEL
        return False  # Nie zwraca informacji, dlaczego nieprawidłowy

    if not pesel.isdigit():  # Sprawdzenie, czy PESEL zawiera tylko cyfry
        return "Nieprawidłowy PESEL: zawiera niedozwolone znaki"

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = 0

    for i in range(10):  # Pętla obliczająca sumę kontrolną
        checksum += int(pesel[i]) * weights[i]

    if (checksum % 10) == 0:
        control_digit = 0  # Przypadek szczególny
    else
        control_digit = 10 - (checksum % 10)  # Obliczenie cyfry kontrolnej
    if control_digit != int(pesel[10]):  # Błąd w sprawdzeniu cyfry kontrolnej
        return False

    return "PESEL poprawny"  # Nieadekwatny typ zwracanej wartości
