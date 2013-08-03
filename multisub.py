class MultiSub(dict):
    """Follows the (recipe)
    [http://code.activestate.com/recipes/81330-single-pass-multiple-replace/]

    """
    def _make_regex(self):
        """Build a regular expression object based on the keys of the current dictionary.

        """
        import re

        return re.compile("(%s)" % "|".join(map(re.escape, self.keys())))

    def __call__(self, mo: "MatchObject"):
        """This handler will be invoked for each regex match.

        """
        return self[mo.string[mo.start():mo.end()]]

    def sub(self, text: "string"):
        """Translate text, returns the modified text.

        """
        return self._make_regex().sub(self, text)
