from nbresult import ChallengeResultTestCase

class TestPreds(ChallengeResultTestCase):
    def test_preds_cols(self):
        """Checks if "preds" "upper" and "lower" are in the columns"""
        self.assertTrue("preds" in self.result.preds_df.columns)
        self.assertTrue("upper" in self.result.preds_df.columns)
        self.assertTrue("lower" in self.result.preds_df.columns)

    def test_df_values(self):
        """Checks if first 'upper' value is greater than 398
        and first 'lower' value is lower than 398"""
        self.assertTrue(self.result.preds_df["upper"][0] > 398)
        self.assertTrue(self.result.preds_df["lower"][0] < 398)
