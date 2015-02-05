import math

#functions is the group of functions and operators that the module will understand
#all of the definitions will be in uppercase, where applicable. This could/should
#facilitate in converting to a lambda by only searching for lowercase and grouping all of the 
#upper cases together

functions={'+':'+', '^':'**', '**':'**', '-':'-', '/':'/', '*':'*','log':'MATH.LOG', 'pi':'MATH.PI', 'sin':'MATH.SIN', 'cos':'MATH.COS', 'tan':'MATH.TAN' }
types={'number':[48,57]}

def converttofunction(somestring):
  components=[]
  """
  This will accept a string, convert it to a lambda, and then return the lambda
  There are several parts to this, ensuring that everything has the correct 
  assortment of operators (ie knowing that 7x = 7*x, as well as converting all of
  the integers to floats
  """
  somestring=somestring.lower()
  
  while(len(somestring)>0):
    if len(somestring)==1:
      components.append(somestring[:1])
      somestring=''
    else:
      end=1
      if ord(somestring[0])<=57 and ord(somestring[0])>=48:
        while ord(somestring[end])<=57 and ord(somestring[end])>=48:
          end+=1
        components.append(somestring[:end])
        somestring=somestring[end:]
        continue
      elif ord(somestring[0])<=122 and ord(somestring[0])>=97:
        while ord(somestring[end])<=122 and ord(somestring[end])>=97:
          end+=1
        components.append(somestring[:end])
        somestring=somestring[end:]
        continue
      else:
        components.append(somestring[:end])
        somestring=somestring[end:]
        continue
  for part in range(len(components)):
    
  
  return components
