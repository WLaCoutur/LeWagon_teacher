import nbresult
import pandas as pd
import numpy as np
from nbresult import ChallengeResultTestCase


class TestPipe(ChallengeResultTestCase):

    def test_pipe_not_crashing(self):
        self.assertNotEqual(self.result.shape[1], 32,
                            msg="Too many columns. Remember to drop the second column when encoding binary features.")
        self.assertEqual(self.result.shape, (1000, 31))
