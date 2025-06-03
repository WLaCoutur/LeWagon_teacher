from nbresult import ChallengeResultTestCase

class TestScore(ChallengeResultTestCase):
    def test_AIC_score(self):
        self.assertTrue(self.result.aic_score < 210.0)
