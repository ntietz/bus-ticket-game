from interpreter import interpret, to_string
from interpreter import parsable_tokens


def solvable_puzzles(num_digits):
    for puzzle in all_puzzles(num_digits):
        if is_solvable(puzzle):
            yield puzzle

puzzle_digits = '0123456789'
def all_puzzles(num_digits):
    if num_digits == 1:
        yield puzzle_digits
    for puzzle in all_puzzles(num_digits - 1):
        for digit in puzzle_digits:
            yield f'{digit}{puzzle}'


def is_solvable(ticket):
    for val in all_values(ticket):
        if val == 100:
            return True
    return False


def all_values(digits):
    if len(digits) == 1:
        yield int(digits)

    for idx, raw_digit in enumerate(digits):
        digit = int(raw_digit)
        rest = digits[:idx] + digits[idx+1:]
        vals = all_values(rest)
        for val in vals:
            yield digit + val
            yield digit - val
            yield digit * val
            if val != 0:
                yield digit / val



