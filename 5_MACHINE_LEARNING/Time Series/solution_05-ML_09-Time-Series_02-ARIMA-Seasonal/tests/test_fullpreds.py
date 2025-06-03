from nbresult import ChallengeResultTestCase

class TestFullpreds(ChallengeResultTestCase):
    def test_columns(self):
        """Checks that preds_df has 'full_preds`, `upper_conf`
        and `lower_conf` columns"""
        self.assertTrue("full_preds" in self.result.preds_df.columns)
        self.assertTrue("upper_conf" in self.result.preds_df.columns)
        self.assertTrue("lower_conf" in self.result.preds_df.columns)

    def test_index(self):
        self.assertEqual(str(self.result.preds_df.index[0]),
                         '2013-12-31 00:00:00')
