###############################################
# Name: SAMPATH KUMAR MANNE
# Class: CMPS 5363 Cryptography
# Date: 04 Aug 2015
# Program 3 - Elliptical Curve
###############################################

import math
import random
import os
import sys
import re
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt

# Function takes all the coordinates given in the command line to find the third vertex
# on the elliptical curve.
def findNewPoint(x1,x2,y1,y2,a,b,m):

    # Condition to check of the given points are on the curve.
    # If present we find the third point or else give error message.
    if ((x1**3) + a*x1 + b - (y1**2) == 0) and ((x2**3) + a*x2 + b - (y2**2) == 0):
        print("\nNew Vertex (x3,y3)")

        x3 = (m**2) - x1 - x2
        #To represent the x3 in fraction.
        print("x3 = %s"%Fraction(x3).limit_denominator())
        
        y3 = m*(x3 - x1) + y1
        #To represent the x3 in fraction.
        print("y3 = %s"%Fraction(y3).limit_denominator())
        
        print("")
        print("----------------------------------------------------------------------")

        # 'n' is a list of absolute values of the coordinates.
        n = [abs(x1),abs(x2),abs(x3),abs(y1),abs(y2),abs(y3)]

        # Condition to check for the largest value to be used in plotting the curve.
        while len(n) != 1:
            if n[0] > n[1]:
                n.remove(n[1])
            else:
                n.remove(n[0])
        largest = n[0]
        print("The largest number among the co-ordinates is '%s' used to plot the curve.\n"%largest)
        print("-----------------------------*END*--------------------------------------")

        # Adding +2 to make sure the points are in the plot.
        w = largest + 2 
        h = largest + 2

        # Function to plot the curve
        createPlot(x1,x2,x3,y1,y2,y3,a,b,m,w,h)
        
    else:
        print("=>Please Try Again : Given Points (x1,y1) and (x2,y2) are not on the elliptical curve. Please enter valid points\n")
        print("-----------------------------*END*--------------------------------------")
    return [x3,y3]


def createPlot(x1,x2,x3,y1,y2,y3,a,b,m,w,h):
    
    # Annotate the plot with your name using width (w) and height (h) as your reference points.
    an1 = plt.annotate("Sampath Manne", xy=(-w+2 , h-2), xycoords="data",
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))

    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a*x + b ), [0])

    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro')

    # Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    plt.plot(x2, y2,'ro')

    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    # Use a contour plot to draw the line (in pink) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))

    # I hard coded the third point, YOU will use good ol mathematics to find
    # the third point
    plt.plot(x3, y3,'yo')

    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1,y3+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    # Show a grid background on our plot
    plt.grid()

    # Show the plot
    plt.show()

