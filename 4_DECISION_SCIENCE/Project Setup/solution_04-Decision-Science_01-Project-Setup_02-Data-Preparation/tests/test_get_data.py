from nbresult import ChallengeResultTestCase


class TestGetData(ChallengeResultTestCase):
    def test_len(self):
        self.assertEqual(self.result.keys_len, 9)

    def test_columns(self):
        self.assertListEqual(
            self.result.columns, [
                'seller_city',
                'seller_id',
                'seller_state',
                'seller_zip_code_prefix'
            ]
        )

    def test_keys(self):
        keys = ['customers', 'geolocation', 'order_items', 'order_payments',
                'order_reviews', 'orders', 'product_category_name_translation',
                'products', 'sellers']
        self.assertListEqual(self.result.keys, keys)

    def test_using_dunder_file(self):
        """Test if the code uses __file__ in the logic.
        If the code doesn't use __file__, it will fail when called from another directory.
        """
        self.assertTrue('__file__' in self.result.vars_used,
                        msg="__file__ not used in your method. It will fail when called from another directory.")
