# Bereken het gemiddelde van de getallen in een array.
# Return value: Het gemiddelde afgerond op één decimaal.
def average(numbers):
    # Als de lijst leeg is dan is het gemiddeld een 0
    if not numbers:
        return 0

    # Tel alle cijfers bijelkaar op.
    total_sum = sum(numbers)

    # Tel het aantal ingevoerde cijfers.
    count = len(numbers)

    # Bereken het gemiddelde.
    average = total_sum / count

    return average
