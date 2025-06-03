from nbresult import ChallengeResultTestCase

class TestSeasonal(ChallengeResultTestCase):
    def test_seasonal_year_shape(self):
        self.assertEqual(self.result.seasonal.shape, (12, 2))
    def test_seasonal_column(self):
        self.assertTrue("seasonal_component" in self.result.train.columns)
