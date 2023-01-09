from global_constants import *
from detect_temp_breach import *

def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = 0
  upperLimit = 0
  if coolingType in limits:
    lowerLimit = limits[coolingType]['lowerLimit']
    upperLimit = limits[coolingType]['upperLimit']
  return infer_breach(temperatureInC, lowerLimit, upperLimit)