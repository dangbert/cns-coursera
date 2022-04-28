#!/usr/bin/env python3
import numpy as np
import math
import pickle
from matplotlib import pyplot as plt

def q7_8():
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
    for stimIndex in range(nData.shape[1]): # 24 unique stimuli values
      """"
      each column corresponds to a given stimulus and has 100 entries
      (each entry being the firing rate over a single 10 sec trial of the given stimulus)
      """
      # compute average firing rate across all trials with this particular stimulus
      avgRes = np.mean(nData[:, stimIndex])
      tuningData[key].append(avgRes)

    ## plot tuning curve for this neuron
    #   we want to see how its average firing rate (response) varies based on the stimuli
    splot = axis[plotMap[n-1]] # AxesSubPlot
    splot.plot(data['stim'], tuningData[key])
    #splot.legend()
    splot.set_xlabel('stimulus value (air velocity direction)')
    splot.set_ylabel('average firing rate Hz (n={})'.format(len(data['stim'])))
    splot.set_title('{}: Tuning Curve'.format(key))

  fig.tight_layout(h_pad=4)
  plt.gcf().set_size_inches(11, 8.5)
  plt.savefig("tuning_curves.png", dpi=400)
  #plt.show()
  print("wrote tuning_curves.png to disk!")


  # now lets investigate the poisson(ness) of each neuron
  plt.clf()
  fig, axis = plt.subplots(2, 2)
  pData = {} # poisson (or not) data
  for n in range(1, 5):
    key = f"neuron{n}"
    nData = data[key]

    # compute list of variances (one for each stimulus)
    #   (multiply by 10 to convert trial firing rate to spike count)
    variance = np.var(nData * 10, axis=0)
    avgSpikes = np.mean(nData * 10, axis=0)
    pData[key] = {'var': variance, 'avg': avgSpikes}

    ## plot variance vs avg spikes for each neuron to evalute poisson(ness)
    splot = axis[plotMap[n-1]] # AxesSubPlot
    splot.scatter(avgSpikes, variance)
    #splot.legend()
    splot.set_xlabel('avg. spike count')
    splot.set_ylabel('variance of spike count')
    splot.set_title('{}: Spike count average vs variance'.format(key))

  fig.tight_layout(h_pad=4)
  plt.gcf().set_size_inches(11, 8.5)
  fName = "poisson.png"
  plt.savefig(fName, dpi=400)
  plt.title('Poisson(ness) Evaluation of Neurons')
  print(f"wrote {fName} to disk!")


if __name__ == "__main__":
  q7_8()