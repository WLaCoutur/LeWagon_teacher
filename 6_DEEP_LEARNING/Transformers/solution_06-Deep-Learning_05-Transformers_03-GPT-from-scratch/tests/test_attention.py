from nbresult import ChallengeResultTestCase

class TestAttention(ChallengeResultTestCase):

    def test_len(self):
        self.assertEqual(self.result.len_output, 2)

    def test_output_shape(self):
        self.assertEqual(self.result.output_shape, [2, 2])

    def test_output_value(self):
        expected_values = [1.0003097, 1.1003097]
        for expected, actual in zip(expected_values, self.result.output_value):
            self.assertAlmostEqual(actual, expected, "Your values seem a little off!")
