import unittest
from alert_classification import *
from classify_temp_breach import *
from send_control import *

class TypewiseAlertTest(unittest.TestCase):
  def check_and_alert_test(self):
    self.assertTrue(check_and_alert('PASSIVE_COOLING','TO_CONTROLLER',0) == True)
    self.assertTrue(check_and_alert('PASSIVE_COOLING','TO_CONTROLLER',35) == True)
    self.assertTrue(check_and_alert('PASSIVE_COOLING','TO_EMAIL',0) == True)
    self.assertTrue(check_and_alert('PASSIVE_COOLING','TO_EMAIL',35) == True)
    self.assertTrue(check_and_alert('PASSIVE_COOLING','TO_EMAIL',21) == False)

    self.assertTrue(check_and_alert('MED_ACTIVE_COOLING','TO_CONTROLLER',0) == True)
    self.assertTrue(check_and_alert('MED_ACTIVE_COOLING','TO_CONTROLLER',40) == True)
    self.assertTrue(check_and_alert('MED_ACTIVE_COOLING','TO_EMAIL',0) == True) 
    self.assertTrue(check_and_alert('MED_ACTIVE_COOLING','TO_EMAIL',40) == True)
    self.assertTrue(check_and_alert('MED_ACTIVE_COOLING','TO_EMAIL',18) == False)

    self.assertTrue(check_and_alert('HI_ACTIVE_COOLING','TO_CONTROLLER',0) == True)
    self.assertTrue(check_and_alert('HI_ACTIVE_COOLING','TO_CONTROLLER',45) == True)
    self.assertTrue(check_and_alert('HI_ACTIVE_COOLING','TO_EMAIL',0) == False)
    self.assertTrue(check_and_alert('HI_ACTIVE_COOLING','TO_EMAIL',45) == False)
    self.assertTrue(check_and_alert('HI_ACTIVE_COOLING','TO_EMAIL',41) == True)

if __name__ == '__main__':
  unittest.main()