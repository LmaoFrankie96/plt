import unittest
from piglatin import PigLatin
from error import PigLatinError

#User story 1
class TestPigLatin(unittest.TestCase):

    def test_value_hello_world_returns_hello_world(self):
        piglatin=PigLatin("hello world")
        self.assertEqual("hello world",piglatin.get_phrase())
        pass
