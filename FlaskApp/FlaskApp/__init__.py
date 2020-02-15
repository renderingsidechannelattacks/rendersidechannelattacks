from flask import Flask, render_template, request, jsonify
import os,sys
import time
import csv
import numpy as np
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./aquarium/aquarium.html')

@app.route("/twowindow")
def twowindow():
    return render_template('./aquarium/aquarium_twowindow.html')

@app.route("/iframe")
def iframe():
    return render_template('./aquarium/load.html')

@app.route("/test")
def test():
    return render_template('./aquarium/test.html')

@app.route("/adjust")
def adjust ():
    return render_template('./aquarium/adjust.html')

@app.route('/server_test',methods=['POST'])
def server_test():
    data1 = request.form.getlist('post_data1[]')
    data2 = request.form.getlist('post_data2[]')
    data3 = request.form.getlist('post_data3[]')
    data4 = request.form.getlist('post_data4[]')
    data5 = request.form.get('post_data5')
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    fname = "/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/Tor/Cache/"+ data5 +"/"+ now +r".csv"
    csvFile = open(fname,'wb')
    writer = csv.writer(csvFile)
    writer.writerows([data1,data2,data3,data4])
    csvFile.close()

    s1 = list(map(float, data1))
    t1 = range(len(s1))

    s2 = list(map(float, data2))
    t2 = range(len(s2))

    s3 = list(map(float, data3))
    t3 = range(len(s3))

    s4 = list(map(float, data4))
    t4 = range(len(s4))
    fig, axs = plt.subplots()
    axs.plot(t1, s1, t2, s2, t3, s3, t4, s4)
    axs.set_xlabel('Real Time')
    axs.set_ylabel('Render Time')

    axs.grid(True)
    # plt.vlines(40, 0, 100, colors = "c", linestyles = "dashed")

    plt.legend(('First Time(D)', 'Second Time', 'Third Time', 'Fourth Time'),loc='upper right')
    fig.tight_layout()
    plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/Tor/Cache/"+ data5 +"/" + now +r".png")


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True) 