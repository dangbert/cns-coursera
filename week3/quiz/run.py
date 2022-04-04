#!/usr/bin/env python3

from re import I
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

outDir = "."
s1_mean = 5
s1_std = 0.5

s2_mean = 7
s2_std = 1

thresholds = [5.667, 5.978, 2.69, 5.830]
thresholds.sort()

def main():
  # distribution of firing rates in response to possible stimulus value s1
  s1 = np.random.normal(s1_mean, s1_std)

  # distribution of firing rates in response to possible stimulus value s2
  s2 = np.random.normal(s2_mean, s2_std)

  x = np.arange(2, 11, 0.001)

  plt.clf()
  plt.plot(x, norm.pdf(x, s1_mean, s1_std), label="s1 distribution")
  plt.plot(x, norm.pdf(x, s2_mean, s2_std), label="s2 distrubtion")
  plt.legend()
  plt.xlabel("stimulus value")
  plt.ylabel("response (firing rate)")
  #plt.title("")
  # plot threshold values as vertical lines:
  for t in thresholds:
    plt.axvline(t, color="red")


  weight = 2 # twice as bad to to mistakenly think it's s2 than s1
  for t in thresholds:
    evalThreshold(t, weight=weight)

  plt.savefig("{}/plot.png".format(outDir), dpi=400)
  plt.show()

def evalThreshold(thresh, weight=1):
  """
  evalute how good a given threshold would be at distinguishing from s1 and s2.
  (assuming both stimuli are equally likely)
  params:
    thresh: float threshold to use on stimulus value
    weight: penalty of getting it wrong (s2:s1)
  """
  p1 = norm.cdf(thresh, s1_mean, s1_std)
  p2 = norm.cdf(thresh, s2_mean, s2_std)

  # not sure how great/accurate this metric acutally is:
  avgPenalty = ( (1-p1) * weight + (1-p2) * 1 ) / weight
  print(f"\nthresh={thresh:.4f}, p(s1) = {p1:.4f}, p(s2) = {p2:.4f}, avgPenalty = {avgPenalty:.4f}")



if __name__ == "__main__":
  main()