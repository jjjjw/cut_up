from unittest import TestCase


class TestNormalize(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_sentence = "The sky above the port was the color of television, tuned to a dead channel."
        cls.sample_norm = "The sky above the port was the color of television , tuned to a dead channel ."

    def test_normalizer(self):
        """It should insert whitespace before punctuation.

        """
        from normalizer import normalize_symbol_boundaries

        res = normalize_symbol_boundaries(self.sample_sentence)
        self.assertEqual(res, self.sample_norm)

    def test_denormalizer(self):
        """It should remove whitespace before punctuation.

        """
        from normalizer import denormalize_symbol_boundaries

        res = denormalize_symbol_boundaries(self.sample_norm)
        self.assertEqual(res, self.sample_sentence)


if __name__ == '__main__':
    import unittest

    unittest.main()
