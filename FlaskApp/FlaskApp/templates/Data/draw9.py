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

    s2 = [100.0, 100.0, 91.2, 84.5, 76.6]
    t1 = [2,3,4,5,6]

    s3 = [100.0, 100.0, 91.8, 85.3, 75.0]
    t2 = [2,3,4,5,6]

    s1 = [100.0, 100.0, 91.5, 85.3, 75.8]
    t3 = [2,3,4,5,6]

    fig, axs = plt.subplots()
    fmt='%.0f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    axs.yaxis.set_major_formatter(yticks)
    axs.plot(t1, s1, 'o-',markersize=10,linewidth=2.0)
    axs.plot(t2, s2, '*--',markersize=10,linewidth=2.0)
    axs.plot(t3, s3,'s-.',linewidth=2.0)
    axs.set_xlabel('Number of Candidate Words')
    axs.set_ylabel('Percentage')

    axs.grid(True)
    # plt.vlines(40, 0, 100, colors = "c", linestyles = "dashed")

    plt.legend(('F1 Score','Precision', 'Recall'),loc='lower left')
    fig.tight_layout()
    # plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_3' +r".png")
    plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_9' +r".eps")
    
