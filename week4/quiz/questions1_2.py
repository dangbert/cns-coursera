#!/usr/bin/env python3
import math

def q1():
  res = -0.1 * math.log(0.1, 2) + (-0.9 * math.log(0.9, 2))
  print(f"q1: {res:0.4f}\n")

# TODO: doesn't look like this answer is right:
def q2():
  # total entropy of responses:
  totalEntropyR = -0.055*math.log(0.055, 2) - 0.845*math.log(0.845, 2)
  # average noise entropy:
  avgEntropyN = -0.1 * (0.5*math.log(0.5, 2)) * (0.5*math.log(0.5, 2)) + \
    -0.9 * (1/18 * math.log(1/18, 2)) * (17/18 * math.log(17/18, 2))

  print(f"totalEntropyR = {totalEntropyR:0.4f}")
  print(f"avgEntropyN = {avgEntropyN:0.4f}")
  res = totalEntropyR - avgEntropyN
  print(f"q2: {res:0.4f}\n")

q1()
q2()