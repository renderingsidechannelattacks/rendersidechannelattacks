import csv
import os
import sys

# find 20 highly used words
def find_word(source_filepath):
    dict = {}
    line = 0
    wordlist = []
    with open(source_filepath, 'r') as source:
        reader = csv.reader(source)
        # print(reader)
        headers = next(reader)
        print(headers)
        # row = print(next(reader))
        while True:
            row = next(reader)
            text = row[2]
            # print(text)
            tmpwords = text.split(' ')
            # print(tmpwords)
            for word in tmpwords:
                if (word in dict):
                    dict[word].append(line)
                    if(len(dict[word])>20 and word not in wordlist and len(word)==9):
                        wordlist.append(word)
                else:
                    dict[word] = [line]
                line = line+1
            if(len(wordlist)>30):
                break
    # print(wordlist)
    # print(dict)

    dic  = {}
    dic ['elections'] = dict['elections']
    # for word in wordlist:
    #     dic[word] = dict[word]
    #     print(word)
    return dic

# find 10 data for each word is enough
def find_data(source_filepath, dic):

    dest_path = '/Users/jia/Desktop/keystrokePJ/ks'
    target_filename = 'wordsdata.csv'
    target_filepath = os.path.join(dest_path, target_filename)

    target = open(target_filepath, 'w')
    writer = csv.writer(target)
    

    files = os.listdir(source_filepath)
    for word in dic:
        for line in dic[word]:
            # print(line)
            file = int((line+2)/999)
            if(file==0):
                file_line = ((line+2)%999)+1
            else:
                file_line = (line+2)%999
            # print(file)
            # print(file_line)
            # print((file-1)*999 + 997 + file_line)
            # if(((file-1)*999 + 997 + file_line)!=line):
            #     print('no')
            file = f'small_{file}.csv'
            # print(file)
            filepath = os.path.join(source_filepath, file)
            with open(filepath, 'r') as source:
                reader = csv.reader(source)
                headers = next(reader)
                i=0
                while(i<file_line):
                    headers = next(reader)
                    i=i+1
                data = headers
                # print(word)
                # print(data)
                writer.writerow(data)

def find_in_features(source_filepath, dic):
    dest_path = '/Users/jia/Desktop/keystrokePJ/ks/keystroke_dataset'
    target_filename = 'data.csv'
    target_filepath = os.path.join(dest_path, target_filename)

    target = open(target_filepath, 'w')
    writer = csv.writer(target)
    
    # files = os.listdir(source_filepath)
    linenumbers = []
    for word in dic:
        linenumbers.extend(dic[word])
    # print('linenumbers', linenumbers)
    for i in range(0, len(linenumbers)):
        linenumbers[i] = linenumbers[i]+3

    with open(source_filepath, 'r') as source:
        reader = csv.reader(source)
        headers = next(reader)
        # print('headers', headers)
        i=0
        length = len(linenumbers)
        while True:
            if (i in linenumbers):
                # print('i', i)
                data = headers
                writer.writerow(data)
                length = length-1
                if(length==0):
                    break
            headers = next(reader)
            i=i+1
        



def main():
    dic = find_word('/Users/jia/Desktop/keystrokePJ/test0/text.csv')
    # dic['a'] = dic['a'].append(10000)
    # find_data('old_data/smallData', dic)
    # data 找出来写到一个文件里好了。。。就可以用了
    dic = find_in_features('/Users/jia/Desktop/keystrokePJ/test0/features.csv', dic)


if __name__ == '__main__':
    main()
