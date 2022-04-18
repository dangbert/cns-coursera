#!/usr/bin/env python3
import numpy as np
import math
import pickle
from matplotlib import pyplot as plt

def q7():
  with open('tuning_3.4.pkl', 'rb') as f:
    data = pickle.load(f)
  print('tuning data is a dict with keys:')
  print(data.keys())
  print("\ndata['stim'] has shape {} and value:".format(data['stim'].shape))
  print(data['stim'])
  print("\ndata['neuron1'] is a numpy.ndarray with shape: {}".format(data['neuron1'].shape))

  # iterate over neurons
  tuningData = {}
  for n in range(1, 5):
    key = f"neuron{n}"
    nData = data[key]

    tuningData[key] = []
    for stimIndex in range(nData.shape[1]): # 24 stimuli values
      # compute average firing rate across all trials with this particular stimulus
      avgResponse = np.mean(nData[:, stimIndex])
      tuningData[key].append(avgResponse)

    # plot tuning curve for this neuron
    #   we want to see how its average firing rate (response) varies based on the stimuli
    plt.clf()
    plt.plot(data['stim'], tuningData[key])
    plt.legend()
    plt.xlabel('stimulus value')
    plt.ylabel('average firing rate (over {} trials)'.format(len(data['stim'])))
    plt.title('Tuning Curve: {}'.format(key))
    plt.savefig("plot_{}.png".format(key), dpi=400)


q7()