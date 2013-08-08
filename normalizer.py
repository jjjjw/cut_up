from functools import reduce
from re import compile as re_compile
from re import escape as re_escape
from re import sub as re_sub
from string import punctuation


def _punct_re() -> type(re_compile('')):
    """Compile the punctuation substitution regex pattern for use.

    """
    return re_compile(r'([%s])' % re_escape(punctuation))


def _steps() -> tuple:
    """The normalization steps.

    """
    def add_whitespace(text: str) -> str:
        return re_sub(_punct_re(), r' \1 ', text)

    def smooth_superfluous_whitespace(text: str) -> str:
        return re_sub(r'\s+', ' ', text).strip()

    return (add_whitespace, smooth_superfluous_whitespace)


def normalize_symbol_boundaries(text: str) -> str:
    """Given a text, inserts whitespace between words, commas, quotations, parens, etc.

    """
    return reduce(lambda x, y: y(x), _steps(), text)
