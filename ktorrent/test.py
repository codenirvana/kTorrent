from unittest import TestCase

import ktorrent, json

class kTorrentTest(TestCase):

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
        output =ktorrent.search(search='Linux', strict=404, category='book')
        status = output['status']
        self.assertEqual(status, 400)

        output = ktorrent.search(category='books')
        status = output['status']
        self.assertEqual(status, 400)

        output = ktorrent.top(category='movies', page='2')
        status = output['status']
        self.assertEqual(status, 400)

if __name__ == '__main__':
    unittest.main()
