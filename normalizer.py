from re import compile as re_compile
from re import escape as re_escape
from re import sub as re_sub
from string import punctuation


def _punct_re() -> type(re_compile('')):
    """Compile the punctuation substitution regex pattern for use.

    """
    return re_compile(r'([%s])' % re_escape(punctuation))


def normalize_symbol_boundaries(text: str) -> str:
    """Given a text, inserts whitespace between words, commas, quotations, parens, etc.

    """
    return re_sub(r'\s+', ' ', re_sub(_punct_re(), r' \1 ', text)).strip()
