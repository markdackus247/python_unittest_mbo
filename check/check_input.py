from check.input import is_mark

assert is_mark(0.9) == False
assert is_mark(1.0) == True
assert is_mark(10.0) == True
assert is_mark(10.1) == False