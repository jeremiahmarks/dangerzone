FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
                         "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                            "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
                            "eighty", "ninety"]
HUNDRED = "hundred"

testMaze=[     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]



def speechmodule(number):
    """
    This module is intended to turn the int(number) into a string representation
    of that number. 
    """
    stringRep=''
    firstDig,lastDigs=divmod(number,100)
    
    if number==0:
        stringRep="zero"
    
    else:
        if (firstDig !=0):
            stringRep=stringRep+FIRST_TEN[firstDig]+" "+HUNDRED+" "
        
        if (10<=lastDigs<=19):
            stringRep=stringRep+SECOND_TEN[lastDigs%10]+' '
            
        if (0<lastDigs<=9):
            stringRep=stringRep+FIRST_TEN[lastDigs%10]+' '
            
        if (lastDigs>=20):
            stringRep=stringRep+OTHER_TENS[(lastDigs/10)-2]+' '
            if (lastDigs%10 !=0):
                stringRep=stringRep+FIRST_TEN[lastDigs%10]+' '
    
    return ' '.join(stringRep.split())
            
def xoRef(game_result):
    """
    This module is intended to accept a list of rows from a tic-tac-toe game and
    determine who the winner is. It will return X, O or D for X, O or Draw
    
    a sample result would be:
    
    game_result=[u'OO.', u'XOX', u'XOX']
    """
    winner='D'
    
    #check horiz winner
    for x in range(3):
        row=game_result[x]
        if (row[0]==row[1]==row[2]):
            winner=row[0].upper()
    
    #check vert winner
    if(winner=='D'):
        for y in range(3):
            if(game_result[0][y]==game_result[1][y]==game_result[2][y]):
                winner=game_result[0][y]
    
    if(winner=='D'):
        if(game_result[0][0]==game_result[1][1]==game_result[2][2]):
            winner=game_result[0][0]
    
    if (winner=='D'):
        if(game_result[0][2]==game_result[1][1]==game_result[2][0]):
            winner=game_result[1][1]
            
    return winner
    
def convtoroman(data):
    """
    This module is designed to accept a numeral and then convert it to its 
    value in roman numerals. It should accept values between 1 and 3999
    """
    I=(1,'I')
    V=(5,'V')
    X=(10,'X')
    L=(50,'L')
    C=(100,'C')
    D=(500,'D')
    M=(1000,'M')
    
    allvals=[I,V,X,L,C,D,M]
    
    romanstring=''
    
    thousands=data/1000
    hundreds=(data/100)%10
    tens=(data/10)%10
    ones=data%10
    
 
    for m in range(thousands):
        romanstring=romanstring+M[1]

    if hundreds==4:
        romanstring=romanstring+"CD"
    elif hundreds==9:
        romanstring=romanstring+"CM"
    else:
        for d in range(hundreds/5):
            romanstring=romanstring+D[1]
        for c in range(hundreds%5):
            romanstring=romanstring+C[1]
    if tens==4:
        romanstring=romanstring+"XL"
    elif tens==9:
        romanstring=romanstring+"XC"
    else:
        for l in range(tens/5):
            romanstring=romanstring+L[1]
        for x in range(tens%5):
            romanstring=romanstring+X[1]
    
    if ones==4:
        romanstring=romanstring+"IV"
    elif ones==9:
        romanstring=romanstring+"IX"
    else:
        for v in range(ones/5):
            romanstring=romanstring+V[1]
        for i in range(ones%5):
            romanstring=romanstring+I[1]
    return romanstring
    
def morseClock(timeinstringformat):
    """
    This module will accept the time in a string format and return
    a morse code representation of the time. the input string can be 
    formatted in a number of ways, with either 1 or 2 positions listed
    in each h/m/s field, but each field will be seperated by a :
    """
    places=[2,4,3,4,3,4]
    furtherSplit=[]
    returnstring=""
    splitTime=timeinstringformat.split(":")
    for eachpart in range(len(splitTime)):
        working="%02d" %int(splitTime[eachpart])
        tempa="%0"+str(places[2*eachpart])+"d"
        tempb="%0"+str(places[2*eachpart+1])+"d"
        furtherSplit.append(tempa %int(bin(int(working[0]))[2:]))
        furtherSplit.append(tempb %int(bin(int(working[1]))[2:]))
        furtherSplit.append(':')
    for place in furtherSplit:
        for eachchar in place:
            if eachchar==':':
                returnstring=returnstring+":"
            if eachchar=='0':
                returnstring=returnstring+"."
            if eachchar=="1":
                returnstring=returnstring+"-"
        returnstring=returnstring+" "
    
    return returnstring.strip()[:-1]
    
