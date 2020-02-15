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
import matplotlib.ticker as mtick
plt.rcParams.update({'font.size': 18})




if __name__ == "__main__":

    s1 = [88.0, 91.7, 95.7,95.7,95.7,95.7]

    
    t1 = [40,80,120,160,200,240]

    s2 = [50, 50, 56, 64, 84.6, 88]

    t2 = [40,80,120,160,200,240]

    s3 = [40, 50, 88.9,88.9,88.9,88.9]

    t3 = [40,80,120,160,200,240]


    # print (s1)
    fig, axs = plt.subplots()
    fmt='%.0f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    axs.yaxis.set_major_formatter(yticks)
    axs.plot(t1, s1, 'o-',markersize=10,linewidth=2.0)
    axs.plot(t2, s2, '*--',markersize=10,linewidth=2.0)
    axs.plot(t3, s3,'s-.',linewidth=2.0)
    axs.set_xlabel('Number of Frames')
    axs.set_ylabel('Percentage')

    axs.grid(True)
    # plt.vlines(40, 0, 100, colors = "c", linestyles = "dashed")

    plt.legend(('Baidu','Jd', '360'),loc='lower right')
    fig.tight_layout()
    plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_10' +r".eps")
    # plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_4' +r".eps")
