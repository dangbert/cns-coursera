#!/usr/bin/env python3
import numpy as np



def main():
    q1_2()


def q1_2():
    """
    for question 1, our largest eigenvalue is evals[0] = 0.23611874,
    which has corresponding eigenvectors evec0 = evevs[:,0] = array([0.75774021, 0.65255634])
    evec0[0] / evec0[1] = 1.1611874208078343,
    looking through the multiple choice options, only one weight vector is proportional to evec0
    (w = [-1.5155, -1.3051]).
    We look for this because "for large t, the largest eigen value term dominates".
    """
    Q = np.array([[0.15, 0.1], [0.1, 0.12]])
    print(Q)
    # n eigen vectors (2*n matrix)
    evals, evecs = np.linalg.eig(Q)
    print("eigen values:")
    print(evals)
    print("eigen vectors:")
    print(evecs)

if __name__ == "__main__":
    main()