def openLabyrinth(data):
    """
    This module accepts a list of lists representing a maze. The 
    player starts at location [1,1] (with the origin being in the top
    left hand corner of the coordinate system) and must find a path
    to cell (10,10). 1's are a bottomless pit, and 0's are pathway.
    The module will return a string representation of a safe path, 
    indicated by N,S,E, and W. 
    """
    N=(-1,0,'N')
    S=(1,0,'S')
    E=(0,1,'E')
    W=(0,-1,'W')

    STARTPOS=(1,1)
    ENDPOS=(10,10)
    currentPos=(1,1)
    roomsWithMovesLeft=[]
    directions=[N,E,S,W]
    escapeString=""
    circular=['NS','SN','EW','WE']
    
    for x in range(len(data)):
        for y in range(len(data[0])):
            data[x][y]=[data[x][y],]
    for x in range(len(data)):
        for y in range(len(data[0])):
            options=[data[x][y][0],]            
            if data[x][y][0]==0:
                for z in range(4):
                    testx, testy = x+directions[z][0], y+directions[z][1]
                    if(0<testx<12 and 0<testy<12 and data[testx][testy][0]==0):
                        options.append([directions[z],False])
            data[x][y]=options
    
    while(currentPos!=ENDPOS):
        canMove=False
        cp=data[currentPos[0]][currentPos[1]]
        movesFromHere=0
        for choice in range(1,len(cp)):
            if cp[choice][1]==False:
                movesFromHere+=1
        if movesFromHere>1:
            roomsWithMovesLeft.append([(currentPos[0],currentPos[1]),escapeString])
        for choice in range(1,len(cp)):
            if cp[choice][1]==False:
                canMove=True
                currentPos=(currentPos[0]+cp[choice][0][0], currentPos[1]+cp[choice][0][1])
                escapeString=escapeString+cp[choice][0][2]
                cp[choice][1]=True
                break
        if not canMove:
            backup=roomsWithMovesLeft.pop()
            currentPos=backup[0]
            escapeString=backup[1]
        
        while True:
            newescapeString=escapeString
            for circularComb in circular:
                escapeString=escapeString.replace(circularComb,'')
            if newescapeString==escapeString:
                break
            
    return escapeString

def allinarow(data):
    
    newlist=[]
    for item in data:
        if type(item)==type([]):
            templist=allinarow(item)
            for anitem in templist:
                newlist.append(anitem)
        else:
            newlist.append(item)
    return newlist
    
def primepalendrome(data):

    prime=False
    palindrome=False
    
    while not(prime and palindrome):
        
        prime=False
        if (data%2):
            prime=True
            for x in range(3, int(data**0.5+1),2):
                if data%x==0: 
                    prime=False
                    break
        dataasstr=str(data)
        datareversed=reversed(dataasstr)
        revdatastr=''
        for x in range(len(dataasstr)):
            revdatastr=revdatastr+datareversed.next()
        palindrome=(dataasstr==revdatastr)
        data+=1
    return data-1

def fixthegen(data):
    
    """"
    Data given will be a list of integers representing different potential sides
    to a triangle. out of the unique triangles available this module will 
    return the number of combinations that will not form a triangle.
    
    EX: 
        input: [5,2,9,6]
            possible triangles are:
                5,2,9 != triangle
                5,2,6 == triangle
                5,9,6 == triangle
                2,9,6 != triangle
        output: 2
    """"
    nottriangles=0
    import itertools
    data=list(itertools.combinations(data,3))
    for item in data:
        if (item[0]+item[1]<item[2] or item[0]+item[2]<item[1] or item[1]+item[2]<item[0]):
            nottriangles+=1
    return nottriangles
    
