from check.input import ask_all_marks
from calc.marks import average

# Vraag de gebruiker om cijfers in te voeren.
marks = ask_all_marks('Cijfer')

# Bereken het gemiddelde van de ingevoerde cijfers.
marks_average = average(marks)

# Bereken het gemiddelde
print(f'Het gemiddelde van de {len(marks)} ingevoerd cijfers is {marks_average:.1f}')

