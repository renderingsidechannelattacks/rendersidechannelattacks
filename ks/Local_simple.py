import matplotlib.pyplot as plt
import urllib
import sys
import os
import processing

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
        if(tmpTime in range(startTime-500, stopTime+300)):
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

if __name__ == '__main__':

    fig= plt.figure(figsize=(40,6))

    axes= fig.add_axes([0.1,0.1,0.8,0.8], ylabel='m sec', xlabel='time')
    axes.grid(True)
    # plt.ylim(0,60)

    
    # originTime = time[0]
    # time[:] = [x - (originTime) for x in time]
    # 
    if(len(sys.argv)>2):
        timeArray, title, sentence = keyTime(sys.argv[2])
        axes.set_title('Baidu: \''+ title + '\'')
        for i in range(0,len(timeArray)):
            print(timeArray[i])
            axes.axvline(timeArray[i], c = 'red')
            axes.text(timeArray[i], 30, sentence[i])

        time, FPS = TimeFPS(sys.argv[1], timeArray[0], timeArray[-1])
    

        para1 = sys.argv[1]
        para2 = sys.argv[2]
        guess = processing.process(para1, para2)
        for ins in guess.list:
            axes.axvline(ins.start, c = 'green')
            axes.axvline(ins.stop, c = 'purple')
            # axes.text(ins.start, ins.height, ins.height)
    else:
            time, FPS = TimeFPS(sys.argv[1])
    axes.plot(time, FPS, color='blue', linestyle='solid')

    if(len(sys.argv)>3):
        time, FPS = TimeFPS(sys.argv[2])
        originTime = time[0]
        time[:] = [x - (originTime) for x in time]
        axes.plot(time,FPS, color='blueviolet', linestyle='solid')


    # plt.savefig('images/' + title + '.png')
    if(len(sys.argv)>2):
        title = str(timeArray[0])
    else:
        title = 'noise' + str(time[0])
    saveName = os.path.join('images', title + '.png')
    plt.savefig(saveName)

    plt.show()








