#just one of many possible solutions

#Find the @ symbol function
def findATsymbol(mystr):
    for index in range(0, len(mystr)+1): # Loop through the list to find the @ character
        if mystr[index] == '@':
            return index
    return False #if no @ is found, then exit
    
# Find a space in the first part of the text
def findbackwards(bwdStr, mychar):
    for index in range(len(bwdStr)-1,-1,-1):
        if bwdStr[index] == mychar:
            return bwdStr[index+1:]
    return bwdStr #instead of returning -1 and using an if statement later on

# Find a space in the second part of the text
def findFwd(fwdStr, mychar):
    for index in range(0,len(fwdStr)):
        if fwdStr[index] == mychar:
            return fwdStr[0:index],index  
    return fwdStr,index #instead of returning -1 and using an if statement later on

# Harvest a single email from a string
def harvestEmail(mystr):
    
    atIndex = findATsymbol(mystr)
    if not atIndex:  #this helps harvestAllEmails to exit when we reach the end 
        return '', 0 #and also to return smth when no @ symbol is found
                       
    firstPart = findbackwards(mystr[:atIndex], ' ')  #no need to use the full str all the time  
    
    secondPart,spaceAfterIndex = findFwd(mystr[atIndex+1:], ' ')  #no need to use the full str all the time

    extractedEmail = firstPart + '@' + secondPart  

    newIndex = atIndex+spaceAfterIndex ###the new starting point of mystr will be
                                       ###(index of @ + index of an email's last character
    return extractedEmail, newIndex ### the newIndex is necessary for the harvestAllEmails function to work
                                    ### as it removes the part of mystr we already processed

#Harvest all the emails from a paragraph
def harvestAllEmails(myStr, listOfEmails):
    if len(myStr) < 3: #An email cannot be smaller than 3 characters (e.g. smaller than a@a) 
        return listOfEmails
    newEmail,startingIndex = harvestEmail(myStr)
    myStr = myStr[startingIndex:]
    listOfEmails.append(newEmail)
    return harvestAllEmails(myStr, listOfEmails)

#Check if the script works

# Task1
print('check Task 1')
print(harvestEmail("here is an email@address.com to test")[0])
print(harvestEmail("test this@this.com out")[0])
print(harvestEmail("is the e-mail a@a.com even in this sentence?")[0])

# Task2
print('\ncheck Task 2') # a new line \n is added to visually split the two tasks
mystr = '''whoever@wherever.com and the ihaveofficiallyfinished@lmao.com ayyy@lmao.com
Thisactuallyworks@nice.gr verywell@genji.jap ihaveranoutofideas@.com!'''
listOfEmails = []
allEmail = harvestAllEmails(mystr, listOfEmails)
print('\n'.join(allEmail))

#thank you for mystr Philip!