def simpleeq(data):
    """
    You are given four positive integers: A, B, C, N. If 0 ≤ a ≤ A, 0 ≤ b ≤ B 
    and 0 ≤ c ≤ C, using these integers you should try to calculate the number 
    of possible solutions to the following equation: a + b + c ≤ N.
    """
    numberofsols=0
    for a in range(data[0]+1):
        for b in range(data[1]+1):
            for c in range(data[2]+1):
                if (a+b+c<=data[3]):numberofsols+=1
                
    return numberofsols
    
def atm(balance, withdrawal):
    """
     Teach Sofia how to use an ATM. The ATM on their home island can only 
     dispense $5 bills which means that the machine will not dispense any amount
     of money that is not divisible by $5. In addition to that, the bank fee 
     for each withdrawal is $1. The robots cannot withdraw any amount above the
     card’s balance. Also the ATM can not process negative value.

    Input: Two arguments: the first one denotes the robot’s account balance, and the
    second is a list of the monetary amounts that the robot wants to withdraw.

    Output: The account balance after all operations. An integer. 
    """
    for amount in withdrawal:
        if (amount>0 and amount%5==0 and balance>amount):
            balance=balance-(amount+1)
    return balance
    
def ship_purchase(data):

    """
    Write a program that will (depending on Sofia and the old man’s initial 
    bargaining sums--the steps by which they will increase or decrease the price 
    during their negotiations) calculate which final price they will agree upon. 
    If Sofia's offer is lower than or equal to the old man's offer, she will 
    accept the old man's price and vice versa.

    Sofia makes her offer first. She never offers an amount higher than what is 
    offered to her. On the other hand, the old man never offers an amount lower 
    than what is offered to him.
    Input data: Contains four integer numbers: Sofia's initial offer, Sofia's 
    raise to her offer, the initial counteroffer from the old man, and the old 
    man's reduction in his offer;
    Output data: The amount of money that Sofia will pay for the spaceship.
    """
    
    initial_sofi, raise_sofi, initial_oldman, reduction_oldman = data
    
    offers=[(initial_sofi, initial_oldman)]
    onnumber=0
    
    pricechange= lambda x : (initial_sofi+x*raise_sofi, initial_oldman-x*reduction_oldman)
    
    while True:
        offers.append(pricechange(onnumber+1))
        if (offers[onnumber][0]>=offers[onnumber][1]):
            return offers[onnumber][0]
        elif (offers[onnumber][1]<=offers[onnumber+1][0]):
            return offers[onnumber][1]
        else: onnumber+=1
        
