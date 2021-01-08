import unittest
from scripts.HammingCode import HammingCode

class HammingCodeTestCase(unittest.TestCase):

    def test_calc_parity_bits(self):
        data = '1011001'
        h = HammingCode(data)
        hc = h.calc_parity_bits()
        self.assertEqual(hc, 10101001110)


if __name__ == '__main__':
    unittest.main()
