def find_the_secret(f):
    # co_consts -> returns a tuple containing the literals used by the bytecode
    _, secret = f.__code__.co_consts
    return secret
