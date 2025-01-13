import re

class MarkProcessor:
    def __init__(self):
        self.exit_commands = ['q', 'quit', 'exit']
        self.allowed_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.', ',']

    def check_exit_command(self, input_user):
        stripped_input = input_user.strip().lower()
        return stripped_input in self.exit_commands

    def check_characters(self, input_string):
        for char in input_string:
            if char not in self.allowed_characters:
                return False
        return True

    def replace_comma_with_dot(self, input_user):
        number_of_dots = input_user.count('.')
        number_of_commas = input_user.count(',')

        if number_of_dots == 0 and number_of_commas == 1:
            return input_user.replace(",", ".")
        if number_of_dots > 1 and number_of_commas == 0:
            return input_user.replace(".", "")
        if number_of_dots > 1 and number_of_commas == 1:
            input_user = input_user.replace('.', '')
            return input_user.replace(",", ".")
        if number_of_dots == 0 and number_of_commas > 1:
            return input_user.replace(',', '')
        if number_of_dots == 1 and number_of_commas > 1:
            return input_user.replace(',', '')
        if number_of_dots > 1 and number_of_commas > 1:
            return False

        return input_user

    def is_float(self, item):
        if isinstance(item, float) or isinstance(item, int):
            return True
        if len(item) != len(item.strip()):
            return False
        int_pattern = re.compile("^[0-9]*$")
        float_pattern = re.compile("^[0-9]*.[0-9]*$")
        if float_pattern.match(item) or int_pattern.match(item):
            return True
        else:
            return False

    def convert_to_number(self, input_user):
        try:
            number = float(input_user)
        except:
            return False
        return number

    def is_mark(self, number):
        return 1 <= number <= 10

    def ask_mark(self, message):
        input_is_mark = False
        number = None

        while not input_is_mark:
            input_is_correct = True
            input_user = input(f'{message} (q for quit): ')

            if self.check_exit_command(input_user):
                return False

            if not self.check_characters(input_user):
                print(f'De invoer bestaat uit ongeldige characters: {input_user}')
                input_is_correct = False

            if input_is_correct:
                if self.replace_comma_with_dot(input_user):
                    input_user = self.replace_comma_with_dot(input_user)
                else:
                    print(f'U heeft geen getal geldig ingevoerd: {input_user}')
                    input_is_correct = False

            if input_is_correct:
                if not self.is_float(input_user):
                    print(f'U heeft geen getal ingevoerd: {input_user}')
                    input_is_correct = False

            if input_is_correct:
                if not self.convert_to_number(input_user):
                    print(f'Het is nog niet gelukt om de input te converteren: {input_user}')
                    input_is_correct = False
                else:
                    number = self.convert_to_number(input_user)

            if input_is_correct:
                if not self.is_mark(number):
                    print(f'Het getal is kleiner dan 1 en groter dan 10')
                else:
                    input_is_mark = True

        return number

    def ask_all_marks(self, message):
        input_user = None
        counter = 1
        all_marks = []

        while input_user != 'q':
            mark = self.ask_mark(f'{message} {counter}')

            if not mark:
                input_user = 'q'
            else:
                all_marks.append(mark)
                counter += 1

        return all_marks

