import unittest
from classify_temp_breach import *

class TemperatureClassifierTest(unittest.TestCase):
  def classify_and_test_limit_per_cooling_type(self):
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',-0.01) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',-1) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',-30) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',75) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',36) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',35.1) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',35) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',25) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',0) == 'NORMAL') 

    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',-0.01) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',-1) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',-9) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',150) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',41) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',40.1) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',40) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',33) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',0) == 'NORMAL') 

    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',-0.01) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',-1) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',-18) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',100) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',46) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',45.1) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',45) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',22) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',0) == 'NORMAL') 

if __name__ == '__main__':
  unittest.main()