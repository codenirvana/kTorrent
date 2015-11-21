from unittest import TestCase

import ktorrent, json

class kTorrentTest(TestCase):

    def testConnection(self):
        output = ktorrent.search(search='linux')
        self.failIfEqual(output,"Couldn't retrieve data.")

    def testOutput(self):
        output = ktorrent.search(search='linux')
        self.assertEqual( type( json.loads(output) ) is dict , True)

if __name__ == '__main__':
    unittest.main()
