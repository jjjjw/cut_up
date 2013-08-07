import re
import string


def _pattern():
    """Compile the substitution regex pattern for use.

    """
    punct = re.escape(string.punctuation)
    punct = r'([%s])' % punct

    return re.compile(punct)


PUNCT = _pattern()


def normalize_symbol_boundaries(text: "string"):
    """Given a text, inserts whitespace between words, commas, quotations, parens, etc.

    """
    normed = re.sub(PUNCT, r' \1 ', text)
    normed = re.sub(r'\s+', ' ', normed).strip()  # Smooth superfluous whitespace

    return normed
