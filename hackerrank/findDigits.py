

numOfInput=int(raw_input())
retString=""
for x in range(numOfInput):
	total=0
	inputString=raw_input()
	inputInt=int(inputString)
	for each in inputString:
		eachInt=int(each)
		if not(eachInt==0):
			if (inputInt%eachInt==0):
				total+=1
	retString+=str(total)+"\n"
print retString

