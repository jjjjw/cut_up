def cut_up(text: "string", seed=1):
    """An implementation of the [cut-up literary technique]
    (http://en.wikipedia.org/wiki/Cut-up_technique). The seed value allows for repeatable random
    rearrangement.

    TODO: find slices, shuffle slices
    """
    from tokenizer import word_tokenize

    words = word_tokenize(text)

    return words
