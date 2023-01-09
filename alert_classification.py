from send_control import *
from classify_temp_breach import *
from detect_temp_breach import *

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    alert = send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    alert = send_to_email(breachType)
  return alert