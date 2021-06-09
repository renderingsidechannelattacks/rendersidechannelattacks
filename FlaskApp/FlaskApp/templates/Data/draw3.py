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

    s1 = [100.0, 100.0, 100.0, 100.0, 98.5,93.8, 89.4]
    t1 = [2,3,4,5,6,7,8]

    s2 = [100.0, 100.0, 100.0, 100.0, 98.7,95.8, 91.6]
    t2 = [2,3,4,5,6,7,8]

    s3 = [100.0, 100.0, 100.0, 100.0, 98.5,94.1, 89.5]
    t3 = [2,3,4,5,6,7,8]

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
    # plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_3' +r".png")
    plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_3' +r".eps")
    
