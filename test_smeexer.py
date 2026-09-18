import unittest
from mixers import (
    seed_validation,
    stepping_stone_mix,
    odd_even,
    obfuscate,
    fivio_mix,
    odd_one_out_mix,
    onion_ring,
    mnemonic_set
)
from sharding import (
    shard,
    staircase_shard,
    compass_shard,
    seesaw_shard,
    box_shard
)


class TestSmeexerMixers(unittest.TestCase):
    def setUp(self):
        # A valid 12-word sample list using bip0039 words
        self.sample_12 = ["abandon", "ability", "able", "about", "above", "absent",
                           "absorb", "abstract", "absurd", "abuse", "access", "accident"]
        self.sample_24 = ["abandon", "ability", "able", "about", "above", "absent",
                           "absorb", "abstract", "absurd", "abuse", "access", "accident",
                           "account", "accuse", "achieve", "acid", "acoustic", "acquire",
                           "across", "act", "action", "actor", "actress", "actual"]

    def test_seed_validation_valid(self):
        self.assertTrue(seed_validation(self.sample_12))
        self.assertTrue(seed_validation(self.sample_24))

    def test_seed_validation_invalid_length(self):
        self.assertFalse(seed_validation(["abandon", "ability"]))

    def test_seed_validation_invalid_word(self):
        invalid_words = self.sample_12.copy()
        invalid_words[0] = "notabipword123"
        self.assertFalse(seed_validation(invalid_words))

    def test_stepping_stone_mix(self):
        result = stepping_stone_mix(self.sample_12)
        self.assertEqual(len(result), 12)
        expected = ["access", "abandon", "about", "able", "absent", "above",
                    "abstract", "absorb", "abuse", "absurd", "accident", "ability"]
        self.assertEqual(result, expected)

    def test_odd_even(self):
        result = odd_even(self.sample_12)
        self.assertEqual(len(result), 12)

    def test_obfuscate(self):
        result = obfuscate(self.sample_12)
        self.assertEqual(len(result), 24)
        self.assertEqual(result[:12], self.sample_12)
        for word in result[12:]:
            self.assertIn(word, mnemonic_set)

    def test_fivio_mix(self):
        obfuscated = obfuscate(self.sample_12)
        left_res = fivio_mix(obfuscated, "l")
        self.assertEqual(len(left_res), 24)
        right_res = fivio_mix(obfuscated, "r")
        self.assertEqual(len(right_res), 24)

    def test_odd_one_out_mix(self):
        obfuscated = obfuscate(self.sample_12)
        left_res = odd_one_out_mix(obfuscated, "left")
        self.assertEqual(len(left_res), 24)
        right_res = odd_one_out_mix(obfuscated, "right")
        self.assertEqual(len(right_res), 24)

    def test_onion_ring(self):
        res_out = onion_ring(self.sample_12, "out")
        self.assertEqual(len(res_out), 12)
        res_in = onion_ring(self.sample_12, "in")
        self.assertEqual(len(res_in), 12)

    def test_shard(self):
        shards = shard(self.sample_12)
        self.assertEqual(len(shards), 3)
        for s in shards:
            self.assertEqual(len(s), 13)

    def test_staircase_shard(self):
        shards = staircase_shard(self.sample_12)
        self.assertEqual(len(shards), 3)
        for s in shards:
            self.assertEqual(len(s), 12)

    def test_compass_shard(self):
        compass = compass_shard(self.sample_12)
        self.assertIn("North", compass)
        self.assertIn("South", compass)

    def test_seesaw_shard(self):
        seesaw = seesaw_shard(self.sample_12)
        self.assertEqual(len(seesaw), 2)

    def test_box_shard(self):
        box = box_shard(self.sample_12)
        self.assertEqual(len(box), 2)
        self.assertEqual(len(box[0]), 2)


if __name__ == '__main__':
    unittest.main()
