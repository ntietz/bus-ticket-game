import types


def interpret(text):
    try:
        tokens = tokenize(text)
        symbols = parse(tokens)
        return evaluate(symbols)
    except ZeroDivisionError:
        return None


def tokenize(text):
    return text.split()


def parse(tokens):
    symbols = [token_to_symbol(token) for token in tokens]
    return symbols


def evaluate(symbols):
    """Performs a prefix evaluation of the given symbols.

    Symbols here are parsed tokens, so these will be functions and data rather
    than the raw character strings.

    This assumes everything is well-formed.
    """
    result, remaining = evaluate_helper(symbols)
    return result


def evaluate_helper(symbols):
    # If the head is not an operator, we are either in a single element list
    # or we are evaluating for an operand.
    if not is_operator(symbols[0]):
        return symbols[0], symbols[1:]

    operator, remaining = take_operator(symbols)
    left_operand, remaining = evaluate_helper(remaining)
    right_operand, remaining = evaluate_helper(remaining)
    return operator(left_operand, right_operand), remaining


def is_operator(symbol):
    return isinstance(symbol, types.FunctionType)


def take_operator(symbols):
    return symbols[0], symbols[1:]


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


parsable_tokens = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}
reverse_tokens_map = {v: k for k, v in parsable_tokens.items()}
parsable_digits = '0123456789'


def token_to_symbol(token):
    if token in parsable_tokens:
        return parsable_tokens[token]
    if token in parsable_digits:
        return int(token)
    raise UnrecognizedTokenError


def symbol_to_token(symbol):
    if is_operator(symbol):
        return reverse_tokens_map[symbol]
    return str(symbol)

def to_string(symbols):
    return ' '.join([symbol_to_token(s) for s in symbols])
