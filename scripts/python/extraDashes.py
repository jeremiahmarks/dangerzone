def extraDashes(aString):
  while (aString.count('--')>0):
    aString=aString.replace('--','-')
  return aString
