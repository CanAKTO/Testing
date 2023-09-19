import unittest
from mats import mats


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.matt=mats()

    def test_tpla(self):
        result=self.matt.tpla(10,5)

        self.assertEqual(result,15)  # add assertion here

    def test_carp(self):
        result=self.matt.carp(10,5)
        self.assertEqual(result,50)  # add assertion here

if __name__ == '__main__':
    unittest.main()
