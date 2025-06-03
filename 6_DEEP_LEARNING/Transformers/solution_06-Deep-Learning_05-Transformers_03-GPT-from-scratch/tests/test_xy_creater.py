from nbresult import ChallengeResultTestCase

class TestXyCreater(ChallengeResultTestCase):
    def test_X_shape(self):
        self.assertEqual(self.result.X_shape, (55,56))

    def test_list_length(self):
        self.assertEqual(self.result.list_length, 2)

    def test_type(self):
        self.assertEqual(self.result.y_shape, 55)
