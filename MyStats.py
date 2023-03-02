import math

'''
    first draft of stats function stand alone simple output just to figure things out

'''
class MyStats:
    '''
        basic statistics class that performs them on a single list of values feed into the class during construction
        all functions within can be used stand alone as well
    '''
    def __init__(self, providedDataList, copyDataFlag):

        #setup core class data
        if copyDataFlag == True:
            self.data = providedDataList.copy()
        else:
            self.data = providedDataList 
        self.mean   =   -7777.7777
        self.min    =   -7777.7777
        self.max    =   -7777.7777
        self.median =   -7777.7777
        self.mode   =   -7777.7777
        self.stdev  =   -7777.7777

        #order depenent stat functions
        self.median = self.compute_median(self.data)

        #order independent stat functions
        self.data.sort()
        self.mean = self.compute_mean(self.data)
        self.min = self.data[0]
        self.max = self.data[len(providedDataList) - 1]
        self.mode = self.compute_mode(self.data)
        self.stdev = self.compute_stdev(self.data, self.mean) 
    
    '''
      returns the mean of a provided list of numbers
    '''
    def compute_mean(self, data):
        workingTotal = 0
        #sum the data set
        for x in data:
            workingTotal = workingTotal + x
        #return and find mean from sum
        return workingTotal/len(data)

    '''
       finds and return the median of a provided data set
       returns average of middle two if even
       returns middle number if odd
    '''
    def compute_median(self, data):
        setSize = len(data)

        if (setSize % 2) == 1: #odd sized data set
             return data[(setSize // 2)]
        else: #even sized data set
            return ((data[(setSize // 2) - 1] + data[(setSize // 2)])/2)

    '''
        function to find the most common number of a provided data set
    '''
    def compute_mode(self, data):

        highestCount = 1
        value = data[0]
        numDic = {}
        #add items to dictionary updating count as they are found
        for x in data:
            if x in numDic:
                nextCount = numDic.get(x)+1
                numDic.update({x : nextCount}) #increase count in dictionary
                if nextCount > highestCount: # check if highest count needs to be updated
                    highestCount = nextCount
                    value = x
            else:
                numDic[x] = 1 #add new entry to dictionary
        return value

    '''
        function to determin the standard deviation of a provided data set using the data set and mean
        uncorrected standard deviation sqrt(sum((xi-mean)^2)/N)
    '''
    def compute_stdev(self, data, mean):
        #setup one off values
        mean2Square = mean * mean
        meanTime2 = 2 * mean
        stdev = 0.0

        for x in data:
            #horner to spped ip
            stdev = stdev + (x - meanTime2) * x + mean2Square
        
        return math.sqrt(stdev / len(data))

    '''
        function to find the smallest number of a provided data set
    '''
    def compute_min(self, data):
        minimum = data[0]
        for x in data:
            if x < minimum:
                minimum = x
        return minimum

    '''
        function to find the largest number of a provided data set
    '''
    def compute_min(self, data):
        maximum = data[0]
        for x in data:
            if x > maximum:
                maximum = x
        return maximum

    '''
        getter for the working data set
    '''
    def get_data(self):
        return self.data

    '''
        getter for the mean of the data set
    '''
    def get_mean(self):
        return self.mean

    '''
        getter for the min of the data set

    '''
    def get_min(self):
        return self.min

    '''
        getter for the max of the data set
    '''
    def get_max(self):
        return self.max

    '''
        getter for the median of the data set
    '''
    def get_median(self):
        return self.median

    '''
        getter for the mode of the data set
    '''
    def get_mode(self):
        return self.mode
    
    '''
        getter for the standard deviation of the data set
    '''
    def get_stdev(self):
        return self.stdev

# Testing goes here

#test one off functions
data = [1,2,3,4,5,5,5,5,5,6,7,8,8,8,9,9]



testStats = MyStats(data, True)
print("MY STATS DEBUG")
print("DATA = " + str(testStats.get_data()))
print("MEAN = " + str(testStats.get_mean()))
print("MIN = " + str(testStats.get_min()))
print("MAX = " + str(testStats.get_max()))
print("MEDIAN = " + str(testStats.get_median()))
print("MODE = " + str(testStats.get_mode()))
print("STAND DEVIATION = " + str(testStats.get_stdev()))