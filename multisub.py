class MultiSub(dict):
    """Follows the (recipe)
    [http://code.activestate.com/recipes/81330-single-pass-multiple-replace/]

    """
    def _make_regex(self):
        """Build a regular expression object based on the keys of the current dictionary.

        """
        import re

        return re.compile("(%s)" % "|".join(self.keys()))

    def __call__(self, mo: "MatchObject"):
        """This handler will be invoked for each regex match.

        """
        import re

        capture = mo.group()
        # Allow for both vanilla string matches and regex pattern matches.
        sub = self.get(capture, False) or self.get(re.escape(capture))

        try:
            # Allow lambdas or functions as replacement args.
            return sub(capture)
        except:
            return sub

    def sub(self, text: "string"):
        """Translate text, returns the modified text.

        """
        return self._make_regex().sub(self, text)
