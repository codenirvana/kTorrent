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
        output = json.loads( ktorrent.search(search='Linux', strict=404, category='book') )
        self.assertEqual(output['status'], 400)

        output = json.loads( ktorrent.search(category='books') )
        self.assertEqual(output['status'], 400)

        output = json.loads( ktorrent.top(category='movies', page='2') )
        self.assertEqual(output['status'], 400)

if __name__ == '__main__':
    unittest.main()
