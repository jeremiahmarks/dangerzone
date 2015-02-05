def hex_spirala(data):
    setranges=lambda x,y: (x+1, x+1+(y*6)-1)
    circleranges={}
    circleranges[0]=[1,1]
    a, b = max(data), min(data)
    circlea=None
    circleb=None
    while(a>circleranges[len(circleranges)-1][1]):
        for x in range(len(circleranges), len(circleranges)+10):
            circleranges[x]=setranges(circleranges[x-1][1], x)
    for x in range(len(circleranges)):
        if not circlea:
            if circleranges[x][0]<=a<=circleranges[x][1]: circlea=x
        if not circleb:
            if circleranges[x][0]<=b<=circleranges[x][1]: circleb=x
    circleaMax=circleranges[circlea][1]
    circlebMax=circleranges[circleb][1]
    distanceaisfrommax=circleaMax-a
    distancebisfrommax=circlebMax-b
    stepsize=circlea
    bstepsize=circleb
    if circlea:
        if distanceaisfrommax/stepsize==0:
            aX=-stepsize
        elif distanceaisfrommax/stepsize==3:
            aX=stepsize
        elif distanceaisfrommax/stepsize==1:
            aX=-stepsize+(distanceaisfrommax%stepsize)

        elif distanceaisfrommax/stepsize==2:
            aX=distanceaisfrommax%stepsize
        elif distanceaisfrommax/stepsize==4:   
            aX=stepsize-(distanceaisfrommax%stepsize)
        elif distanceaisfrommax/stepsize==5:    
            aX=-(distanceaisfrommax%stepsize)
    else:
        aX=0    

    if circleb:

        if distancebisfrommax/bstepsize==0:
            bX=-bstepsize
        elif distancebisfrommax/bstepsize==3:
            bX=bstepsize
        elif distancebisfrommax/bstepsize==1:
            bX=-bstepsize+(distancebisfrommax%bstepsize)
    
        elif distancebisfrommax/bstepsize==2:
            bX=distancebisfrommax%bstepsize
        elif distancebisfrommax/bstepsize==4:   
            bX=bstepsize-(distancebisfrommax%bstepsize)
        elif distancebisfrommax/bstepsize==5:    
            bX=-(distancebisfrommax%bstepsize)    
    else:
        bX=0        
    
    amaxycoord=circlea
    bmaxycoord=circleb
    if circlea:
        if distanceaisfrommax/stepsize==0:
            aY=amaxycoord-2*distanceaisfrommax

        elif distanceaisfrommax/stepsize==1:  
            aY=-amaxycoord-(distanceaisfrommax%stepsize)
        elif distanceaisfrommax/stepsize==2:
            if amaxycoord==1:
                aY=-(2*(amaxycoord))+(distanceaisfrommax%stepsize)
            else:
                aY=-(2*(amaxycoord-1))+(distanceaisfrommax%stepsize)
        elif distanceaisfrommax/stepsize==3:
            aY=-amaxycoord+(distanceaisfrommax%stepsize)
        elif distanceaisfrommax/stepsize==4:  
            aY=amaxycoord+(distanceaisfrommax%stepsize)

        elif distanceaisfrommax/stepsize==5: 
            if amaxycoord==1:
                aY=(2*(amaxycoord))-(distanceaisfrommax%stepsize)
            else:
                aY=(2*(amaxycoord-1))-(distanceaisfrommax%stepsize)

    else:
        aY=0  
        
    if circleb:
        if distancebisfrommax/bstepsize==0:
            bY=bmaxycoord-2*distancebisfrommax

        elif distancebisfrommax/bstepsize==1:  
            bY=-bmaxycoord-(distancebisfrommax%bstepsize)
        elif distancebisfrommax/bstepsize==2:
            if bmaxycoord==1:
                bY=-(2*bmaxycoord)+(distancebisfrommax%bstepsize)
            else:
                bY=-(2*(bmaxycoord-1))+(distancebisfrommax%bstepsize)
        elif distancebisfrommax/bstepsize==3:
            bY=-bmaxycoord+(distancebisfrommax%bstepsize)
        elif distancebisfrommax/bstepsize==4:  
            bY=bmaxycoord+(distancebisfrommax%bstepsize)

        elif distancebisfrommax/bstepsize==5: 
            if bmaxycoord==1:
                bY=(2*bmaxycoord)-(distancebisfrommax%bstepsize)
            else:
                bY=(2*(bmaxycoord-1))-(distancebisfrommax%bstepsize)
            
    else:
        bY=0      
    xdiff=(aX-bX)
    ydiff=(aY-bY)
    
    if xdiff>ydiff:
        dis=xdiff
    if ydiff>xdiff:
        dis=xdiff+(ydiff-xdiff)/2
    
    print aX, aY, bX,bY,circlea,circleb

