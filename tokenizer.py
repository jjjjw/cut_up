from multisub import MultiSub

# Hygienic replacements
QUOTATIONS = MultiSub({
    r'^\"': r'``',
    r'(``)': r' \1 ',
    r'([ (\[{<])"': r'\1 ``',
})

PUNCTUATION = MultiSub({
    r'([:,])([^\d])': r' \1 \2',
    r'\.\.\.': r' ... ',
    r'[;@#$%&]': r' \g<0> ',
    r'([^\.])(\.)([\]\)}>"\']*)\s*$': r'\1 \2\3 ',
    r'[?!]': r' \g<0> ',
    r"([^'])' ": r"\1 '",
})

# List of contractions adapted from Robert MacIntyre's tokenizer.
CONTRACTIONS = MultiSub({
    r"(?i)\b(can)(not)\b": r' \1 \2 ',
    r"(?i)\b(d)('ye)\b": r' \1 \2 ',
    r"(?i)\b(gim)(me)\b": r' \1 \2 ',
    r"(?i)\b(gon)(na)\b": r' \1 \2 ',
    r"(?i)\b(got)(ta)\b": r' \1 \2 ',
    r"(?i)\b(lem)(me)\b": r' \1 \2 ',
    r"(?i)\b(mor)('n)\b": r' \1 \2 ',
    r"(?i)\b(wan)(na) ": r' \1 \2 ',
    r"(?i) ('t)(is)\b": r' \1 \2 ',
    r"(?i) ('t)(was)\b": r' \1 \2 ',
})

def word_tokenize( text: "string"):
    """The tokenizer creates a cleaned list of words and punctuation.
    Adapted/copied from NLTK's (tokenizer)
    [https://github.com/nltk/nltk/blob/master/nltk/tokenize/treebank.py]

    Uses single pass multiple replace where this makes sense, following the (recipe)
    [http://code.activestate.com/recipes/81330-single-pass-multiple-replace/]

    (When NLTK works with python 3, the NLTK tokenizer module can be more or less
    used as a drop in replacement, the key difference being the handling of sentences.)

    """
    text = _clean_quotations(text)
    text = _clean_punctuation(text)
    text = _clean_contractions(text)
    return text.split()

def _clean_quotations(text: "string"):
    return QUOTATIONS.sub(text)

def _clean_punctuation(text: "string"):
    return PUNCTUATION.sub(text)

def _clean_contractions(text: "string"):
    return CONTRACTIONS.sub(text)
