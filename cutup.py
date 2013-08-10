from normalizer import Normalizer
from random import Random


def cut_up(text: str, seed: int = 1):
    """An implementation of the [cut-up literary technique]
    (http://en.wikipedia.org/wiki/Cut-up_technique). The seed value allows for repeatable random
    rearrangement.

    """
    normalizer = Normalizer()
    random = Random(seed)
    tokens = normalizer.normalize_symbol_boundaries(text).split()
    random.shuffle(tokens)
    res = " ".join(tokens)
    res = normalizer.denormalize_symbol_boundaries(res)

    return res
