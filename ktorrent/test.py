from unittest import TestCase

import ktorrent

class FailureMessageTest(TestCase):

    def testFail(self):
        output = ktorrent.search(search='linux')
        self.failIfEqual(output,"Couldn't retrieve data.")

if __name__ == '__main__':
    unittest.main()
