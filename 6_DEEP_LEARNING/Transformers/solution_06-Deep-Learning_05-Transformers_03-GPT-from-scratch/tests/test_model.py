from nbresult import ChallengeResultTestCase

class TestModel(ChallengeResultTestCase):
    def test_params(self):
        self.assertEqual(self.result.params, 2785406)
