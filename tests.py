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
def is_number(input_user):
    # Controleer of het een positief geheel getal is.
    if input_user.isdigit():
        return True
    
    # Controleer of het een negatief geheel getal is.
    if input_user[0] == '-':
        input_user_sub = input_user[1:len(input_user)]
        if input_user_sub.isdigit():
            return True


# print(replace_comma_with_dot('1132234.5'))
# print(replace_comma_with_dot('1.132.234,5'))
# print(replace_comma_with_dot('1132234,5'))
# print(replace_comma_with_dot('1,132,234.5'))
# print(replace_comma_with_dot('1,132,234.5.7'))
# print(replace_comma_with_dot('1132234'))
