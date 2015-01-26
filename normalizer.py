from re import compile as re_compile
from re import escape as re_escape
from re import sub as re_sub
from string import punctuation


class Normalizer():
    @property
    def _punct(self):
        """Get the list of punction as an re escaped string.

        """
        if not hasattr(self, '_punct_initialized'):
            self._punct_initialized = re_escape(punctuation)

        return self._punct_initialized

    @property
    def _punct_re(self):
        """Compile the normalizing punctuation substitution regex pattern for use.

        """
        if not hasattr(self, '_punct_re_initialized'):
            self._punct_re_initialized = re_compile(r'([{}])'.format(self._punct))

        return self._punct_re_initialized

    @property
    def _s_punct_re(self):
        """Compile the denormalizing punctuation substitution regex pattern for use.

        """
        if not hasattr(self, '_s_punct_re_initialized'):
            self._s_punct_re_initialized = re_compile(r'(\s[{}])'.format(self._punct))

        return self._s_punct_re_initialized

    def normalize_symbol_boundaries(self, text: str):
        """Given a text, inserts whitespace around commas, quotations, parens, etc.

        """
        return re_sub(r'\s+', ' ', re_sub(self._punct_re, r' \1 ', text)).strip()

    def denormalize_symbol_boundaries(self, text: str):
        """Given a text, trims leading whitespace before commas, quotations, parens, etc.

        """
        return re_sub(self._s_punct_re, lambda x: x.group()[1:], text)
