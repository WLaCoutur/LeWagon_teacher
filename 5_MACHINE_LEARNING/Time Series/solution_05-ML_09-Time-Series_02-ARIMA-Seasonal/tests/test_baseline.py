from nbresult import ChallengeResultTestCase

class TestBaseline(ChallengeResultTestCase):
    def test_missing(self):
        self.assertTrue("naive_preds" in self.result.test.columns)

    def test_first_value(self):
        self.assertAlmostEqual(self.result.test["naive_preds"][0],
                               395.360667,
                               places=1)
    def test_baseline_mae(self):
        self.assertAlmostEqual(self.result.baseline_mae,
                         14.5,
                         places = 1)
