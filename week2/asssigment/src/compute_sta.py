"""
Created on Wed Apr 22 15:21:11 2015

Code to compute spike-triggered average.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def compute_sta(stim, rho, num_timesteps):
    """Compute the spike-triggered average from a stimulus and spike-train.
    
    Args:
        stim: stimulus time-series
        rho: spike-train time-series
        num_timesteps: how many timesteps to use in STA
        
    Returns:
        spike-triggered average for num_timesteps timesteps before spike"""
    

    # This command finds the indices of all of the spikes that occur after 300 ms into the recording.
    # (because any spike in the first 300ms doesn't have enough data before it for a sta window)
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps

    # Fill in this value. Note that you should not count spikes that occur
    # before 300 ms into the recording.
    num_spikes = len(spike_times)
    print(f"num_spikes (after first 300 ms) = {num_spikes}")
    
    # Compute the spike-triggered average of the spikes found.
    # To do this, compute the average of all of the vectors
    # starting 300 ms (exclusive) before a spike and ending at the time of
    # the event (inclusive). Each of these vectors defines a list of
    # samples that is contained within a window of 300 ms before each
    # spike. The average of these vectors should be completed in an
    # element-wise manner.
    
    print(f"computing spike-triggered average using data from {num_spikes} spike events")
    #sta = np.zeros((num_timesteps,))
    sta = np.zeros((num_timesteps,)) # TODO for now
    for spikeIndex in spike_times:
      windowData = stim[(spikeIndex-num_timesteps):spikeIndex]
      sta += windowData

    return sta / num_spikes