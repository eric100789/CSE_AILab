import numpy as np
import matplotlib.pyplot as plt
import csv

def readData(filename):
    rows = []
    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    rows = np.transpose(np.array(rows))
    return rows[:-1], rows[-1]

if __name__ == '__main__':
    train_data, train_label = readData("SVM/DataA/train_data.csv")
    test_data, test_label = readData("SVM/DataA/test_data.csv")