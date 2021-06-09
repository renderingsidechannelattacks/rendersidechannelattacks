import os,sys
import time
import csv
import numpy as np
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import operator
import math
from random import seed
from random import random


def Predict(collectData):

    # change value
    sortArray = reduce(operator.add, collectData)
    sortArray.sort()
    aveLow = sortArray[ int(math.floor(len(sortArray) * 0.475))]
    aveMid = sortArray[ int(math.floor(len(sortArray) * 0.975))]
    for i in range(len(collectData)):
        for j in range(len(collectData[i])):
            if collectData[i][j] < aveLow:
                collectData[i][j] = 0
            else:
                if ((aveMid - aveLow)) == 0:
                    collectData[i][j] = 0
                else:
                    collectData[i][j] = (collectData[i][j] - aveLow) / (aveMid - aveLow) * 3
                if collectData[i][j] < 0.5:
                    collectData[i][j] = 0
    print(aveLow, aveMid)
    # print(collectData)
    controlDistance1 = DTW(collectData[1], collectData[2])
    controlDistance2 = DTW(collectData[1], collectData[3])
    controlDistance3 = DTW(collectData[2], collectData[3])
    if (min([controlDistance1, controlDistance2, controlDistance3]) * 5 < max([controlDistance1, controlDistance2, controlDistance3])):
        if min([controlDistance1, controlDistance2, controlDistance3]) == controlDistance1:
            collectData[3] = collectData[1]
        elif (min([controlDistance1, controlDistance2, controlDistance3]) == controlDistance2):
            collectData[2] = collectData[1]
        else:
            collectData[1] = collectData[2]

    testDistance1 = DTW(collectData[0], collectData[1])
    testDistance2 = DTW(collectData[0], collectData[2])
    testDistance3 = DTW(collectData[0], collectData[3])
    print('controlDistance1',controlDistance1)
    print('controlDistance2',controlDistance2)
    print('controlDistance3',controlDistance3)
    print('testDistance1',testDistance1)
    print('testDistance2',testDistance2)
    print('testDistance2',testDistance3)
    # print('rate',(testDistance1+ testDistance2 + testDistance3) / (controlDistance1 + controlDistance2 + controlDistance3))

def DTW(Q, C):
    m = len(Q)
    n = len(C)
    distanceMap = []
    DTWMap = []
    for j in range(n):
        temArray = []
        for i in range(m):
            temDistance = abs(Q[i] - C[j]) * (abs(i - j) + 1)
            temArray.append(temDistance)
        distanceMap.append(temArray)
        DTWMap.append(temArray)
    for j in range(n):
        for i in range(m):
            if (i != 0) and (j != 0):
                value1 = DTWMap[j - 1][i] + distanceMap[j][i]
                value2 = DTWMap[j][i - 1] + distanceMap[j][i]
                value3 = DTWMap[j - 1][i - 1] + distanceMap[j][i] * 2
                DTWMap[j][i] = min([value1, value2, value3])
    return DTWMap[n-1][m-1]






roundValue = 25.0
if __name__ == '__main__':
    websiteName = '360/'
    cachepath = './Chrome/Cache/' + websiteName
    nocachepath =  './Chrome/NoCache/' + websiteName
    cacheNumber = 0
    nocacheNumber = 0
    cutvalue = 120
    # roundValue = 800.0
    for info in os.listdir(cachepath):
        if info.endswith('v'):
            print(info)
            print('************************************')
            collectData = []
            cacheNumber += 1
            with open (cachepath + info) as f: 
                for line in f.readlines():
                    array = line.split(',')
                    array = map(float, array)
                    # array = array[:cutvalue]
                    # for i in range (1, len(array)):
                    #     array[i] = array[i] + array[i - 1] + random() * roundValue
                    # for i in range (len(array)):
                    #     array[i] = math.ceil(array[i] / roundValue) * roundValue
                    # # print (array)
                    # for i in range (len(array)-1, 0, -1):
                    #     array[i] = array[i] - array[i - 1]
                    collectData.append(array)
                    # print ('cachelength',len(array))
                # print(collectData)
                predictresult = Predict(collectData)

    
    print('==========================================================')
    print('==========================================================')
    print('==========================================================')

    for info in os.listdir(nocachepath):
        if info.endswith('v'):
            print(info)
            print('************************************')
            collectData = []
            nocacheNumber += 1
            with open (nocachepath + info) as f:
                for line in f.readlines():
                    array = line.split(',')
                    array = map(float, array)
                    # array = array[:cutvalue]
                    # print(array)
                    # for i in range (1, len(array)):
                    #     array[i] = array[i] + array[i - 1]
                    # for i in range (len(array)):
                    #     array[i] = math.ceil(array[i] / roundValue) * roundValue
                    # # print (array)
                    # for i in range (len(array)-1, 0, -1):
                    #     array[i] = array[i] - array[i - 1]
                    # print (array)
                    collectData.append(array)
                    # print (array)
                # print(collectData)
                predictresult = Predict(collectData)
    print("cacheNumber",cacheNumber)
    print("nocacheNumber",nocacheNumber)




