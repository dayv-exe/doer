def is_valid(*args):
    # returns false if any of the arguments parsed is None
    for v in args:
        if v is None:
            return False
        elif v == "":
            return False
    return True