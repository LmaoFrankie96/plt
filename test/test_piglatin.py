import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):
    # User story 1
    def test_value_hello_world_returns_hello_world(self):
        piglatin=PigLatin("hello world")
        self.assertEqual("hello world",piglatin.get_phrase())
    # User Story 2
    def test_value_emptyString_returns_nil(self):
        piglatin = PigLatin("")
        self.assertEqual("nil",piglatin.translate())
    #User Story 3
    def test_value_startsWithAVowel_and_wordEndsWithY_returns_wordAppendedWithNay(self):
        piglatin=PigLatin("any")
        self.assertEqual("anynay",piglatin.translate())
    def test_value_startsWithAVowel_and_wordEndsWithVowel_returns_wordAppendedWithYay(self):
        piglatin = PigLatin("apple")
        self.assertEqual("appleyay",piglatin.translate())
    def test_value_startsWithAVowel_and_wordEndsWithConsonantThatIsNotY_returns_wordAppendedWithAy(self):
        piglatin = PigLatin("ask")
        self.assertEqual("askay",piglatin.translate())
    #User Story 4
    def test_value_startsWithSingleConsonant_returns_word_WithConsonantAtEnd_AppendedWith_ay (self):
        piglatin = PigLatin("hello")
        self.assertEqual("ellohay",piglatin.translate())