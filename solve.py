from itertools import combinations_with_replacement


puzzle_digits = [d for d in range(1, 10)]


def num_puzzles(num_digits):
    def fib(n):
        if n == 1:
            return n
        return n * fib(n - 1)

    return len(list(all_puzzles(num_digits)))


shared_cache = {} # TODO: refactor this to have it as an argument instead


def solvable_puzzles(num_digits, target=100):
    for puzzle in all_puzzles(num_digits):
        cache_key = str(sorted(puzzle))
        if cache_key not in shared_cache:
            shared_cache[cache_key] = is_solvable(puzzle, target)
        if shared_cache[cache_key]:
            yield puzzle
        else:
            print(puzzle)


def all_puzzles(num_digits):
    return combinations_with_replacement(puzzle_digits, num_digits)


def is_solvable(ticket, target=100):
    for val in all_values(ticket):
        if val == target:
            return True
    return False


def all_values(digits):
    if len(digits) == 1:
        yield digits[0]
        return

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



