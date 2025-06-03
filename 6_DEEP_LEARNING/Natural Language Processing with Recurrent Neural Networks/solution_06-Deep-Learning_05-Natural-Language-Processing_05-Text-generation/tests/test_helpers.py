from nbresult import ChallengeResultTestCase


class TestHelpers(ChallengeResultTestCase):
    def test_chars_to_ids(self):
        self.assertEqual(self.result.ids, [25, 44, 36, 40, 46, 54, 53])

    def test_ids_to_chars(self):
        self.assertEqual(self.result.chars, b'NLP[UNK]')
