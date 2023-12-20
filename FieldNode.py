#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:07:14 2023

@author: william
"""
import numpy as np
import pandas as pd


# Need something that makes already visited nodes easier to access
# How to make each touch of the node grease the path to it?

# Should contain a database of vectors with g values and create nodes
class Field(object):

    def __init__(self):

        self.name = "Field"
        self.field = pd.DataFrame()
        iVec = np.array([1, 0, 1, 1, 1])
        origin = Node(1, iVec, 0)
        Impulse(0, origin, cl=1)

    def display_node_vals(self):
        # For each node in the field, display the value. Result should be 
        # visually rendered at the very least in 2D.
        pass


class Node(object):

    def __init__(self):
        # neighbours is the collection of weights assigned to surrounding
        # Nodes, these weights should increment each time the path is taken:
        # effectively greasing the most active pathways
        self.neigbours = np.array([None, None, None, None])
        self.g = 0

    # inacted when an impulse "crosses" the node
    def pulse(self):
        self.g = self.f(self.g)
        self.update_weights()

    def update_weights(self):
        # before moving the pulse to the next node, "grease the pathways" by
        # incrementing the weights by both the size of the impulse and the
        # amount that the path is already "greasy". The weights should be a 
        # four value array (N/E/S/W in 2D)
        pass

class Impulse(object):

    # G is the new value at the vector as a function of the old
    # nVec is the vector with which the future node will be created
    # cl is the CHAIN LENGTH of connected nodes so far
    def __init__(self, g, pVec, cl):
 
        self.cl = cl + 1
        self.g = self.f(g)

        nVec = self.vecfunc(pVec)
        print(g)
        # Store new vector in database
        # access database through a parent class

        if not self.g <= 0:
            Node(self.g, nVec, self.cl)

    # increment the g factor (grease factor)
    # decreases signal according to the length of the chain
    def f(self, g):
        return g + (1 - self.cl / 100)

    def vecfunc(self, r):
        return r

    # this
    def fire():
        pass