def hex_spiral(data):
    """
    The map of the circuit consists of a collection of hexagonal elements. The 
    first element in the center is marked as 1 and in a continuing clockwise 
    spiral, the rest of the elements are marked in ascending order ad infinitum. 
    On the map, you can move (connect) through the adjoining edges of the 
    hexagonal elements.

    For example: the distance between elements 6 and 19 is two moves and the 
    distance between 2 and 9 is one move. You must help Nikola find the distance 
    between any two elements on the map.
    """
    
    """
    This copy of the code is only for history's sake. I am currently rewritting
    it and am leaving this copy so I can come back if needed
    """
    setranges=lambda x,y: (x+1, x+1+(y*6)-1)
    circleranges={}
    circleranges[0]=[1,1]
    a, b = max(data), min(data)
    circlea=None
    circleb=None
    #find the circle a is in
    while(a>circleranges[len(circleranges)-1][1]):
        for x in range(len(circleranges), len(circleranges)+10):
            circleranges[x]=setranges(circleranges[x-1][1], x)
            # this ugle statement should appropriatly lengthen the dictionary so that
            # it can find the appropriate circle that a is in
    for x in range(len(circleranges)):
        if not circlea:
            if circleranges[x][0]<=a<=circleranges[x][1]: circlea=x
        if not circleb:
            if circleranges[x][0]<=b<=circleranges[x][1]: circleb=x
    circleaMax=circleranges[circlea][1]
    circlebMax=circleranges[circleb][1]
    distanceaisfrommax=circleaMax-a
    distancebisfrommax=circlebMax-b
    
    
    stepsize=circlea
    bstepsize=circleb
    


    
        
    if circlea:
        #When the number 1 is used it is in the zeroth circle
        #this caused several issues and this seemed like a decent
        #resolution to that particular issue
        
        #also, this bunch of code finds the X coordinate for the 
        #larger of the two circles.
        if distanceaisfrommax/stepsize==0:
            aX=-stepsize
        elif distanceaisfrommax/stepsize==3:
            aX=stepsize
        elif distanceaisfrommax/stepsize==1:
            aX=-stepsize+(distanceaisfrommax%stepsize)

        elif distanceaisfrommax/stepsize==2:
            aX=distanceaisfrommax%stepsize
        elif distanceaisfrommax/stepsize==4:   
            aX=stepsize-(distanceaisfrommax%stepsize)
        elif distanceaisfrommax/stepsize==5:    
            aX=-(distanceaisfrommax%stepsize)
    else:
        aX=0    

    if circleb:
        #this particular section finds the x coordinate of the 
        #smaller of the two numbers

        if distancebisfrommax/bstepsize==0:
            bX=-bstepsize
        elif distancebisfrommax/bstepsize==3:
            bX=bstepsize
        elif distancebisfrommax/bstepsize==1:
            bX=-bstepsize+(distancebisfrommax%bstepsize)
    
        elif distancebisfrommax/bstepsize==2:
            bX=distancebisfrommax%bstepsize
        elif distancebisfrommax/bstepsize==4:   
            bX=bstepsize-(distancebisfrommax%bstepsize)
        elif distancebisfrommax/bstepsize==5:    
            bX=-(distancebisfrommax%bstepsize)    
    else:
        bX=0        
    
    #Now that we have the X coordinates, it is time to find the Y coords
    
    #Starting with the larger of the two numbers:
    amaxycoord=circlea
    bmaxycoord=circleb
    if circlea:
        if distanceaisfrommax/stepsize==0:
            aY=amaxycoord-2*distanceaisfrommax

        elif distanceaisfrommax/stepsize==1:  
            aY=-amaxycoord-(distanceaisfrommax%stepsize)
        elif distanceaisfrommax/stepsize==2:
            if amaxycoord==1:
                aY=-(2*(amaxycoord))+(distanceaisfrommax%stepsize)
            else:
                aY=-(2*(amaxycoord-1))+(distanceaisfrommax%stepsize)
        elif distanceaisfrommax/stepsize==3:
            aY=-amaxycoord+(distanceaisfrommax%stepsize)
        elif distanceaisfrommax/stepsize==4:  
            aY=amaxycoord+(distanceaisfrommax%stepsize)

        elif distanceaisfrommax/stepsize==5: 
            if amaxycoord==1:
                aY=(2*(amaxycoord))-(distanceaisfrommax%stepsize)
            else:
                aY=(2*(amaxycoord-1))-(distanceaisfrommax%stepsize)

    else:
        aY=0  
        
    if circleb:
        if distancebisfrommax/bstepsize==0:
            bY=bmaxycoord-2*distancebisfrommax

        elif distancebisfrommax/bstepsize==1:  
            bY=-bmaxycoord-(distancebisfrommax%bstepsize)
        elif distancebisfrommax/bstepsize==2:
            if bmaxycoord==1:
                bY=-(2*bmaxycoord)+(distancebisfrommax%bstepsize)
            else:
                bY=-(2*(bmaxycoord-1))+(distancebisfrommax%bstepsize)
        elif distancebisfrommax/bstepsize==3:
            bY=-bmaxycoord+(distancebisfrommax%bstepsize)
        elif distancebisfrommax/bstepsize==4:  
            bY=bmaxycoord+(distancebisfrommax%bstepsize)

        elif distancebisfrommax/bstepsize==5: 
            if bmaxycoord==1:
                bY=(2*bmaxycoord)-(distancebisfrommax%bstepsize)
            else:
                bY=(2*(bmaxycoord-1))-(distancebisfrommax%bstepsize)
            
    else:
        bY=0      
    xdiff=(aX-bX)
    ydiff=(aY-bY)
    
    if xdiff>ydiff:
        dis=xdiff
    if ydiff>xdiff:
        dis=xdiff+(ydiff-xdiff)/2
    
    print aX, aY, bX,bY,circlea,circleb
