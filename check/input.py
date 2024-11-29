import re       # Is nodig voor regular expressions.

# verander alle komma's door punten
def replace_comma_with_dot(input_user):
    number_of_dots = input_user.count('.')
    number_of_commas = input_user.count(',')

    # Getal met alleen in 1 komma. 
    # Dat wordt de komma door een punt vervangen.
    if number_of_dots == 0 and number_of_commas == 1:
        return  input_user.replace(",", ".")
    
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


# Deze functie vraagt input van de gebruiker.
# Return value: number van het type float
def ask_mark(message):
    input_is_mark = False
    number = None

    # Blijf een cijfer vragen totdat de
    while input_is_mark == False:
        input_user = input(f'{message}: ')

        # Vervang de komma met een punt.
        # Verwijder alle punten en komma's die met grote getallen te maken hebben.
        # Zie replace_comma_with_dot functie.
        if replace_comma_with_dot(input_user) != False:
            input_user = replace_comma_with_dot(input_user)
        else:
            print(f'U heeft geen getal geldig ingevoerd: {input_user}')

        # Controleer of de invoer ook echt een getal is.
        if not is_float(input_user):
            print(f'U heeft geen getal ingevoerd: {input_user}')

        # Converteer de invoer naar een getal
        if not convert_to_number(input_user):
            print(f'Het is nog niet gelukt om de input te converteren: {input_user}')
        else:
            number = convert_to_number(input_user)

        input_is_mark = True

    return number


# print(replace_comma_with_dot('1132234.5'))
# print(replace_comma_with_dot('1.132.234,5'))
# print(replace_comma_with_dot('1132234,5'))
# print(replace_comma_with_dot('1,132,234.5'))
# print(replace_comma_with_dot('1,132,234.5.7'))
# print(replace_comma_with_dot('1132234'))
