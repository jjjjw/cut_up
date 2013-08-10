from itertools import chain
from normalizer import Normalizer
from random import Random


def cut_up(text: str, seed: int = 1):
    """An implementation of the [cut-up literary technique]
    (http://en.wikipedia.org/wiki/Cut-up_technique). The seed value allows for repeatable random
    rearrangement.

    """
    # Init our tools
    normalizer = Normalizer()
    random = Random(seed)

    # Normalize the corpus
    tokens = normalizer.normalize_symbol_boundaries(text).split()

    # Segment the tokens and randomize the segments
    blocks = _get_blocks(tokens, random)
    random.shuffle(blocks)

    # Reconstitute and denormalize the corpus
    tokens = list(chain.from_iterable(blocks))
    res = " ".join(tokens)
    res = normalizer.denormalize_symbol_boundaries(res)

    return res


def _get_blocks(tokens: list, random: Random):
    """Chunk the tokens into random blocks.

    """
    tokens_len = len(tokens)
    consume_tokens = list(tokens)
    blocks = []

    while len(consume_tokens) > 0:
        i = random.randint(0, tokens_len)
        try:
            block = consume_tokens[:i]
        except:
            block = consume_tokens

        consume_tokens = consume_tokens[len(block):]
        blocks.append(block)

    return blocks
