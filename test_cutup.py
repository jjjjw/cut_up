from cutup import cut_up
from unittest import TestCase

class TestCutUp(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_sentence = "The sky above the port was the color of television, tuned to a dead channel."
        cls.cut_up_sentence = ", was channel dead television The of a the the tuned to color sky. above port"

    def test_normalizer(self):
        """It should scramble a text.

        """
        res = cut_up(self.sample_sentence)
        self.assertEqual(res, self.cut_up_sentence)


if __name__ == '__main__':
    from unittest import main

    main()
