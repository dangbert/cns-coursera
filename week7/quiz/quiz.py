#!/usr/bin/env python3
from curses.ascii import DEL
import numpy as np
import random
import pickle
import copy
import matplotlib.pyplot as plt

def main():
    q1_2()
    q7()


def q1_2():
    """
    for question 1, our largest eigenvalue is evals[0] = 0.23611874,
    which has corresponding eigenvectors evec0 = evevs[:,0] = array([0.75774021, 0.65255634])
    evec0[0] / evec0[1] = 1.1611874208078343,
    looking through the multiple choice options, only one weight vector is proportional to evec0
    (w = [-1.5155, -1.3051]).
    We look for this because "for large t, the largest eigen value term dominates".
    """
    print("\n\nq1_2:::")
    Q = np.array([[0.15, 0.1], [0.1, 0.12]])
    print(Q)
    # n eigen vectors (2*n matrix)
    evals, evecs = np.linalg.eig(Q)
    print("eigen values:")
    print(evals)
    print("eigen vectors:")
    print(evecs)

def q7():
    """
    applying oja's rule to a dataset of 100 points.
    """

    print("\n\nq7:::")
    with open('c10p1.pkl', 'rb') as f:
        odata = pickle.load(f) # dict with one key
    # "original data" 100 (x,y) points
    odata = odata['c10p1'] # data.shape == (100, 2)

    plotPoints(odata, 'original data')

    # center the dataset at (0,0)
    meanPoint = np.mean(odata, axis=0) # array([0.51518173, 0.52049697])
    print(f"mean of origData: {meanPoint}")
    cdata = copy.deepcopy(odata)
    cdata = cdata - meanPoint # "centered data"
    #ranOffset = np.array([random.gauss(0, 5), random.gauss(0, 5)])
    #cdata += ranOffset
    print(f"mean of centered data: {np.mean(cdata, axis=0)}")
    #plotPoints(cdata, 'centered data')

    ETA = 1.0
    ALPHA = 1.0
    #ALPHA = 0 # this turns Oja's rule into hebb's rule
    DELTA_T = 0.001
    CYCLES = 100000

    # random start point for learning process
    w = np.array([random.gauss(0, 5), random.gauss(0, 5)])
    print(f'initial w: {w}')
    print(f'learning for {CYCLES} cycles...')
    for n in range(CYCLES):
        u = cdata[n % len(cdata)] # current data point
        v = w.dot(u) # output of neuron
        # discrete time implementation of Oja's rule
        w = w + DELTA_T * ETA * (v * u - ALPHA * pow(v, 2) * w)
    print(f'final w: {w}')

    plotPoints(cdata, 'centered data with learned w', w=w)


def plotPoints(data, title, w=None, save=True):
    plt.clf()
    plt.scatter(data[:,0], data[:, 1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)

    if w is not None:
      plt.scatter(w[0], w[1], s=100, cmap='Greens')

    if save:
        fname = f"{title}.png".lower().replace(' ', '_')
        plt.savefig(fname, dpi=400)
        print(f"wrote file: {fname}")
    else:
        plt.show()

if __name__ == "__main__":
    main()
