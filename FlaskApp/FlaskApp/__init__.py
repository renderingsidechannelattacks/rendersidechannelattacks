from flask import Flask, render_template, request, jsonify, url_for, redirect, session
import os,sys
import time
import csv
import json
'''
from tinydb import TinyDB, Query
from tinydb.operations import delete
from flask_cors import CORS
import os,sys
import time
import csv
import numpy as np
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt

db = TinyDB('/home/ubuntu/Sites/FlaskApp/FlaskApp/db.json')
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testdemo'
# CORS(app)

@app.route("/")
def index():
    return render_template('./aquarium/test.html')
#====================================================================
#Cross broswer demo test


sendpre = 0
receivepre = 0
sendend = 0
testInfo = {}
num_receive = 10
num_send = 10
@app.route('/readytocollect',methods=['GET','POST'])
def readytocollect():
    global num_receive
    global receivepre
    recv_data = request.get_data()
    if recv_data:
        f= open("/home/ubuntu/Sites/FlaskApp/FlaskApp/flag.txt","w+")
        f.write("1")
        f.close()
    '''send data'''
    print ('already receive and change',receivepre, session.get('receivepre'))
    num_receive = num_receive + 1
    return json.dumps(num_receive)

@app.route('/readytosend',methods=['GET','POST'])
def test_post1():
    global num_send
    global receivepre
    '''receive data'''
    # print ('ready to send', receivepre, session.get('receivepre'))
    recv_data = request.get_data()
    f = open("/home/ubuntu/Sites/FlaskApp/FlaskApp/flag.txt","r+")
    flag = f.readline()
    # print('ready to send',flag)
    f.close()
    if recv_data:
        if flag == '1':
            num_send = num_send + 1
            receivepre = 0
            return json.dumps(num_send)
    return json.dumps(0)

@app.route('/endtosend',methods=['GET','POST'])
def endtosend():
    global sendend
    f= open("/home/ubuntu/Sites/FlaskApp/FlaskApp/flag.txt","r+")
    f.truncate(0)
    f.write("2")
    f.close()
    return json.dumps(0)

@app.route('/endtoreceive',methods=['GET','POST'])
def endtoreceive():
    global sendend
    f = open("/home/ubuntu/Sites/FlaskApp/FlaskApp/flag.txt","r+")
    flag = f.readline()
    # print('ready to send',flag)
    f.close()
    return json.dumps(flag)
    

@app.route('/senddatapre', methods=['GET', 'POST'])
def senddatapre():
    if request.method == 'POST':
        title = request.form.get('title')
        return redirect(url_for('senddata',title = title))
    return render_template('senddatapre.html')

@app.route('/senddata', methods=['GET', 'POST'])
def senddata():
    title = request.args.get('title', None)
    f= open("/home/ubuntu/Sites/FlaskApp/FlaskApp/flag.txt","r+")
    f.truncate(0)
    f.write("0")
    f.close()
    return render_template('senddata.html', title = title)

@app.route('/receivedata')
def receivedata():
    f= open("/home/ubuntu/Sites/FlaskApp/FlaskApp/flag.txt","r+")
    f.truncate(0)
    f.write("0")
    f.close()
    return render_template('receivedata.html')


#=====================================================================start
#=======================fingerprint attack============================
@app.route("/fingerprint")
def fingerprint ():
    return render_template('fingerprint.html')

@app.route("/fingerprint_iframe")
def fingerprint_iframe ():
    return render_template('fingerprint_iframe.html')

@app.route("/wasm")
def wasm():
    return render_template('wasm.html')

@app.route('/fingerprint_data',methods=['POST'])
def server_test():
    data1 = request.form.getlist('post_data1')
    data2 = request.form.getlist('post_data2')
    data3 = request.form.getlist('post_data3')
    data4 = request.form.getlist('post_data4[]')
    data5 = request.form.getlist('post_data5[]')
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    fname = "/home/ubuntu/Sites/FlaskApp/FlaskApp/static/fingerprint-features/Data7/"+ now +r".csv"
    csvFile = open(fname,'wb')
    # File.writelines(L) 
    # for L = [data1, data2, data3, data4, data5] 
    # File.close()
    writer = csv.writer(csvFile)
    # print data1
    # print data2
    # print data3
    # print data4
    # print data5
    writer.writerows([data1,data2,data3,data4,data5])
    csvFile.close()

    # data5string = "".join(data5)
    # print data5string
    # print data5string[10]
    # print data5string[22:]
    # fh = open("/home/ubuntu/Sites/FlaskApp/FlaskApp/static/fingerprint-features/Data6/"+ now +r".png", "wb")
    # fh.write(data5string[22:].decode('base64'))
    # fh.close()

    return jsonify(otstr=[1,2,3,4,5,6,7])
#=====================================================================end
'''
cpuCollectFlag = 0
gpuCollectFlag = 0

@app.route("/check")
def check():
    return render_template('./aquarium/test/check.html')

@app.route('/checkFinished')
def check_finished():
    values = db.all()
    if len(values) != 0:
        db.purge()
        return 'True'
    else:
        db.purge()
        return 'False'

