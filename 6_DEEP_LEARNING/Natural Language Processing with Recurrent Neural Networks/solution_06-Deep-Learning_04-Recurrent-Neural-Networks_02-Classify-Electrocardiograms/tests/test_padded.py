from nbresult import ChallengeResultTestCase

class TestPadded(ChallengeResultTestCase):

     def test_variable_padded_shape(self):
        self.assertEqual(self.result.padded_shape,(87554,187))
