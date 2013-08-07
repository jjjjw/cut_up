from normalizer import normalize_symbol_boundaries


def cut_up(text: "string", seed=1):
    """An implementation of the [cut-up literary technique]
    (http://en.wikipedia.org/wiki/Cut-up_technique). The seed value allows for repeatable random
    rearrangement.

    TODO: find slices, shuffle slices
    """

    tokens = normalize_symbol_boundaries(text).split()

    return tokens
