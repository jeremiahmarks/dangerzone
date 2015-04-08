import sys


sys.path.append('/home/jlmarks/dangerzone/scripts/p1')
from turtleRelated import fvh

class particle(object):
    """
        The particle class will implement a turtle that has
        the ability to determine if it has impacted something
        and then react progmatically. It will initially only
        support to drive a predetermined path, but user input
        may come into play
    """

    def __init__(self):
        self.lm=fvh.MyTurtle()
        self.lm.setup()
        self.velocity=0
        