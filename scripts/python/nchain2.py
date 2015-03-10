#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-09 19:47:09
# @Last Modified 2015-03-09
# @Last Modified time: 2015-03-09 22:40:55
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-09 19:47:09
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2015-03-09 19:47:09


# I have been thinking of how to do this on and off all day,
# I wish I could have gotten to the computer earlier!

class numChain(object):

    def __init__(self, numberOfLinks, desiredValue):
        self.numberOfLinks = numberOfLinks
        self.desiredValue = desiredValue
        self.links=[]
        self.links.append(1)
        self.stringGroup=[]
        self.allPotentialValues=set()
        for x in range(numberOfLinks+1):
            self.stringGroup.append([x,])
        print self.calculateNextLinks()
        

    def calculateNextLinks(self):
        potentialNextValues = set()
        currentNumberOfLinks=len(self.links)
        if (self.links[-1]==self.desiredValue):
            return self.links
        elif (currentNumberOfLinks>self.numberOfLinks):
            return False
        else:
            for outterLinkLocation in range(currentNumberOfLinks):
                for innerLinkLocation in range(outterLinkLocation, currentNumberOfLinks):
                    self.allPotentialValues.add(self.links[outterLinkLocation]+self.links[innerLinkLocation])
                    potentialNextValues.add(self.links[outterLinkLocation]+self.links[innerLinkLocation])
            for eachLink in potentialNextValues:
                self.links.append(eachLink)
                done=self.calculateNextLinks()
                if (done):
                    return done
                else:
                    self.links.pop()
            return False

