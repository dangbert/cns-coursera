#!/usr/bin/env python3
from tabnanny import check
import numpy as np

def main():
  W = np.zeros((5,5))
  np.fill_diagonal(W, 0.6)
  W[W==0] = 0.1
  print('W = ')
  print(W)

  #u = np.array([[0.6, 0.5, 0.6, 0.2, 0.1]]).transpose()
  u = np.array([0.6, 0.5, 0.6, 0.2, 0.1])
  M = np.array([
    [-0.25, 0, 0.25, 0.25, 0], 
    [0, -0.25, 0, 0.25, 0.25], 
    [0.25, 0, -0.25, 0, 0.25], 
    [0.25, 0.25, 0, -0.25, 0],
    [0, 0.25, 0.25, 0, -0.25]
  ])
  # note M is symmetric so we can use eigen vectors to solve for /bar{v}(t)
  #   see 6.3 notes
  if not check_symmetric(M):
    print("M is not symmetric! Can't compute VSS with eigen values")
    exit(1)
  

  h = W.dot(u) # (this is a matrix multiplication)
  print('h = ')
  print(h)

  # all eigven values are <= 1 so the network is stable!
  evals, evecs = np.linalg.eig(M)

  # calculate steady state using eigvenvalues
  vss = np.zeros(5)
  for i in range(5):
    eval = evals[i]
    evec = evecs[:, i]
    #vss += (np.dot(h[:, 0], evec)) / (1 - eval) * evec
    #import pdb; pdb.set_trace()
    c_i = (np.dot(h, evec)) / (1 - eval)
    vss +=  c_i * evec
  print('final vss = ')
  print(vss)

  # TODO: understand why my answer is slightly different than the correct one on the quiz!
  #   (each component of the vector off by ~ +/- 0.02)
  #import pdb; pdb.set_trace()

# https://stackoverflow.com/a/52601850
def check_symmetric(a, tol=1e-8):
  return np.all(np.abs(a-a.T) < tol)

if __name__ == "__main__":
  main()