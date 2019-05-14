'''
Created on 2019年5月11日

@author: tony
'''

class place(object):
    '''
   place class represent the location of the CLP electric charging station
    '''
    numplace = 0 # class variable to record number of location

    def __init__(self,area,location,address):
        '''
        constructor method
        
        parameters:
        - arae
        - location
        - address
        '''
        place.numplace += 1
        
        self.__area = area
        self.__location = location
        self.__address = address
        
    def getarea(self):
        ''' accessor method to get area   '''
        return self.__area
    
    def getlocation (self):
        '''accessor method to get location   '''
        return self.__location
    
    def getaddress (self):
        '''accessor method to get address   '''
        return self.__address
    
    def __str__ (self):
        '''String representation of charging location  '''
        return '%-20s%-50s%-15s'%\
            (self.__area,self.__location,self.__address)