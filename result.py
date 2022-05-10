
import numpy as np
from scipy.cluster.vq import kmeans, vq
import pandas as pd

def detection(filename):
    df = pd.read_csv(filename, sep=' ',
                     names=['label', 'x', 'y', 'width', 'height'])  # read label ,x separte it in files/names =columns
    df = df.sort_values(by='y', ascending=True)
    Y = df.y.values

    codebook, _ = kmeans(Y, 3)  # three clusters
    cluster_indices, _ = vq(Y, codebook)

    i = 0  # for each line
    line = 0
    lines = [0]
    for i in range(1, len(cluster_indices)):
        if cluster_indices[i] == cluster_indices[i - 1]:
            lines.append(line)
        else:
            line += 1
            lines.append(line)

    lines = np.array(lines)
    df['line'] = lines

    final_reading = []

    for l in df.line.unique():  # rows
        numberArray = df[df.line == l].sort_values(by='x').label.values  # for each line
        number = 0
        for i in range(len(numberArray)):
            number = number + numberArray[i] * 10 ** (len(numberArray) - i - 1)  # convert to number

        final_reading.append(number)

    return final_reading
