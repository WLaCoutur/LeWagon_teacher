from nbresult import ChallengeResultTestCase

class TestTokenization(ChallengeResultTestCase):
    def test_len(self):
        self.assertEqual(self.result.list_length, 372)
        
    def test_type(self):
        self.assertEqual(self.result.contains_tensor, True)
        
    def test_seq_length(self):
        self.assertEqual(self.result.tensor_shape, 56)
