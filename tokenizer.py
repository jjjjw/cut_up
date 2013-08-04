from multisub import MultiSub

CLEAN_WORDS = MultiSub({
    r'[^\w\s.]': None, # abbreviations currently unhandled
    r'\.$': None, # sentence periods currently unhandled
})

def word_tokenize(text: "string"):
    """Dramatically simple word tokenizer, returns the list of words.

    """
    text = CLEAN_WORDS.sub(text)
    return text.split()
