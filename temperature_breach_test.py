import unittest
from detect_temp_breach import *

class TemperatureBreachTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(infer_breach(10, 3, 8) == 'TOO_HIGH')
    self.assertTrue(infer_breach(10, 1, 30) == 'NORMAL')
    self.assertTrue(infer_breach(-2, -10, -5) == 'TOO_HIGH')
    self.assertTrue(infer_breach(-26, -20, 0) == 'TOO_LOW')
    self.assertTrue(infer_breach(-4, -100, -2) == 'NORMAL')

if __name__ == '__main__':
  unittest.main()