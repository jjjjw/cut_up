from cut_up import _get_blocks
from cut_up import cut_up
from random import Random
from unittest import TestCase


class TestCutUp(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_sentence = "The sky above the port was the color of television, tuned to a dead channel."
        cls.cut_up_sentence = "The sky above the the color of television, tuned to a port was dead channel."
        cls.sample_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    def test_cut_up(self):
        """It should scramble a text.

        """
        res = cut_up(self.sample_sentence)
        self.assertEqual(res, self.cut_up_sentence)

    def test_get_blocks(self):
        """It should create discrete sublists.

        """
        random = Random(1)
        res = _get_blocks(self.sample_list, random)
        self.assertTrue(len(res) == 2)
        self.assertRaises(ValueError, res[1].index, res[0][-1])


if __name__ == '__main__':
    from unittest import main

    main()
