# Deze functie controleert of het getal niet kleiner is dan 1
# en niet groter dan 10.
# Return value: False. Getal is groter dan 10 of kleiner dan 1.
# Return value: True. Getal is tussen 1 en 10.
def is_mark(number):
    if number < 1 or number > 10:
        return False
    else:
        return True

