from unittest import TestCase

import ktorrent, json

class kTorrentTest(TestCase):

    def testConnection(self):
        # Check connection
        output = ktorrent.search(search='linux')
        self.failIfEqual(output,"Couldn't retrieve data")

    def testSearch(self):
        # search: Validate JSON
        output = ktorrent.search(search='linux')
        self.assertEqual( type( json.loads(output) ) is dict , True)

    def testTop(self):
        # top: Validate JSON
        output = ktorrent.top(category='movies', page=2)
        self.assertEqual( type( json.loads(output) ) is dict , True)

    def testInvalidArgs(self):
        # Check invalid args
        output1 = ktorrent.search(search='Linux', strict=404, category='book')
        output2 = ktorrent.search(category='books')
        output3 = ktorrent.top(category='movies', page='2')
        self.assertEqual(output1, "Invalid parameters passed")
        self.assertEqual(output2, "Invalid parameters passed")
        self.assertEqual(output3, "Invalid parameters passed")

if __name__ == '__main__':
    unittest.main()
