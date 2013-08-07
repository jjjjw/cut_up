from re import compile
from re import escape
from re import sub
from string import punctuation


def _pattern() -> type(compile('')):
    """Compile the substitution regex pattern for use.

    """
    punct = escape(punctuation)
    punct = r'([%s])' % punct

    return compile(punct)


PUNCT = _pattern()


def _add_whitespace(text: str) -> str:
    return sub(PUNCT, r' \1 ', text)

def _smooth_superfluous_whitespace(text: str) -> str:
    return sub(r'\s+', ' ', text).strip()


def normalize_symbol_boundaries(text: str) -> str:
    """Given a text, inserts whitespace between words, commas, quotations, parens, etc.

    """
    return _smooth_superfluous_whitespace(_add_whitespace(text))
