#!/usr/bin/env python3
from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron 
R Rao 2007

translated to Python by rkp 2015
"""

import numpy as np
import matplotlib.pyplot as plt

def run(noiseamp=0.0):
  # input current
  I = 1 # nA

  # capacitance and leak resistance
  C = 1 # nF
  R = 40 # M ohms

  # I & F implementation dV/dt = - V/RC + I/C
  # Using h = 1 ms step size, Euler method

  V = 0
  tstop = 200
  tstop = 1000
  abs_ref = 5 # absolute refractory period 
  ref = 0 # absolute refractory period counter
  V_trace = []  # voltage trace for plotting
  V_th = 10 # spike threshold
  spikeTimes = [] # list of times spikes occurred

  # input current
  #noiseamp = 0 # amplitude of added noise
  #noiseamp = 0.5
  I += noiseamp*np.random.normal(0, 1, (tstop,)) # nA; Gaussian noise
  #import pdb; pdb.set_trace()

  for t in range(tstop):
    
    if not ref:
      V = V - (V/(R*C)) + (I[t]/C)
    else:
      ref -= 1
      V = 0.2 * V_th # reset voltage

    if V > V_th:
      V = 50 # emit spike
      ref = abs_ref # set refractory counter

    # TODO: TODO: this logic for checking if at a spike fails when we have noise!
    if len(V_trace) > 0 and V_trace[-1] > V:
      # we're at a spike
      spikeTimes.append(t)

    V_trace += [V]


  plt.clf()
  fig, axis = plt.subplots(1, 2)
  fig.tight_layout(h_pad=4)
  plt.gcf().set_size_inches(11, 8.5)

  splot = axis[0] # AxesSubPlot
  splot.plot(V_trace)
  splot.set_xlabel(f"time (ms)\n")
  splot.set_ylabel(f"voltage (mV?)")
  splot.set_title(f"integrate-and-fire model with noise amp. {noiseamp:.2f}")
  #plt.title(f"integrate-and-fire model with noise amp. {noiseamp:.2f}\n({len(spikeTimes)} spikes)")

  # compute times between successive spikes
  if len(spikeTimes) > 0:
    spikeIntervals = []
    prevSpikeT = spikeTimes[0]
    for i in range(1, len(spikeTimes)):
      spikeT = spikeTimes[i]
      spikeIntervals.append(spikeT - prevSpikeT)
      prevSpikeT = spikeT

    splot = axis[1] # AxesSubPlot
    # plot historgram
    splot.hist(spikeTimes, bins=20)
    splot.set_xlabel(f"time (ms)")
    splot.set_ylabel(f"count")
    splot.set_title(f"histogram of spike intervals ({len(spikeTimes)} spikes)")
  #plt.title(f"integrate-and-fire model with noise amp. {noiseamp:.2f}\n({len(spikeTimes)} spikes)")

  #plt.title(f"integrate-and-fire model with noise amp. {noiseamp:.2f}\n({len(spikeTimes)} spikes)")
  plt.savefig(f"intfire_with_noise_amp_{noiseamp:.2f}.png", dpi=400)
  #plt.clf()
  #plt.show()

if __name__ == "__main__":
  #for noiseamp in np.arange(0.0, 0.25, 0.05):
  for noiseamp in np.arange(0.0, 1.0, 0.1):
    run(noiseamp)