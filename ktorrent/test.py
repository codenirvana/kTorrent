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
        output = ktorrent.top(category='movies', page='2')
        self.assertEqual( type( json.loads(output) ) is dict , True)

if __name__ == '__main__':
    unittest.main()
