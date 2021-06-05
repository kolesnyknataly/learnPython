import os
import sys

path = sys.argv[1]
metric = sys.argv[2].replace("-", "")
fileNames = os.listdir(path)

for fileName in fileNames:
    filePath = path + "\\" + fileName
    if metric == "b":
        print("File name: [" + fileName + "] File size: [" + str(os.path.getsize(filePath)) + "] bytes")
    elif metric == "k":
        print("File name: [" + fileName + "] File size: [" + str(round(os.path.getsize(filePath) / 1024, 2)) + "] kilobytes")
    elif metric == "m":
        print("File name: [" + fileName + "] File size: [" + str(round(os.path.getsize(filePath) / (1024 * 1024), 2)) + "] megabytes")
    else:
        raise Exception("wrong metric: " + metric)
