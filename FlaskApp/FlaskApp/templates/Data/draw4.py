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
plt.rcParams.update({'font.size': 18})
import matplotlib.ticker as mtick



if __name__ == "__main__":

    s1 = [1.0, 1.0, 1.0, 1.0, 0.964,0.870, 0.829]
    s1 = [i * 100.0 for i in s1]
    
    t1 = [2,3,4,5,6,7,8]

    s2 = [1.0, 1.0, 1.0, 1.0, 0.964,0.883, 0.843]
    s2 = [i * 100.0 for i in s2]
    t2 = [2,3,4,5,6,7,8]

    s3 = [1.0, 1.0, 1.0, 1.0, 0.964,0.873, 0.830]
    s3 = [i * 100.0 for i in s3]
    t3 = [2,3,4,5,6,7,8]


    print (s1)
    fig, axs = plt.subplots()
    fig, axs = plt.subplots()
    fmt='%.0f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    axs.yaxis.set_major_formatter(yticks)
    axs.plot(t1, s1, 'o-',markersize=10,linewidth=2.0)
    axs.plot(t2, s2, '*--',markersize=10,linewidth=2.0)
    axs.plot(t3, s3,'s-.',linewidth=2.0)
    axs.set_xlabel('Number of Websites')
    axs.set_ylabel('Percentage')

    axs.grid(True)
    # plt.vlines(40, 0, 100, colors = "c", linestyles = "dashed")

    plt.legend(('F1 Score','Precision', 'Recall'),loc='lower left')
    fig.tight_layout()
    plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_4' +r".eps")
    # plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_4' +r".eps")
