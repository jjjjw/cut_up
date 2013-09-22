def fold(corpus: str):
    page = corpus.splitlines()
    midpoint = len(page) // 2
    return page[:midpoint], page[midpoint:]


def fold_in(page1: str, page2: str):
    """An implementation of the [fold-in literary technique]
    (http://en.wikipedia.org/wiki/Cut-up_technique).

    @return str
    """
    res = fold(page1)[0] + fold(page2)[1]
    return "\n".join(res)
