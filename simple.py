# Vraag de gebruiker om cijfers in te voeren.
mark1 = float(input('Cijfer 1: '))
mark2 = float(input('Cijfer 2: '))
mark3 = float(input('Cijfer 3: '))

# Bereken het gemiddelde van de ingevoerde cijfers.
marks_average = (mark1 + mark2 + mark3) / 3

# Bereken het gemiddelde
print(f'Het gemiddelde van de 3 ingevoerd cijfers is {marks_average:.1f}')

# Problemen bij de invoer van een getal.
# 1. Gebruiker drukt op enter. Veld is leeg.
# 2. Gebruiker voert tekst i.p.v. getallen.
# 3. Gebruiker voert Komma's in i.p.v. punten.
# 4. Gebruiker voert een getal in kleiner dan 1 en groter dan 10.