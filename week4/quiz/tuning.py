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

  fig, axis = plt.subplots(2, 2)
  # map each neurone to a section of the plot:
  plotMap = [(0,0), (0, 1), (1,0), (1,1)]
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
    splot = axis[plotMap[n-1]] # AxesSubPlot
    #plt.clf()
    splot.plot(data['stim'], tuningData[key])
    #splot.legend()
    splot.set_xlabel('stimulus value (air velocity direction)')
    splot.set_ylabel('average firing rate Hz ({} trials)'.format(len(data['stim'])))
    splot.set_title('Tuning Curve: {}'.format(key))

  fig.tight_layout(h_pad=4)
  plt.gcf().set_size_inches(11, 8.5)
  plt.savefig("tuning_curves.png".format(key), dpi=400)
  #plt.show()


q7()