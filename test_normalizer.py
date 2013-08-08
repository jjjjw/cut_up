from normalizer import normalize_symbol_boundaries
from unittest import TestCase


class TestNormalize(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_sentence = "The sky above the port was the color of television, tuned to a dead channel."
        cls.sample_norm = "The sky above the port was the color of television , tuned to a dead channel ."

    def test_normalizer(self):
        """It should insert whitespace before punctuation.

        """
        res = normalize_symbol_boundaries(self.sample_sentence)
        self.assertEqual(res, self.sample_norm)


if __name__ == '__main__':
    from unittest import main

    main()