@app.route('/clearDb')
def clearDb():
    f=open('/home/ubuntu/Sites/FlaskApp/FlaskApp/db.json','w')
    f.write('{"_default": {}}')
    f=open('/home/ubuntu/Sites/FlaskApp/FlaskApp/db.json','w')
    f.close()
    return ('clearDb')

@app.route("/set")
def set():
    return render_template('./aquarium/test/set.html')

@app.route('/setFinished')
def set_finished():
    db.purge()
    db.insert({'finished': True})
    print ("set:cpuCollectFlag",cpuCollectFlag)
    return "change the value" 
#====================================================================
#Cross broswer real test
@app.route("/cross_target")
def cross_target():
    return render_template('./aquarium/cross_target.html')

@app.route("/cross_collect")
def cross_collect():
    return render_template('./aquarium/cross_collect.html')

@app.route("/twowindow")
def twowindow():
    return render_template('./aquarium/aquarium_twowindow.html')
'''
@app.route("/iframe")
def iframe():
    return render_template('./aquarium/load.html')

# this is the baidu demo website
@app.route("/test")
def test():
    return render_template('./aquarium/aquarium.html')

# this is the website that collect data from single broswer
# history sniff collect
# collect no cache data 
@app.route("/collectdataNC")
def collectdataNC():
    return render_template('./aquarium/aquarium_Collect.html')

# collect already cached data
@app.route("/collectdataAC")
def collectdataAC():
    return render_template('./aquarium/aquarium_Collect.html')


#=====================================================================

@app.route("/Gpu_test")
def Gpu_test():
    return render_template('./aquarium/aquarium_Gpu.html')

@app.route("/demo")
def demo():
    return render_template('./aquarium/demo.html')
'''

@app.route("/Cached")
def Cached():
    return render_template('./aquarium/Cached.html')

@app.route("/NoCached")
def NoCahced():
    return render_template('./aquarium/NoCached.html')
'''
@app.route("/adjust")
def adjust ():
    return render_template('./aquarium/adjust.html')

@app.route("/collectdemo")
def collectdemo ():
    return render_template('./collectdemo.html')


@app.route('/server_test_Gpu',methods=['POST'])
def server_test_Gpu():
    data1 = request.form.getlist('post_data1[]')
    data2 = request.form.get('post_data2')
    dir = "/home/ubuntu/Sites/FlaskApp/FlaskApp/data/Tor_Mac/" + str(data2) + '/'
    # print dir
    list = os.listdir(dir) 
    # print list
    if len(list) < 50:
        fname = dir + str(len(list) + 1) +r".csv"
        csvFile = open(fname,'wb')
        writer = csv.writer(csvFile)
        writer.writerows([data1])
        csvFile.close()
        # print fname

    return jsonify(otstr=[1,2,3,4,5,6,7])
'''
@app.route('/server_test',methods=['POST'])
def server_test():
    data1 = request.form.getlist('post_data1[]')
    data2 = request.form.getlist('post_data2[]')
    data3 = request.form.getlist('post_data3[]')
    data4 = request.form.getlist('post_data4[]')
    data5 = request.form.get('post_data5')
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    fname = "/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/Test/"+ now +r".csv"
    csvFile = open(fname,'wb')
    writer = csv.writer(csvFile)
    writer.writerows([data1,data2,data3,data4])
    csvFile.close()

    # s1 = list(map(float, data1))
    # t1 = range(len(s1))

    # s2 = list(map(float, data2))
    # t2 = range(len(s2))

    # s3 = list(map(float, data3))
    # t3 = range(len(s3))

    # s4 = list(map(float, data4))
    # t4 = range(len(s4))
    # fig, axs = plt.subplots()
    # axs.plot(t1, s1, t2, s2, t3, s3, t4, s4)
    # axs.set_xlabel('Real Time')
    # axs.set_ylabel('Render Time')

    # axs.grid(True)
    # # plt.vlines(40, 0, 100, colors = "c", linestyles = "dashed")

    # plt.legend(('First Time(D)', 'Second Time', 'Third Time', 'Fourth Time'),loc='upper right')
    # fig.tight_layout()
    # plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/Test/"+ now +r".png")


    return jsonify(otstr=[1,2,3,4,5,6,7])



# input bandwidth  output array
@app.route('/control_bandwidth',methods=['POST'])
def control_bandwidth():
    bandwidth = request.form.get('post_data1')
    returnlist = np.random.rand(10000 * int(bandwidth)).tolist()
    return jsonify(otstr=returnlist)

# input bandwidth  output array
@app.route('/control_bandwidth1',methods=['POST'])
def control_bandwidth1():
    bandwidth = request.form.get('post_data1')
    returnlist = np.random.rand(10000 * int(bandwidth)).tolist()
    return jsonify(otstr=returnlist)

# input bandwidth  output array
@app.route('/control_bandwidth2',methods=['POST'])
def control_bandwidth2():
    bandwidth = request.form.get('post_data1')
    returnlist = np.random.rand(10000 * int(bandwidth)).tolist()
    return jsonify(otstr=returnlist)

# input bandwidth  output array
@app.route('/control_bandwidth3',methods=['POST'])
def control_bandwidth3():
    bandwidth = request.form.get('post_data1')
    returnlist = np.random.rand(10000 * int(bandwidth)).tolist()
    return jsonify(otstr=returnlist)
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True) 