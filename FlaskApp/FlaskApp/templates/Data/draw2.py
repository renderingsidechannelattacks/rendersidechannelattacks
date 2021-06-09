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




if __name__ == "__main__":

    s1 = [1.0, 1.0, 0.88, 0.8]
    t1 = [2,3,4,5]

    s2 = [1, 1, 0.825, 0.74]
    t2 = [2,3,4,5]

    s3 = [1, 1, 0.85, 0.73]
    t3 = [2,3,4,5]

    fig, axs = plt.subplots()
    axs.plot(t1, s1, 'o-')
    axs.plot(t2, s2, '*--')
    axs.plot(t3, s3,'s-.')
    axs.set_xlabel('Number of words')
    axs.set_ylabel('Percentage')

    axs.grid(True)
    # plt.vlines(40, 0, 100, colors = "c", linestyles = "dashed")

    plt.legend(('F1 Score','Precision', 'Recall'),loc='lower left')
    fig.tight_layout()
    plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_2' +r".eps")
