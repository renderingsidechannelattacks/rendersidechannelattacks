# calculate F1 score here!
from sklearn import metrics
# from sklearn.metrics import f1_score, accuracy_score
import os
import processing
import sys
import numpy as np
import itertools

# LARGESTLENGTH = 20

# sort_word_list = [2,5,6,8,10]
# sort_word_list = [6]
# 0.831
# sort_word_list = [2,5,6,8,10]
# 0.669
# sort_word_list = [2,3,5,6,9,10]
# 
# sort_word_list = [2, 3]
# sort_word_list = [7]
# 
# sort_word_list = [2,5,8]
# 0.899
# sort_word_list = [2,5,8,10]
# 
# 0.825
# sort_word_list = [2,4,8,10]

def calcu(sort_word_list, paths):  
    y_true = []
    y_pred = []
    ans = []
    # print(paths)
    for path in paths:
        # word = path.split('data')[0]
        word = path
        path = 'data/' + path
        truth = len(word)
        if(truth not in sort_word_list):
            continue
        ans.append(truth)
        files = os.listdir(path)
        files = sorted(files)
        files = [x for x in files if not(x.startswith('.'))]
        # print(files)
        y_true.extend([truth]*(int(len(files)/2)))
        res = []
        for i in range(0, int(len(files)/2)):
            para1 = os.path.join(path, files[i*2+1])
            para2 = os.path.join(path, files[i*2])
            list = processing.process(para1, para2)
            # print(list.pred())
            # a = list.pred()
            res.append(list.score())
        pred_res = [re for re in res]
        y_pred.extend(pred_res)
    if(len(sort_word_list)==1):
        print(y_pred)
    #  classify
    y_pred_classify = []
    origin_y_true = y_true
    y_true = []
    for i in range(0, len(y_pred)):
        # see how far from each word
        tmpAns = np.array(ans)-y_pred[i]
        tmpAns = np.abs(tmpAns)
        distance = abs(origin_y_true[i]-y_pred[i])
        # see it as noise
        if(distance>10):
            continue
        else:
            y_true.append(origin_y_true[i])
        index = np.argmin(tmpAns)
        y_pred[i] = ans[index]
        y_pred_classify.append(y_pred[i])

    y_pred = y_pred_classify
    # Print the confusion matrix
    # print(metrics.confusion_matrix(y_true, y_pred))
    # Print the precision and recall, among other metrics
    # print(metrics.classification_report(y_true, y_pred, digits=3))
    f1 = metrics.f1_score(y_true, y_pred, average='macro')
    recall = metrics.recall_score(y_true, y_pred, average='macro')
    precision = metrics.precision_score(y_true, y_pred, average='macro')

    # print(macro)
    return precision, recall, f1

def selectMax(paths, minlen, maxlen):
    sort_word_list = []
    for i in range(minlen, maxlen):
        maxf1 = 0
        maxlist = []
        maxprecision = 0
        maxrecall = 0
        for j in itertools.combinations('123456789abc', i):
            tmplist = list(j)
            sort_word_list = []
            for x in tmplist:
                if(x=='a'):
                    sort_word_list.append(11)
                    continue
                elif(x=='b'):
                    sort_word_list.append(12)
                    continue
                elif(x=='c'):
                    sort_word_list.append(9)
                    continue
                tmp = int(x)
                if(tmp<8):
                    sort_word_list.append(tmp+1)
                elif(tmp==8):
                    sort_word_list.append(10)
                elif(tmp==9):
                    sort_word_list.append(13)

            # print('sort_word_list', sort_word_list)
            precision, recall, f1 = calcu(sort_word_list, paths)
            if(f1>maxf1):
                maxf1 = f1
                maxlist = sort_word_list
                maxprecision = precision
                maxrecall = recall
        print('maxprecision:', maxprecision, 'maxrecall:', maxrecall, 'maxF1:', maxf1, 'maxlist:', maxlist)


if __name__ == '__main__':
    paths = os.listdir('data')
    # print(paths)
    paths = [x for x in paths if not x.startswith('.')]
    # 看所有单词单独预测的情况
    # python run.py 1
    if(len(sys.argv)==2 and int(sys.argv[1])==1):
        list = [2,3,4,5,6,7,8,9,10,11,12,13]
        for i in list:
            sort_word_list = [i]
            print(sort_word_list)
            calcu(sort_word_list, paths)
    # 手动输入想看哪几个一起分类
    # python run.py 2 3
    elif(len(sys.argv)>2):
        sort_word_list = []
        for i in range(1, len(sys.argv)):
            sort_word_list.append(int(sys.argv[i]))
            # print(sort_word_list)
        precision, recall, f1 = calcu(sort_word_list, paths)
        print("precision, recall, f1")
        print(precision, recall, f1)
    # python run.py
    else:
        selectMax(paths, 2, 9)

    










