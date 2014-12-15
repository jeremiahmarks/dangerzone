#

from mypy.physics import constants

def averageVelocity(positionEquation, startTime, endTime):
  """
  The position equation is in the form of a one variable lambda and the 
  
  averagevelocity=(changeinposition)/(timeelapsed)
  """
  startTime=float(startTime)
  endTime=float(endTime)
  vAvg=(positionEquation(startTime)-positionEquation(endTime))/(startTime-endTime)
  
  return vAvg
