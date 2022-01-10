import doctest
import unittest
import json
import wordle.wordle as wrdle



class TestPhase(unittest.TestCase):

    def test_find_word(self):
        wrdle.find_word()

    def test_calculate_permutations(self):
        with open('../../resources/wordle/basic_permutation.json') as config_file:
            config = json.loads(config_file.read())
        words = wrdle.calculate_permutations(config, [], '', 0)
        self.assertEqual(27, len(words))

    def test_calculate_permutations_valid(self):
        with open('../../resources/wordle/valid_letters.json') as config_file:
            config = json.loads(config_file.read())
        words = wrdle.calculate_permutations(config, [], '', 0)
        print(*words)
        self.assertEqual(21, len(words))

    def test_calculate_permutations_failure(self):
        with open('../../resources/wordle/failure_config.json') as config_file:
            config = json.loads(config_file.read())
        words = wrdle.calculate_permutations(config, [], '', 0)
        print(*words)
        self.assertEqual(21, len(words))

    def test_check_word(self):
        with open('../../resources/wordle/test_config.json') as config_file:
            config = json.loads(config_file.read())
        words = 'ceecc alert beecd'
        wrdle.check_word(config['payload_start'], words, config['payload_end'])


if __name__ == "__main__":
    unittest.main()
    doctest.testmod()
