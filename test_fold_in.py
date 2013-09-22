from fold_in import fold_in
from unittest import TestCase


class TestCutUp(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_page1 = "The sky above the port was the color of television, tuned to a dead channel.\n It's not like I'm using,\" Case heard someone say, as he shouldered his way through the crowd around the door of the Chat. \"It's like my body's developed this massive drug deficiency.\"It was a Sprawl voice and a Sprawl joke. The Chatsubo was a bar for professional expatriates; you could drink there for a week and never hear two words in Japanese."
        cls.sample_page2 = "Call me Ishmael.\n Some years ago - never mind how long precisely - having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world."
        cls.recombination = "The sky above the port was the color of television, tuned to a dead channel.\n Some years ago - never mind how long precisely - having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world."

    def test_fold_in(self):
        """It should fuse the two pages.

        """
        res = fold_in(self.sample_page1, self.sample_page2)
        self.assertEqual(res, self.recombination)


if __name__ == '__main__':
    from unittest import main

    main()
