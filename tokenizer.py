from multisub import MultiSub

CLEAN_WORDS = MultiSub({
    r'[^\w\d\s.]': None,
    r'\.|!|\?': None, # abbreviations currently unhandled
})

def word_tokenize(text: "string"):
    """Dramatically simple word tokenizer, returns the list of words.

    """
    text = CLEAN_WORDS.sub(text)
    return text.split()
