import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):
    # User story 1
    def test_value_hello_world_returns_hello_world(self):
        piglatin=PigLatin("hello world")
        self.assertEqual("hello world",piglatin.get_phrase())
    def test_value_emptyString_returns_nil(self):
        piglatin=PigLatin("")
        self.assertEqual("nil",piglatin.translate())

