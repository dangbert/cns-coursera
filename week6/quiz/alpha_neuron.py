#!/usr/bin/env python3
"""
Created on Wed Apr 22 16:13:18 2015

Models an integrate-and-fire neuron receiving input spikes through an alpha synapse.
(Fire a neuron via alpha function synapse and random input spike train).

R Rao 2007
translated to python by rkp 2015
"""
from __future__ import print_function, division

import time
import numpy as np
#from numpy import concatenate as cc
import matplotlib.pyplot as plt


def main():
  np.random.seed(0)
  # I & F implementation dV/dt = - V/RC + I/C
  h = 1. # step size, Euler method, = dt ms
  t_max= 200 # ms, simulation time period
  tstop = int(t_max/h) # number of time steps
  ref = 0 # refractory period counter

  # Generate random input spikes
  # Note: This is not entirely realistic - no refractory period
  # Also: if you change step size h, input spike train changes too...
  thr = 0.9 # threshold for random spikes
  spike_train = np.random.rand(tstop) > thr # (array of true false values: spike or not)

  # alpha function: synaptic conductance
  t_a = 100 # Max duration of syn conductance (ms after a spike)
  t_peak = 1 # ms after a spike occurs at which the alpha functions peaks
  #   ^controls how long the effects of an input spike linger on in the postsynaptic neuron)
  t_peak = 5
  g_peak = 0.05 # nS (peak synaptic conductance)
  const = g_peak / (t_peak*np.exp(-1))
  t_vec = np.arange(0, t_a + h, h)
  #   value of alpha function, sampled over time (t_vec)
  #   (from equation in 6.1 notes)

  oSpikeCounts = []
  t_peaks = np.arange(0.15, 10, 0.5)
  for t_peak in t_peaks:
    alpha_func = const * t_vec * (np.exp(-t_vec/t_peak))

    plt.clf()
    plt.plot(t_vec[:80], alpha_func[:80])
    plt.xlabel('t (in ms)')
    plt.title('Alpha Function (Synaptic Conductance for Spike at t=0)')
    plt.draw()
    caption = f"t_peak = {t_peak:.2f}, const={const:.2f}"
    plt.figtext(0.5, 0.005, caption, wrap=True, horizontalalignment='center', fontsize=8)
    #plt.savefig('alpha_function.png', dpi=400)
    plt.savefig(f't_peak/alpha_function{t_peak:.2f}.png', dpi=400)
    #time.sleep(2) 

    # capacitance and leak resistance
    C = 0.5 # nF
    R = 40 # M ohms
    print('C = {}'.format(C))
    print('R = {}'.format(R))

    # conductance and associated parameters to simulate spike rate adaptation
    g_ad = 0
    G_inc = 1/h
    tau_ad = 2

    # Initialize basic parameters
    E_leak = -60 # mV, equilibrium potential
    E_syn = 0 # Excitatory synapse (why is this excitatory?)
    g_syn = 0 # Current syn conductance
    V_th = -40 # spike threshold mV
    V_spike = 50 # spike value mV
    ref_max = 4/h # Starting value of ref period counter
    # running times (ms) since (recent) past spikes occured
    t_list = np.array([], dtype=int)
    V = E_leak
    V_trace = [V] # history of voltages in mV
    t_trace = [0]

    fig, axs = plt.subplots(2, 1)
    axs[0].plot(np.arange(0,t_max,h), spike_train)
    axs[0].set_title('Input spike train')

    print(f"running model for {tstop} time iterations")
    #import pdb; pdb.set_trace()
    oSpikeCounts.append(0)
    for t in range(tstop):
      # Compute input
      if spike_train[t]: # check for input spike
        #import pdb; pdb.set_trace()
        t_list = np.concatenate([t_list, [1]])

      # Calculate synaptic current due to current and past input spikes
      #   question 8: to make I_syn negative, it seems like 
      g_syn = np.sum(alpha_func[t_list]) # synaptic conductance (e.g. 3.459-05)
      I_syn = g_syn*(E_syn - V)          # synaptic current (e.g. 0.00207, while e.g. V=-59.997)

      # Update spike times
      if np.any(t_list):
        t_list = t_list + 1
        if t_list[0] == t_a: # Reached max duration of syn conductance
          t_list = t_list[1:]

      # Compute membrane voltage
      # Euler method: V(t+h) = V(t) + h*dV/dt
      if not ref:
        V = V + h*(-((V-E_leak)*(1+R*g_ad)/(R*C)) + (I_syn/C))
        g_ad = g_ad + h*(-g_ad/tau_ad) # spike rate adaptation
      else:
        ref -= 1
        V = V_th - 10 # reset voltage after spike
        g_ad = 0

      # Generate spike
      if (V > V_th) and not ref:
        oSpikeCounts[-1] += 1
        V = V_spike
        ref = ref_max
        g_ad = g_ad + G_inc

      V_trace += [V]
      t_trace += [t*h]
    print("t_list =")
    print(t_list)


    axs[1].plot(t_trace,V_trace)
    plt.draw()
    axs[1].set_title('Output spike train')
    axs[1].set_ylabel('Voltage (mV)')
    plt.savefig(f't_peak/spike_trains_tpeak_{t_peak:.2f}.png', dpi=400)
    #plt.show()

  #import pdb; pdb.set_trace()
  plt.clf()
  plt.plot(t_peaks, oSpikeCounts)
  plt.xlabel('t_peak value (ms)')
  plt.ylabel('output spike count')
  plt.title('Effect of t_peak on output spike count')
  plt.draw()
  plt.savefig(f't_peak/t_peak_effect.png', dpi=400)

if __name__ == "__main__":
  main()