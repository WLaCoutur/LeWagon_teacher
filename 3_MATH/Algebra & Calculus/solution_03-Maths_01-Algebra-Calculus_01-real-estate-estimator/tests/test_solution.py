from nbresult import ChallengeResultTestCase


class TestSolution(ChallengeResultTestCase):
    def test_theta_shape(self):
        self.assertEqual(self.result.theta.shape, (4, 1))

    def test_theta0_is_correct(self):
        self.assertAlmostEqual(self.result.theta[0][0], 74, 0)
