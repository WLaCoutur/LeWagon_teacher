from nbresult import ChallengeResultTestCase

class TestPreprocBaseline(ChallengeResultTestCase):

    def test_shape(self):
        self.assertEqual(self.result.shape[0], 1460,
                         msg="Not the right number of rows. Did you train-test split?")
        self.assertNotEqual(self.result.shape[1], 183,
                            msg="Too many columns. Remember to drop the second column when encoding binary features.")
        # The next test allows two values due to how pandas.read_csv() handles
        # "None" differently since Pandas>=2.0.0 (old 179, new 178)
        self.assertIn(self.result.shape[1], [178, 179],
                      msg="Not the right number of columns.")
