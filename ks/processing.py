import sys
import numpy as np

heightThreshold = 10
topThreshold = 40
topPara = 1.1

speedThreshold = 40
uptimeThreshold = 100

### read the file from server to draw FPS and 
def TimeFPS(filename, startTime, stopTime):
    time = []
    FPS = []
    ### get Time-FPS file
    f = open(filename,'r')
    content =f.read()
    content = content.split('aquarium.js:398 =============start==============')[1]
    # print(len(content))
    contents = content.split('\n')
    contents = contents[1:]
    for index in range(int(len(contents)/2)):
        tmp = contents[index*2].split(' ')[1]
        tmpTime = int(tmp)
        if(tmpTime in range(startTime-100, stopTime+300)):
            time.append(tmpTime)
            tmp = contents[index*2+1].split(' ')[1]
            i = float(tmp)
            FPS.append(i)
    f.close() 
    return time, FPS

def keyTime(filename):
    timeArray = []
    f = open(filename,'r')
    contents =f.read()
    content = contents.split('$')[0]
    sentences = contents.split('$')[1]
    sentence = sentences.split(',')
    title = ''
    title = title.join(sentence)
    timeArray = content.split(',')
    for i in range(len(timeArray)):
        timeArray[i] = int(timeArray[i])
    f.close()
    return timeArray, title, sentence

class Climb(object):
    def __init__(self, start, stop, height, top):
        self.start = start
        self.stop = stop
        self.height = height
        self.top = top

class ClimbList(object):
    def __init__(self):
        self.list = []
        self.pred = 0
    def add(self, Climb):
        self.list.append(Climb)                

    def remove(self, height):
        for i in self.list:
            if(i.height==height):
                self.list.remove(i)
    def minHeight(self):
        if(self.list == []):
            min =  0
        else:
            min = self.list[0].height
            for i in self.list:
                if(i.height<min):
                    min = i.height
        return min
    def length(self):
        return len(self.list)
    def print(self):
        for ins in self.list:
            print(ins.start)
            print(ins.stop)
            print(ins.height)
            print(ins.top)
    def hit(self, timeArray):
        hit  = 0
        for i in range(wordlen):
            tmpStart = self.list[i].start
            tmpStop = self.list[i].stop
            if(timeArray[i] in range(tmpStart, tmpStop)):
                hit = hit+1
        return hit
    def lastStop(self):
        if(len(self.list)>0):
            return self.list[-1].stop
        else:
            return 0
    def sift(self, startTime):
        # self.list = self.list[]
        newlist = []
        for ins in self.list:
            if(ins.stop>startTime and ins.top>topThreshold and ins.height>heightThreshold):
                newlist.append(ins)
        self.list = newlist
    def combine(self, speedThreshold):
        newlist = []
        i = 0
        while(i < len(self.list)):
            ins = self.list[i]
            while(i < len(self.list)-1 and self.list[i+1].start < self.list[i].stop+speedThreshold and (ins.stop-ins.start)<uptimeThreshold):
                ins.stop = self.list[i+1].stop
                i = i+1
            newlist.append(ins)
            i = i+1
        self.list = newlist
    # modify here
    def predict(self):
        # score = 0
        # for ins in self.list:
        #     score = score+ (ins.height-heightThreshold)/heightThreshold
        # self.pred = score
        self.pred = len(self.list)
    def score(self):
        return self.pred

        
# def median():

def denoise(time, FPS):
    windowSize = 100


def process(para1, para2):
    timeArray, title, sentence = keyTime(para2)
    time, FPS = TimeFPS(para1, timeArray[0], timeArray[-1])
    # original time and FPS data here
    # 
    FPSdiff = [0]*(len(FPS))
    for i in range(len(FPS)-1, 0, -1):
        FPSdiff[i] = FPS[i]-FPS[i-1]
    FPSdiff = FPSdiff[1:]
    ############## para ##############
    # print('FPSdiff', FPSdiff)
    # print('FPS', FPS)
    # print('para1', para1)
    tmp = [int(x) for x in FPSdiff if x>0]
    # print('FPSdiff', tmp)
    tmp = np.array(tmp)
    # tmp = np.abs(tmp)
    # FPSdiffmean = np.mean(tmp)
    tmpList = np.bincount(tmp)
    FPSdiffmode = np.argmax(tmpList)
    # print('FPSdiffmode', FPSdiffmode)
    heightThreshold = FPSdiffmode
    FPSmean = np.array(FPS)
    # print('FPSmean', np.mean(FPSmean))
    topThreshold = FPSmean*topPara
    ############### para ##############
    list = ClimbList()
    mark = 0
    minHeight = 0
    for i in range(0, len(FPSdiff)):
        if(mark==0):
            if(FPSdiff[i]>0):
                mark = 1
                tmpHeight = FPSdiff[i]
                tmpStart = time[i]
        elif(mark==1):
            if(FPSdiff[i]>0):
                tmpHeight = tmpHeight+FPSdiff[i]
            else:
                mark = 0
                tmpStop = time[i]
                list.add(Climb(tmpStart, tmpStop, tmpHeight, FPS[i]))
        else:
            continue

    # print(list.length())
    list.sift(timeArray[0])
    # print(list.length())
    list.combine(speedThreshold)
    # print(list.length())
    list.predict()
    return list


if __name__ == '__main__':
    para1 = sys.argv[1]
    para2 = sys.argv[2]
    list = process(para1, para2)
