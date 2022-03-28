#!/usr/bin/env python3

"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle
import os

from compute_sta import compute_sta


FILENAME = 'c1p8.pickle'
#OUTPUT_DIR = "outputs/"
OUTPUT_DIR = "./"

def main():
  # this data has a sampling rate of 500Hz = 500 samples/sec = 0.5 samples/ms
  #   (and total 600,000 samples -> so 20 min of data total)
  SAMPLING_RATE_HZ = 500
  with open(FILENAME, 'rb') as f:
      data = pickle.load(f)

  # stimulus vector
  #   (the velocity of of a pattern of bars experienced by a fly while an H1 motion-sensitive neuron was recorded)
  stim = data['stim']
  # binary vector (1 if spike occurred in time bin corresponding to time index, 0 otherwise)
  rho = data['rho']

  sampling_period = 1000 / SAMPLING_RATE_HZ # 2 ms (between each sample)
  # here a timestep is an occurence of a single sample
  # number of timesteps in window of 300ms prior to a spike's occurence
  #   (note: for this problem we ignore the stimulus value exactly 300ms prior to spike, and the one 0ms "prior")
  num_timesteps = int((300 / sampling_period) - 2) # width (ms) of window to look at prior to each spike
  import pdb; pdb.set_trace()
  print(f"num_timesteps = {num_timesteps}")

  total_spikes = len(rho[rho == 1]) # 53601
  print(f"total spikes in data: {total_spikes}")
  plotData(stim, rho, sampling_period)

  sta = compute_sta(stim, rho, num_timesteps)
  print(f"computed sta has length {len(sta)}")

  time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

  plt.clf()
  plt.plot(time, sta)
  plt.xlabel('Time (ms)')
  plt.ylabel('Stimulus')
  plt.title('Spike-Triggered Average')
  plt.savefig(os.path.join(OUTPUT_DIR, 'spike_triggered_average.png'), dpi=600)
  plt.show()


def plotData(stim, rho, sampling_period):
  """plot raw data for viewing"""
  totalSamples = stim.shape[0] # 600,000
  time = np.arange(0, totalSamples) * sampling_period

  plt.clf()
  plt.plot(time, stim, label="stimulus (velocity of a pattern of bars shown to a fly)")
  # scaling rho so it can be seen better alongside stim:
  plt.plot(time, rho * 20, label="rho (tracks occurences of spikes, note: scaled for visibility)")

  plt.xlabel('Time (ms)')
  plt.ylabel('Stimulus')
  plt.legend()
  plt.title('Raw stimulus over time')

  #plt.savefig(os.path.join(OUTPUT_DIR, 'all_data.png'), dpi=400)
  #plt.show()

  plt.xlim(0, 500) # set range of x axis (ms)
  plt.savefig(os.path.join(OUTPUT_DIR, 'first_500ms.png'), dpi=600)


if __name__ == "__main__":
  main()