import pyedflib
import csv
import numpy as np
import math

fileName = "..\\s1.bdf"
f = pyedflib.EdfReader(fileName)

labels = f.getSignalLabels()
sampleCount = min(f.getNSamples())
channelCount = f.signals_in_file

# chunk samples into 40 to 41 chunks
sampleCountPerTrial = math.floor(sampleCount / 40)

# prepare signal buffer
sigbufs = np.zeros((sampleCount, channelCount + 1))

# generate time column data
sigbufs[:, 0] = range(0, sampleCount)

# read signal into buffer
for i in range(0, channelCount - 1):
    sigbufs[:, i + 1] = f.readSignal(i)

# data now lives in RAM => close input file
f.close()

# dump the entire data into one big file
with open('s1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Time"] + f.getSignalLabels())
    writer.writerows(sigbufs)

# chunk the data for convenient file handling without stalling the computer all the time
for chunkStart in range(0, sampleCount, sampleCountPerTrial):
    chunkEnd = (chunkStart + sampleCountPerTrial)
    with open('s1_' + str(chunkStart) + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Time"] + f.getSignalLabels())
        writer.writerows(sigbufs[chunkStart:chunkEnd:1])