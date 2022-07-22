#!/usr/bin/env python3
from __future__ import print_function
"""
Experiment / implementation of the "integrate and fire" neuron model.

Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron 
R Rao 2007

translated to Python by rkp 2015
"""

import numpy as np
import matplotlib.pyplot as plt


# input current
#I_pA = 1000 # pA
#I_pA = 250  # smallest input current that fails to cause a spike
I_pA = 5000

I = I_pA / 1000 # nA (note 1 nano amp = 10^3 pico amps)
print(f"I = {I}")

# capacitance and leak resistance
C = 1 # nF
R = 40 # M ohms

# I & F implementation dV/dt = -V/RC + I/C
# Using h = 1 ms step size, Euler method

V = 0
tstop = 100
tstop = 1000
abs_ref = 5   # absolute refractory period 
ref = 0       # absolute refractory period counter
V_trace = []  # voltage trace for plotting
V_th = 10     # spike threshold

# run the model for tstop ms
for t in range(tstop):
    if not ref:
        V = V - (V/(R*C)) + (I/C)
    else:
        ref -= 1
        V = 0.2 * V_th # reset voltage
    
    if V > V_th:
        V = 50 # emit spike
        ref = abs_ref # set refractory counter

    V_trace += [V]


plt.plot(V_trace)
plt.title(f"Integrate-and-fire model (I={I:.4f})\n(Calculating max fire rate)")
plt.xlabel(f"time (ms)\n")
plt.ylabel(f"voltage (mV?)")
#plt.figtext(0.5, 0.0, "smallest input current that fails to cause a spike", wrap=True, horizontalalignment='center', fontsize=6)

#plt.title(f"R={R:.2f}, C={C:.2f}, STOP_INJECTION={STOP_INJECTION}")
plt.savefig("intfire_q17.png", dpi=400)

plt.show()