from nbresult import ChallengeResultTestCase

class TestDataset(ChallengeResultTestCase):
    def test_input_shape(self):
        self.assertEqual(self.result.input_shape, (64,100))

    def test_output_shape(self):
        self.assertEqual(self.result.output_shape, (64,100))
