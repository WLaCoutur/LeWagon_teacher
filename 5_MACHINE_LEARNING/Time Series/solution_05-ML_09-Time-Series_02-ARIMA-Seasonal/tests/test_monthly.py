from nbresult import ChallengeResultTestCase

class TestMonthly(ChallengeResultTestCase):
    def test_missing(self):
        self.assertEqual(self.result.monthly.shape, (594, 1))
    def test_first_value(self):
        self.assertAlmostEqual(self.result.monthly["CO2 molfrac (ppm)"][0],
                               333.156923,
                               places=1)
