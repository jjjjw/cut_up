from normalizer import Normalizer
from unittest import TestCase


class TestNormalize(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.normalizer = Normalizer()
        cls.sample_sentence = "The sky above the port was the color of television, tuned to a dead channel."
        cls.sample_norm = "The sky above the port was the color of television , tuned to a dead channel ."

    def test_normalizer(self):
        """It should insert whitespace before punctuation.

        """
        res = self.normalizer.normalize_symbol_boundaries(self.sample_sentence)
        self.assertEqual(res, self.sample_norm)

    def test_denormalizer(self):
        """It should remove whitespace before punctuation.

        """
        res = self.normalizer.denormalize_symbol_boundaries(self.sample_norm)
        self.assertEqual(res, self.sample_sentence)


if __name__ == '__main__':
    from unittest import main

    main()
