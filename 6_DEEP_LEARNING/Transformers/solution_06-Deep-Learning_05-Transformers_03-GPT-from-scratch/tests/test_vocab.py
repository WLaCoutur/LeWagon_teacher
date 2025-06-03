from nbresult import ChallengeResultTestCase

class TestVocab(ChallengeResultTestCase):
    def test_vocab(self):
        self.assertEqual(self.result.vocab_size, 1150)
