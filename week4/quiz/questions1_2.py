#!/usr/bin/env python3
import math

def q1():
  """
  note: I added this full problem to my notes
  https://beta.engbert.me/p/sci/cns/coursera.md
  """
  print("\n------q1---------")
  res = -0.1 * math.log(0.1, 2) + (-0.9 * math.log(0.9, 2))
  print(f"q1: {res:0.4f}\n")
  return res

def q2(a1):
  """computing Mutal information. see equation for MI(S,R) in notes"""
  print("\n------q2---------")
  # total entropy of responses (comes from question1)
  totalEntropyR = a1

  # average noise entropy:
  avgEntropyN = -0.1 * (0.5*math.log(0.5, 2) + 0.5*math.log(0.5, 2)) + \
    -0.9 * (1/18*math.log(1/18, 2) + 17/18*math.log(17/18, 2))

  print(f"totalEntropyR = {totalEntropyR:0.4f}")
  print(f"avgEntropyN = {avgEntropyN:0.4f}")
  res = totalEntropyR - avgEntropyN
  print(f"q2: {res:0.4f}\n")

a1 = q1()
q2(a1)