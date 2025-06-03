from nbresult import ChallengeResultTestCase

class TestFinalShapes(ChallengeResultTestCase):
    def test_X_shape(self):
        self.assertEqual(self.result.X_shape, [17026, 56])
        
    def test_sample_X_values(self):
        self.assertEqual(self.result.X_value, 401)
        
    def test_y_shape(self):
        self.assertEqual(self.result.y_shape, 17026)
        
    def test_y_value(self):
        self.assertEqual(self.result.y_value, 443)
    
    def test_zeroes(self):
        self.assertEqual(self.result.zeroes, 0, "There are still y values of zero which means you are predicting padding")
