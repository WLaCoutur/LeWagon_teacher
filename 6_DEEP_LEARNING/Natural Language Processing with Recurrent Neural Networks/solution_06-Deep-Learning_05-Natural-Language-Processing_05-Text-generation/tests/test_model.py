from nbresult import ChallengeResultTestCase
from tensorflow.keras.losses import SparseCategoricalCrossentropy as loss

class TestModel(ChallengeResultTestCase):
    def test_loss(self):
        self.assertEqual(self.result.loss, loss)

    def test_output(self):
        self.assertEqual(self.result.output_weights, 66)
