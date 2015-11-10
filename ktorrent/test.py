from unittest import TestCase

import ktorrent, json

class TestSearch(TestCase):
    def test_valid_json(self):
        s = ktorrent.search(search='linux')
        self.assertTrue( json.loads(s) )
