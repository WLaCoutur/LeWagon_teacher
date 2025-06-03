from nbresult import ChallengeResultTestCase

class TestMissing(ChallengeResultTestCase):
    def test_missing(self):
        self.assertEqual(self.result.missing, 2861)
