'''
Author: Fionn Mcguire
Date: 31-10-2017
Description: Create a program to run a dictionary attack to test for brute force resistance
'''



class dictAttack(object):
    def __init__(self):
        self.wordList = []
        self.popularPassword = []
        self.replacements = {}
        
    #TODO Develop for special char _%$@€
    #Combine some of the modes if password is john1983 it could also be John_1983
    #These are a series of True False variables used to denote the extent of the attack
    def execAttack(self,replacements,numbers,caseSensitive,engageFullDict):
        
         
        def readDictFile(filename):
            with open(filename) as f:
                for line in f:
                    self.wordList.append(line)

        def readCommonPassFile(filename):
            with open(filename) as f:
                for line in f:
                    self.popularPassword.append(line)

        #Always try most common passwords
        readCommonPassFile('DataSets/CommonPassword.txt')

        if engageFullDict == True:
            readDictFile('DataSets/words.txt')

        
        #This code will emulate a POST command to a RESTful API, 200 Success, 404 Fail
        PASSWORD = "12345678"
        

        for i in self.popularPassword:
            if str(i.strip())  == str(PASSWORD.strip()):
                return 200
            elif numbers == True:
                for num in range(10000):
                    if str(i.strip())+str(num)  == str(PASSWORD.strip()):
                        return 200
        for i in self.wordList:
            if i == PASSWORD:
                return 200
        return 404


myAttack = dictAttack()
print(myAttack.execAttack(False,False,False,False))

