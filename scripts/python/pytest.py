"""
This script simply shows that a value is passed, not the object.

If the object had been passed, the final value would be 0, not 99

 

"""

def main ( ) :
      value = 99
      print ' The value is ' , value
      changeme(value)
      print 'Back in main the value is', value
def changeme(arg):
      print 'I am changing the value.'
      arg = 0
      print 'Now the value is ' , arg
# Call the main function.
main ( )

