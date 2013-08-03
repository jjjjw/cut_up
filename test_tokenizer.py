import unittest
from unittest import TestCase

class TestMultiSub(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_sentence = "The sky above the port was the color of television, tuned to a dead channel."
        cls.sample_text = "The sky above the port was the color of television, tuned to a dead channel. 'It's not like I'm using,' Case heard someone say, as he shouldered his way through the crowd around the door of the Chat. 'It's like my body's developed this massive drug deficiency.' It was a Sprawl voice and a Sprawl joke. The Chatsubo was a bar for professional expatriates; you could drink there for a week and never hear two words in Japanese. Ratz was tending bar, his prosthetic arm jerking monotonously as he filled a tray of glasses with draft Kirin. He saw Case and smiled, his teeth a webwork of East European steel and brown decay. Case found a place at the bar, between the unlikely tan on one of Lonny Zone's whores and the crisp naval uniform of a tall African whose cheekbones were ridged with precise rows of tribal scars. 'Wage was in here early, with two joeboys,' Ratz said, shoving a draft across the bar with his good hand. 'Maybe some business with you, Case?' Case shrugged. The girl to his right giggled and nudged him."

    def test_word_sub(self):
        """It should return a string with the word substitutions correctly made.

        """
        from multisub import MultiSub

        silly_replacements = MultiSub(
            sky="velociraptor",
            television="paystub",
        )

        res = silly_replacements.sub(self.sample_sentence)
        self.assertEqual(res,
            "The velociraptor above the port was the color of paystub, tuned to a dead channel.")

    def test_regex_sub(self):
        """It should return a string with the regex substitutions correctly made.

        """
        from multisub import MultiSub

        silly_replacements = MultiSub({
            r"\.": "!",
        })

        res = silly_replacements.sub(self.sample_sentence)
        self.assertEqual(res,
            "The sky above the port was the color of television! tuned to a dead channel!")


if __name__ == '__main__':
    unittest.main()

