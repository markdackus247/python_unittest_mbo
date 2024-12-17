import re
import math

# De functie heb ik van internet gehaald.
# Deze functie controleert of de variabele (item) een float is.
# Voor het item kan een float, int of string worden ingevoerd.
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
        float_pattern = re.compile("^-?[0-9]*.[0-9]*$")
        if float_pattern.match(item) or int_pattern.match(item) or item == 'pi':
            return True
        else:
            return False

print(is_float('pi'))

# Test scenario's:
# item is een integer, bijvoorbeeld: 5, -12 en 0
# item is een float, bijvoorbeeld: 7.3 -0.777 en pi
# item is een string met integer erin, bijvoorbeeld: '7', '12' en '0'
# item is een string met float erin, bijvoorbeeld: '7.3' '-0.777' en 'pi'