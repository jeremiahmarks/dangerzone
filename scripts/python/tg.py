def fasterV(maxValue):
    strongAchilliescounter = 0
    achillesNumbers={}
    primes={}

    def checkPrime(numb):
        if (numb in primes.keys()):
            return primes[numb]
        prime = True
        if numb == 1:
            return True
        if numb == 2:
            return True
        for i in range(numb/2):
            i = i+2
            if numb%i == 0:
                prime = False
                break
        primes[numb] = prime
        return prime

    def calculatePhiNumber(number):
        phiNumber = 1
        for i in range(number/2):
            i = i+2
            powr = 0
            if checkPrime(i) == True and number % i == 0:
            # if ( (i in primes) and (number % i == 0)):
                powr = powr+1
                numb = number/i 
                while numb % i == 0:
                    powr = powr+1
                    numb = numb/i
                phiNumber = phiNumber*(pow(i,powr)-pow(i,powr-1))
        return phiNumber

    def checkPowerful(number):
        powerful = True   
        phiNumber = 1   
        powr = 0
        powersList = ()
        maxPower = 0
        for i in range(number/2):
            i = i+2
            powr = 0
            if checkPrime(i) == True and number % i == 0:
            # if ( (i in primes) and (number % i == 0)):
                #print i
                powr = powr+1
                numb = number/i 
                while numb % i == 0:
                    powr = powr+1
                    numb = numb/i
                if maxPower < powr:
                    maxPower = powr
                powersList = powersList+(powr,)
                if powr < 2:
                    powerful = False
                    break
        #print powersList,maxPower           
        if powerful == False:
            return False
        else:
            perfect  = True   
            for l in range(maxPower-1):
                l = l+2
                #print ">",l
                temp = True
                for p in powersList:
                    if p%l != 0:        
                        temp = False
                if temp == False:
                    perfect = False
                else:
                    perfect = True
                    break
            if perfect == False:
                return True
            else:
                return False

    for i in range(maxValue):           
        number = i+1
        checkPrime(number)
        if checkPowerful(number) == True:
            if checkPowerful(calculatePhiNumber(number)) == True:
                strongAchilliescounter = strongAchilliescounter + 1
                print number,"is a Strong Achilles number:"
            else:
                continue   
        else:
            continue
    print "Total number of Strong Achilles number is:",strongAchilliescounter
fasterV(1000)
