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
    punct_re = _punct_re()
    return (
        lambda text: re_sub(punct_re, r' \1 ', text),  # Add whitespace
        lambda text: re_sub(r'\s+', ' ', text).strip(),  # Smooth superfluous whitespace
    )


STEPS = _steps()


def normalize_symbol_boundaries(text: str) -> str:
    """Given a text, inserts whitespace between words, commas, quotations, parens, etc.

    """
    return reduce(lambda x, y: y(x), STEPS, text)
