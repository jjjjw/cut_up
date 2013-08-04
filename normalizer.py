import re


def _make_subs():
    """Compile the substitution regexes for use.

    """
    import string

    punct = re.escape(string.punctuation)
    subs = (
        (r'([%s])' % punct, r' \1 '),
        (r'(\s[%s])' % punct, lambda x: x.group().strip()),
    )
    compiled = []

    for pattern, repl in subs:
        pattern = re.compile(pattern)
        compiled.append(tuple([pattern, repl]))

    return compiled


SUBS = _make_subs()
NORM_PATTERN, NORM_REPL = SUBS[0]
DENORM_PATTERN, DENORM_REPL = SUBS[1]


def normalize_symbol_boundaries(text: "string"):
    """Given a text, inserts whitespace between words, commas, quotations, parens, etc.

    """
    normed = re.sub(NORM_PATTERN, NORM_REPL, text)
    return ' '.join(normed.split())  # Smooth superfluous whitespace


def denormalize_symbol_boundaries(text: "string"):
    """Given a text, removes whitespace between words, commas, quotations, parens, etc.

    """
    return re.sub(DENORM_PATTERN, DENORM_REPL, text)
