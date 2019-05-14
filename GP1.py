'''
Group project

Created on 10/4/2019

@author: TonyChan, 
'''
from place import place
import fileinput
import sys

placeDT=['Area','Location','Address'] #data field labels
placeDL=[]     #place data list

def readFile(datafile):
    '''
    read and validate data from datafile
    '''
    try:
        fileIn = open(datafile, 'r')
        
        line = fileIn.readline()
        
        while line != '':
            placeRec = line.split('_')
            if len(placeRec) < 3:
                sys.stderr.write('Invalid data line : '+line+'\n')
            elif placeRec[0] == '' or placeRec[1] == '':
                sys.stderr.write('Invalid Name or Address : '+line+'\n')
            
            else:
                placeDL.append(place(placeRec[0],placeRec[1],placeRec[2]))
            
            line = fileIn.readline()
            
        if place.numplace == 0:
            sys.stderr.write('empty or invalid data only : '+line+'\n')
        
        else:
            placeDL.append(place(placeRec[0],placeRec[1],placeRec[2]))
            
        fileIn.close()
            
    except FileNotFoundError as error:
        sys.stderr.write(str(error)+'\n')  
         
    
def displayallchargingplace (datafile):
    print('%-20s%-50s%20s'%(placeDT[0],placeDT[1],placeDT[2]))
    print('='*100) 
    for line in fileinput.input(datafile):
        sys.stdout.write(line)
        
def allchargingplace():
    print('%-20s%-40s%20s'%(placeDT[0],placeDT[1],placeDT[2]))
    print('='*100)    
    for e in sorted(placeDL, key = lambda c: c.getarea()):
        print(e)
        
def kowloon():
    print('%-20s%-50s%-20s'%(placeDT[0],placeDT[1],placeDT[2]))
    print('='*100)
    for e in sorted(placeDL, key = lambda c: c.getlocation()):
        if e.getarea() == 'Kowloon':
            print (e)
        
def newterritories():
    print('%-20s%-50s%-20s'%(placeDT[0],placeDT[1],placeDT[2]))
    print('='*100)
    for e in sorted(placeDL, key = lambda c: c.getlocation()):
        if e.getarea() == 'New Territories':
            print (e)
            
def outlayingisland():
    print('%-20s%-50s%-20s'%(placeDT[0],placeDT[1],placeDT[2]))
    print('='*100)
    for e in sorted(placeDL, key = lambda c: c.getlocation()):
        if e.getarea() == 'Outlying Island':
            print (e) 
            
def readdata(s,inputType):
    while True:
        try:
            inputValue=input(s)
            if inputType == 1:
                if inputValue != ('Kowloon'and'kowloon'and'New Territories'and'new territories'and'New territories'and\
                                'new Territories'and'outlying island'and'Outlying Island'and'Outlying island'and'outlying Island'):
                    raise ValueError('Please enter correct area name')

            return inputValue
        except ValueError as error:
            sys.stderr.write(str(error)+'\n')
                       
def main():
    instructions = """\nEnter one of the following:
        1 to reads the contents of data
        2 to print all input data
        3 to to print searching result  
        4 to end \n"""

    while True:
        sys.stderr.flush()    
        sys.stdout.write (instructions)        
        choice = input( "Enter 1 to 4 " ) 
        sys.stdout.flush()
        
        if choice == "1":
            displayallchargingplace(sys.argv[1])
        if choice == '2':
            allchargingplace()
        if choice == "3":
            searchInform = input('Enter where you are?(Kowloon,new territories,outlying Island) ')
            if searchInform == ('Kowloon' and 'kowloon'):
                kowloon()
            elif searchInform == ('New Territories' and 'new territories' and 'New territories' and 'new Territories'):
                newterritories()
            elif searchInform == ('outlying island' and 'Outlying Island' and 'Outlying island' and 'outlying Island'):
                outlayingisland()
            else:
                print('Please enter a correct area name!')
        if choice == '4':
            break
    print("End of searching!")     
    
if __name__ == "__main__":
    try:
        readFile(sys.argv[1])
    
        if place.numplace != 0:
            main()
            
    except IndexError as error:
        sys.stderr.write('Type \"python grade.py filename\" to run program\n')