def dest_in_spiral(data):
    """
    The map of the circuit consists of square cells. The first element in the 
    center is marked as 1, and continuing in a clockwise spiral, the other 
    elements are marked in ascending order ad infinitum. On the map, you can 
    move (connect cells) vertically and horizontally. For example, the distance 
    between cells 1 and 9 is two moves and the distance between 24 and 9 is one 
    move. You must help Nikola find the distance between any two elements on the 
    map.

    Input: A list of two marks of cells (integers).

    Output: The distance between the two elements. An Integer.
    
    Find the nearest square number that the larger of the two numbers is less than.
    
    if the nearest square number is odd it can move down sqrt(nearestsquare)-1 digits
    and then left the same number. determine it's location with 1 being the origin
    
    
     
    
     
    """
    a,b=max(data),min(data)
    nearestSquare=lambda x: int(x**0.5) if (float(int(x**0.5))==x**0.5) else 1+int(x**0.5)
    NRA=nearestSquare(a) # nearest square of a
    NSA=NRA**2   # nearest root of a
    NRB=nearestSquare(b)
    NSB=NRB**2
    

    
    
    stepsfromNSA=NSA-a
    if NRA%2!=0:
        if stepsfromNSA>(NRA-1):
            aY=0
            aX=stepsfromNSA-(NRA-1)
        else:
            aX=0
            aY=(NRA-1)-stepsfromNSA
    else:
        if stepsfromNSA>(NRA-1):
            aY=NRA-1
            aX=(NRA-1)-(stepsfromNSA-(NRA-1))
        
        else:
            aX=NRA-1
            aY=stepsfromNSA
    
    offset=(NRA-NRB)/2 
    if (NRB%2==0 and NRB%2 != NRA %2):
        offset+=1
    stepsfromNSB=NSB-b
    if NRB%2!=0:
        if stepsfromNSB>(NRB-1):
            bY=0
            bX=stepsfromNSB-(NRB-1)
        else:
            bX=0
            bY=(NRB-1)-stepsfromNSB
    else:
        if stepsfromNSB>(NRB-1):
            bY=NRB-1
            bX=(NRB-1)-(stepsfromNSB-(NRB-1))
        
        else:
            bX=NRB-1
            bY=stepsfromNSB
    bX,bY= bX+offset, bY+offset
            
    distance=(((aX-bX)**2)**0.5)+(((aY-bY)**2)**0.5)
    return distance   


    
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
    setranges=lambda x,y: [x+1, x+1+(y*6)-1]
    a, b = data
    layera=None #These variables will be used to hold which layer of the hexagrams
    layerb=None #each number is in. The zeroth layer has the number 1, the first layer
                #has 2-7, the second layer has 8-20, and so on.
    
    
    
    currentlayer=0   #This variable will be useful to find the layer that each number is in
    layerminmax=[1,1]#This variable will hold the min and max of each layer
    
    while (not layera or not layerb):
        if (layerminmax[0]<=a<=layerminmax[1]): layera=[currentlayer,layerminmax]
        if (layerminmax[0]<=b<=layerminmax[1]): layerb=[currentlayer,layerminmax]
        currentlayer+=1
        layerminmax=setranges(layerminmax[1],currentlayer)
    
    info=[[a,layera],[b,layerb]]


    for number in info:
        #format of number = [number, [layer, [layermin, layermax]]]
        #          number     [0]     [1][0]  [1][1][0]  [1][1][1]
        #the end format   = [number, [layer, [layermin, layermax]], (xcoord, ycoord)]
        layermax=number[1][1][1]
        distancefrommax=layermax-number[0]
        stepsize=number[1][0]
        #special cases:
            #The number that is in the first position is a special case, and, due
            #to multiplication by zero when finding the y coordinates,  the 
            #2 and 5 in first layer are special cases as well
        
        if number[0]==1:
            number.append((0,0))
            continue
        else:
            if distancefrommax/stepsize==0:
                xcoord=-stepsize
            elif distancefrommax/stepsize==3:
                xcoord=stepsize
            elif distancefrommax/stepsize==1:
                xcoord=-stepsize+(distancefrommax%stepsize)
            elif distancefrommax/stepsize==2:
                xcoord=distancefrommax%stepsize
            elif distancefrommax/stepsize==4:   
                xcoord=stepsize-(distancefrommax%stepsize)
            elif distancefrommax/stepsize==5:    
                xcoord=-(distancefrommax%stepsize)
            
            if distancefrommax/stepsize==0:
                ycoord=stepsize-2*distancefrommax
            elif distancefrommax/stepsize==1:  
                ycoord=-stepsize-(distancefrommax%stepsize)
            elif distancefrommax/stepsize==2:
                ycoord=-(2*(stepsize))+(distancefrommax%stepsize)
            elif distancefrommax/stepsize==3:
                ycoord=-stepsize+(distancefrommax%stepsize)
            elif distancefrommax/stepsize==4:  
                ycoord=stepsize+(distancefrommax%stepsize)
            elif distancefrommax/stepsize==5: 
                ycoord=(2*(stepsize))-(distancefrommax%stepsize) 
               
        number.append((xcoord,ycoord))
    xdiff=((info[0][2][0]-info[1][2][0])**2)**0.5
    ydiff=((info[0][2][1]-info[1][2][1])**2)**0.5
    
    if xdiff>=(ydiff):
        dis=xdiff
    else:
        dis=xdiff+round((ydiff-xdiff)/2)
    return int(dis)


