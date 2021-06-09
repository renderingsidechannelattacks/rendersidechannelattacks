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
plt.rcParams.update({'font.size': 15})



if __name__ == "__main__":

    s1 = [96.0, 88.9,84.7, 75.9, 75.9, 72.7]
    t1 = [0, 5, 10, 15, 20 , 25]

    s2 = [100.0, 100.0, 83.3, 83.3, 73.3, 64.2]
    t2 = [0, 5, 10, 15, 20 , 25]

    s3 = [100.0, 96.0, 72.0, 64.3, 69.2, 62.1]
    t3 = [0, 5, 10, 15, 20 , 25]

    fig, axs = plt.subplots()
    axs.plot(t1, s1, 'o-',markersize=6,linewidth=2.0)
    axs.plot(t2, s2, '*--',markersize=6,linewidth=2.0)
    axs.plot(t3, s3,'s-.',markersize=6,linewidth=2.0)
    axs.set_xlabel('Defense Noide Level in Fuzzy Time (ms)')
    axs.set_ylabel('Percentage')

    axs.grid(True)
    # plt.vlines(40, 0, 100, colors = "c", linestyles = "dashed")

    plt.legend(('Chrome','Firefox', 'Safari'),loc='lower left')
    fig.tight_layout()
    plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_1' +r".eps")
