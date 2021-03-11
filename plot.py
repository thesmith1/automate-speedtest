import csv
import numpy as np
from vis import plot_timeseries

file_path = './out.csv'

data = {'download': [], 'upload': [], 'latency': []}
download_idx = 5
upload_idx = 6
latency_idx = 2


def bytes_to_mbits(x): return x * 8 / 1e6


with open(file_path) as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0

    for row in reader:
        if line_count > 0:
            data['latency'].append(float(row[latency_idx]))
            data['download'].append(bytes_to_mbits(float(row[download_idx])))
            data['upload'].append(bytes_to_mbits(float(row[upload_idx])))
        line_count += 1

plot_timeseries([np.arange(len(data['download'])), np.arange(len(data['upload']))],
                [data['download'], data['upload']], legend=['Download', 'Upload'], title='Speed',
                filename='speed.html', xaxis_title='Time', yaxis_title='Speed (Mb/s)')

plot_timeseries([np.arange(len(data['latency']))], [data['latency']], legend=['Latency'], title='Latency',
                filename='latency.html', xaxis_title='Time', yaxis_title='Time (ms)')