def bullet_wall(data):
    """
    The wall is represented by two coordinates W1 (xw1, yw1) and W2 (xw2, yw2) 
    on a coordinate plane. The bullet flies from point "A" (xa, ya), and the 
    direction of its flight is given by the second point "B" (xb, yb). 
    Determine whether the bullet hits the wall or not if gravity is not a 
    factor. A != B.



    Input: A list with coordinates in next order W1, W2, A, B. Each coordinate 
    is a list of x and y coordinates (int).

    Output: Whether the bullet hits the wall or not. A boolean.
    
    plan, use the bullet to construct a line using point slope form
    
    if one point is below the line and another point is above it, it 
    intersects, else it does not
    
    """

    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya = data[2]
    xb, yb = data[3]
    
    #check if the wall is behind the gun
    
    
    
    if ((xa-xb)/(xa-xw1)>0 or (ya-yb)/(ya-yw1>0)):
        hits=(False, "The wall is behind the gun")
    
    elif ((xb,yb)==(xw1,yw1) or (xb,yb)==(xw2,yw2)):
        hits= (True, "The aim point is the wall")
    elif (xa-xb)!=0:
        mgun=float(ya-yb)/(xa-xb)
        bgun=-(mgun*xa-ya)
        guneq = lambda x: mgun*x+bgun
        if (xw1-xw2)!=0:
            mwall=float(yw1-yw2)/(xw1-xw2)
            bwall=mwall*xw1-yw1
            xvalue=(bgun-bwall)/(mwall-mgun)
                
            hits= ((min(xw1,xw2) <= xvalue <= max(xw1,xw2)), mgun, bgun, guneq, mwall, bwall, xvalue)
                
        else:
            hits= ((min(yw1,yw2) <= guneq(xw1) <= max(yw1,yw2)), mgun, bgun, guneq)
    else:
        hits= (min(xw1,xw2) <= xa <= max(xw1,xw2))
    
	# if the line is below the wall at one point and above it in the other in the direction
	# of the bullets trajectory, it hit the wall
    
    # issues to be aware of, if the wall extends to the right and below of 
    
    return hits


def bullet_walla(data):
    """
    The wall is represented by two coordinates W1 (xw1, yw1) and W2 (xw2, yw2) 
    on a coordinate plane. The bullet flies from point "A" (xa, ya), and the 
    direction of its flight is given by the second point "B" (xb, yb). 
    Determine whether the bullet hits the wall or not if gravity is not a 
    factor. A != B.



    Input: A list with coordinates in next order W1, W2, A, B. Each coordinate 
    is a list of x and y coordinates (int).

    Output: Whether the bullet hits the wall or not. A boolean.
    
    plan, use the bullet to construct a line using point slope form
    
    if one point is below the line and another point is above it, it 
    intersects, else it does not
    
    """

    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya = data[2]
    xb, yb = data[3]
    guneq=walleq=None
    shotType=wallType=''    
    
    if ((xb,yb)==(xw1,yw1) or (xb,yb)==(xw2,yw2)):
        hits=True #The aimpoint is part of the wall
    
    if (xa-xb)!=0:
        mgun=float(ya-yb)/(xa-xb)
        bgun=-(mgun*xa-ya)
        guneq = lambda x: mgun*x+bgun
    else:
        shotType="Vertical"
        
    if (xw1-xw2)!=0:
        mwall=float(yw1-yw2)/(xw1-xw2)
        bwall=mwall*xw1-yw1
        walleq= lambda x: mwall*x+bwall
    else:
        wallType="Vertical"
        
    if (guneq and walleq):
        xvalue=(bgun-bwall)/(mwall-mgun) #The xvalue is the value where the equations
                                         #for each line intersect
        
        if (((xa-xb)/(xa-xvalue))>0) and (min(yw1,yw2)<=guneq(xvalue)<=max(yw1,yw2))):
            #basically this ensures that the x value is "in front" of the gun and 
            #its intersection with the wall is between the walls top and bottom points 
            return True
        else:
            return False
    if (shotType=="Vertical" and walleq):
        #If there is a vertical shot, but and equation for the wall
        xvalue, yvalue= xa,walleq(xa)
        if (((ya-yb)/(ya-yvalue)>0) and (min(xw1,xw2)<=xvalue<=max(xw1,xw2))):
            return True
        else:
            return False
    if (wallType=="Vertical" and guneq):
        xvalue, yvalue=xw1, guneq(xw1)
        
        if ((((xa-xb)/(xa-xvalue))>0) and (min(yw1,yw2)<=yvalue<=max(yw1,yw2))):
            return True
        else: 
            return False
    else:
        return ((ya-yb)/(ya-yw1)>0 or (ya-yb)/(ya-yw2)>0)
