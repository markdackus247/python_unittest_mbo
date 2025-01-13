from Models.MarkProcessor import MarkProcessor
from calc.marks import average

# Programma wordt uitgevoerd als direct main.py wordt aangeroepen.
if __name__ == '__main__':
    # Vraag de gebruiker om cijfers in te voeren.
    processor = MarkProcessor()
    all_marks = processor.ask_all_marks("Voer een cijfer in")

    # Bereken het gemiddelde van de ingevoerde cijfers.
    marks_average = average(all_marks)

    # Bereken het gemiddelde
    print(f'Het gemiddelde van de {len(all_marks)} ingevoerd cijfers is {marks_average:.1f}')