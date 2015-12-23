"""
This module contains all the utility and mathematical functions
required for this projects.

Module contains the following Functions

1. Distance - To compute distance between two images
    - The following distance metrics are considered
            - L1 distance
            - Euclidean or L2 distance
            - City Block or Manhattan distance
            - Cosine distance
            - Mahanalobis distance

"""

from math import sqrt


def is_vector(ip):

    if :
        return True
    else:
        return False

def distance(x, y, dist_type="euclidean"):

    if is_vector(x) and is_vector(y) == True:
        if dist_type == 'euclidean' or 'l2':
            dist = (x-y)
            return dist

        if dist_type == 'l1':
            dist = (x-y)
            return dist

        if dist_type == 'cosine':
            dist = (x-y)
            return dist

        if dist_type == 'city block' or 'manhattan':
            dist = (x-y)
            return dist

        if dist_type == 'mahanalobis':
            dist = (x-y)
            return dist

    else:
        print 'Error: Non vector arguments, The input arguments should be vectors '