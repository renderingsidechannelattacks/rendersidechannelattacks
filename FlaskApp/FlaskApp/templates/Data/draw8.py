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
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})
import matplotlib.ticker as mtick



if __name__ == "__main__":

    objects = ('0', '1', '2', '3', '4')
    y_pos = np.arange(len(objects))
    performance = [2,3,10,3,2]
    for i in range(len(performance)):
        performance[i] = performance[i] * 5
    fig, ax = plt.subplots()
    fmt='%.0f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    plt.bar(y_pos, performance, align='center')
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    # plt.title('Programming language usage')
    # axs[1].hist(y, bins=n_bins)
    ax.set_xlabel('Number of Frames')
    ax.set_ylabel('Percenatge')
    fig.tight_layout()
    plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_8' +r".eps")
    # plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/"+ 'demo_6' +r".eps")
