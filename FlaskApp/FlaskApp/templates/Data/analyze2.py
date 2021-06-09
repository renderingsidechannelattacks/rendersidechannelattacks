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







if __name__ == '__main__':
    websiteNameList = []
    # websiteNameList.append('360/')
    websiteNameList.append('Baidu/')
    websiteNameList.append('Google/')
    websiteNameList.append('Jd/')
    # websiteNameList.append('LoginTmall/')
    # websiteNameList.append('Qq/')
    websiteNameList.append('Sohu/')
    websiteNameList.append('Taobao/')
    # websiteNameList.append('Tmall/')
    websiteNameList.append('Youtube/')
    collectDataMap = []
    predictMap = []
    for i in range(len(websiteNameList)):
        cachepath = './Tor/Cache/' + websiteNameList[i]
        collectDataArray = []
        predictArray = []
        for info in os.listdir(cachepath):
            if info.endswith('v'):
                # print(info)
                # print('************************************')
                with open (cachepath + info) as f: 
                    line = f.readlines()[0]
                    array = line.split(',')
                    array = map(float, array)
                    array = array[:1000]
                    collectDataArray.append(array)
                    predictArray.append(0)
        # print(websiteNameList[i])
        # print(len(collectDataArray))
        collectDataMap.append(collectDataArray)
        predictMap.append(predictArray)
    # print(len(collectDataMap))
    # print(collectDataMap[0])
    sortArray = reduce(operator.add,reduce(operator.add, collectDataMap))
    sortArray.sort()
    aveLow = sortArray[ int(math.floor(len(sortArray) * 0.475))]
    aveMid = sortArray[ int(math.floor(len(sortArray) * 0.975))]
    for i in range(len(collectDataMap)):
        for j in range(len(collectDataMap[i])):
            for k in range(len(collectDataMap[i][j])):
                collectDataMap[i][j][k] = (collectDataMap[i][j][k] - aveLow) / (aveMid - aveLow) * 3
                # if collectDataMap[i][j][k] < aveLow:
                #     collectDataMap[i][j][k] = 0
                # else:
                #     collectDataMap[i][j][k] = (collectDataMap[i][j][k] - aveLow) / (aveMid - aveLow) * 3
                    # if collectDataMap[i][j][k] < 0.1:
                    #     collectDataMap[i][j][k] = 0
    # print(aveLow, aveMid)
    # print(collectDataMap)
    for i in range(len(collectDataMap)):
        for j in range(len(collectDataMap[i])):
            testArray = collectDataMap[i][j]
            distanceArray = []
            for k in range(len(collectDataMap)):
                temArray = []
                for l in range(len(collectDataMap[k])):
                    distance = DTW(testArray, collectDataMap[k][l])
                    if (i == k) and (l == j):
                        distance = 99999.0
                    temArray.append(distance)
                temArray.sort()
                distanceArray.append((temArray[0] + temArray[1] + temArray[2])/ 3.0)
            predictLine = distanceArray.index(min(distanceArray))
            predictMap[i][j] = predictLine
        print(websiteNameList[i], i)
        print(predictMap[i])
    reducePredictMap = reduce(operator.add, predictMap)
    resultMap = [0, 0, 0]
    for i in range(len(predictMap)):
        precision = float(predictMap[i].count(i))/ float(len(predictMap[i])) 
        resultMap[0] += precision
        if (float(reducePredictMap.count(i))  == 0):
            recall = 0.0
        else:
            recall = float(predictMap[i].count(i)) / float(reducePredictMap.count(i)) 
        resultMap[1] += recall
        # print(predictMap[i].count(i), len(predictMap[i]), reducePredictMap.count(i)) 
        # print(precision, recall)
        if ((precision + recall) == 0):
            F1 = 0.0
        else:
            F1 = 2.0 * precision * recall / (precision + recall)
        resultMap[2] += F1
        print(precision, recall, F1)
    print("final", resultMap[0]/len(predictMap) * 1.0, resultMap[1]/len(predictMap)* 1.0, resultMap[2]/len(predictMap)* 1.0)


    # print(predictMap)
            
            


    

    # cachepath = './Tor/Cache/' + websiteName
    # nocachepath =  './Tor/NoCache/' + websiteName
    # cacheNumber = 0
    # nocacheNumber = 0
    # roundValue = 800.0
    # for info in os.listdir(cachepath):
    #     if info.endswith('v'):
    #         print(info)
    #         print('************************************')
    #         collectData = []
    #         cacheNumber += 1
    #         with open (cachepath + info) as f: 
    #             line = readlines()[0]
    #             for line in f.readlines():
    #                 array = line.split(',')
    #                 array = map(float, array)
    #                 # for i in range (1, len(array)):
    #                 #     array[i] = array[i] + array[i - 1] + random() * roundValue
    #                 # for i in range (len(array)):
    #                 #     array[i] = math.ceil(array[i] / roundValue) * roundValue
    #                 # # print (array)
    #                 # for i in range (1, len(array)):
    #                 #     array[i] = array[i] - array[i - 1]
    #                 collectData.append(array)
    #                 # print (array)
    #             # print(collectData)
    #             predictresult = Predict(collectData)

    
    # print('==========================================================')
    # print('==========================================================')
    # print('==========================================================')

    # for info in os.listdir(nocachepath):
    #     if info.endswith('v'):
    #         print(info)
    #         print('************************************')
    #         collectData = []
    #         nocacheNumber += 1
    #         with open (nocachepath + info) as f:
    #             for line in f.readlines():
    #                 array = line.split(',')
    #                 array = map(float, array)
    #             #     for i in range (1, len(array)):
    #             #         array[i] = array[i] + array[i - 1]
    #             #     for i in range (len(array)):
    #             #         array[i] = math.ceil(array[i] / roundValue) * roundValue
    #                 # print (array)
    #                 # for i in range (1, len(array)):
    #                 #     array[i] = array[i] - array[i - 1]
    #                 collectData.append(array)
    #                 # print (array)
    #             # print(collectData)
    #             predictresult = Predict(collectData)
    # print("cacheNumber",cacheNumber)
    # print("nocacheNumber",nocacheNumber)

    '''  
    
            predict->True     
             cache->cache    cache->no         no->no        no->cache      value            precision    Recall     f1_score
        360       12/12            0/12         9/12           3/12          300             12/12         12/15
        Baidu     12/12            0/12         11/12          1/12          60              12/12         12/13
        Google    9/12             3/12         5/12           7/12          10              9/12          9/16
        Jd        11/12            1/12         7/12           5/12          400             11/12         11/16
        LT        5/12             7/12         7/12           5/12          450             5/12          5/10
        Qq        5/12             7/12         11/12          1/12          100             5/12          5/6
        Sohu      4/11             7/11         10/12          2/12          140             4/11          4/6
        Taobao    10/12            2/12         8/12           4/12          200             10/12         10/14
        Tmall     9/12             3/12         9/12           3/12          400             9/12          9/12
        Youtube   7/12             5/12         9/12           3/12          60              7/12          7/10
        All       84/119           35/119       86/120         34/120        --              84/119        84/118      0.709
    '''


                




