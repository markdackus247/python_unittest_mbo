import re  # Is nodig voor regular expressions.


# Deze functie controleert of de gebruiker wil stoppen.
# De gebruiker voert dan q, quit, of exit in.
def check_exit_command(input_user):
    # Lijst met commando's om af te sluiten.
    exit_commands = ['q', 'quit', 'exit']

    # Verwijder alle spaties van in de input en converteer alles naar kleine letters.
    stripped_input = input_user.strip().lower()

    # Controleer of het exit commando is gebruikt.
    return stripped_input in exit_commands


# Deze functie controleert of er geen teksten worden ingevoerd.
def check_characters(input_string):
    # Een lijst met alle toegestane characters voor een getal.
    allowed_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.', ',']

    # Doorloop de characters van de input_string één voor één.
    # Return value: True. Als er alleen toegestane characters zijn.
    # Return false: Als er andere characters aanwezig zijn.
    for char in input_string:
        if char not in allowed_characters:
            return False
    return True


# verander alle komma's door punten
def replace_comma_with_dot(input_user):
    number_of_dots = input_user.count('.')
    number_of_commas = input_user.count(',')

    # Getal met alleen in 1 komma. 
    # Dat wordt de komma door een punt vervangen.
    if number_of_dots == 0 and number_of_commas == 1:
        return input_user.replace(",", ".")

    # Grote getallen met meerdere punten.
    # Dan worden alle punten verwijderd.
    # bijvoorbeeld 1.234.356 wordt 1234356
    if number_of_dots > 1 and number_of_commas == 0:
        return input_user.replace(".", "")

    # Grote getallen met meerdere punten en 1 komma.
    # Dan worden alle punten verwijderd.
    # bijvoorbeeld 1.234.356,98 wordt 1234356.98
    if number_of_dots > 1 and number_of_commas == 1:
        input_user = input_user.replace('.', '')
        return input_user.replace(",", ".")

    # Grote getallen met meerdere komma's.
    # Dan worden alle komma's verwijderd.
    # bijvoorbeeld 1,234,356,98 wordt 1234356
    if number_of_dots == 0 and number_of_commas > 1:
        return input_user.replace(',', '')

    # Grote getallen met meerdere komma's en 1 punt.
    # Dan worden alle komma's verwijderd.
    # bijvoorbeeld 1,234,356.98 wordt 1234356.98
    if number_of_dots == 1 and number_of_commas > 1:
        return input_user.replace(',', '')

    if number_of_dots > 1 and number_of_commas > 1:
        return False

    return input_user


# Deze functie controleert of de string daadwerkelijk een nummers is.
# Regular expressions worden gebruikt om te controleren of de invoer een getal is.
# De functie heb ik van internet gehaald.
# Return value: False: Als de input geen float is. True: wel float.
def is_float(item):
    # A float is a float
    if isinstance(item, float):
        return True

    # Ints are okay
    if isinstance(item, int):
        return True

    # Detect leading white-spaces
    if len(item) != len(item.strip()):
        return False

    # Some strings can represent floats or ints ( i.e. a decimal )
    if isinstance(item, str):
        # regex matching
        int_pattern = re.compile("^[0-9]*$")
        float_pattern = re.compile("^[0-9]*.[0-9]*$")
        if float_pattern.match(item) or int_pattern.match(item):
            return True
        else:
            return False


# Deze functie maakt van de invoer een getal.
# Return value: getal van type float.
def convert_to_number(input_user):
    try:
        number = float(input_user)
    except:
        return False
    return number


# Deze functie controleert of het getal niet kleiner is dan 1
# en niet groter dan 10.
# Return value: False. Getal is groter dan 10 of kleiner dan 1.
# Return value: True. Getal is tussen 1 en 10.
def is_mark(number):
    if number < 1 or number > 10:
        return False
    else:
        return True

assert is_mark(0.9) == False
assert is_mark(1.0) == True
assert is_mark(10.0) == True
assert is_mark(10.1) == False


# Deze functie vraagt input van de gebruiker.
# Return value: number van het type float
def ask_mark(message):
    input_is_mark = False
    number = None

    # Blijf een cijfer vragen totdat de
    while not input_is_mark:
        input_is_correct = True
        input_user = input(f'{message} (q for quit): ')

        # Controleer of het exit command: q, quit of exit is gebruikt.
        if check_exit_command(input_user):
            return False

        # Controleer of de ingevoerde tekst uit de juiste characters bestaat.
        if not check_characters(input_user):
            print(f'De invoer bestaat uit ongeldige characters: {input_user}')
            input_is_correct = False

        # Vervang de komma met een punt.
        # Verwijder alle punten en komma's die met grote getallen te maken hebben.
        # Zie replace_comma_with_dot functie.
        if input_is_correct:
            if replace_comma_with_dot(input_user):
                input_user = replace_comma_with_dot(input_user)
            else:
                print(f'U heeft geen getal geldig ingevoerd: {input_user}')
                input_is_correct = False

        # Controleer of de invoer ook echt een getal is.
        if input_is_correct:
            if not is_float(input_user):
                print(f'U heeft geen getal ingevoerd: {input_user}')
                input_is_correct = False

        # Converteer de invoer naar een getal
        if input_is_correct:
            if not convert_to_number(input_user):
                print(f'Het is nog niet gelukt om de input te converteren: {input_user}')
                input_is_correct = False
            else:
                number = convert_to_number(input_user)

        # Controleer of het getal ook een cijfer is.
        if input_is_correct:
            if not is_mark(number):
                print(f'Het getal is kleiner dan 1 en groter dan 10')
            else:
                input_is_mark = True

    return number


# Vraagt alle cijfers.
# Gebruiker voert q in als deze klaar is met het invoeren van de cijfers.
# Return value: array van alle ingevulde cijfers: bv. [9.3, 8.2, 6.6, 5,3]
def ask_all_marks(message):
    input_user = None
    counter = 1
    all_marks = []

    while input_user != 'q':
        mark = ask_mark(f'{message} {counter}')

        if not mark:
            input_user = 'q'
        else:
            all_marks.append(mark)
            counter += 1

    return all_marks
