###############################################
# Name: SAMPATH KUMAR MANNE
# Class: CMPS 5363 Cryptography
# Date: 04 Aug 2015
# Program 3 - Elliptical Curve
###############################################

import argparse
import sys
from fractions import Fraction
import elliptical as help

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="")
    parser.add_argument("-y1",dest="y1", help="")
    parser.add_argument("-x2",dest="x2", help="")
    parser.add_argument("-y2",dest="y2", help="")

    args = parser.parse_args()

    # Using Fractions function "from fractions import Fraction"
    # To initialize variables using the command line arguments as fractions.
    a =Fraction(args.a)
    b = Fraction(args.b)
    x1 = Fraction(args.x1)
    y1 = Fraction(args.y1)
    x2 = Fraction(args.x2)
    y2 = Fraction(args.y2)
    x3 = Fraction()
    y3 = Fraction()
    
    print("")
    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)
    print("----------------------------------------------------------------------")
    print("The curve equation after substituting values is y^2 = x^3 + {0}x + {1}".format(a,b))
    print("----------------------------------------------------------------------")

    # Initally initializing slope(m) to zero in float.
    m  = 0.0
    
    # Empty list to store the new points (X3,Y3) 
    Newpoint = []

    # If given points are same, we find the derivative (dy/dx) = 3x^2 + a / 2y
    # To get the tangent line at that point.
    if (x1 == x2) and (y1 == y2):
                
        print("=>Given points (x1,y1) and (x2,y2) are same")
        m = (3*x1**2)+ a / 2*y2

        #Function call to finding the new point and return x3,y3 coordinates to the list
        Newpoint = help.findNewPoint(x1,x2,y1,y2,a,b,m)

    # If given points have same y coordinates this condition is executed.       
    elif(y1 == y2):

        print("\n=>Two points (x1,y1) and (x2,y2) have same 'y' values i.e. y = %s"%y1)
        print("=>Given points form a horiontal line. Slope(m) is zero")
        print("----------------------------------------------------------------------")

        #For any Horizontal line slope is by default Zero.
        m = 0.0

        #Function call to finding the new point and return x3,y3 coordinates to the list
        Newpoint = help.findNewPoint(x1,x2,y1,y2,a,b,m)

    # If given points have same x coordinates this condition is executed and stops.         
    elif (x1 == x2):

        # For any vertical line slope is undefined or infinite.
        # Hence no need to find the slope and third Coordinate.
        
        print("\n=>Two points (x1,y1) and (x2,y2) have same 'x' values,i.e. x = %s"%x1)
        print("=>Given points from a vertical line. Hence, Slope(m) is infinity\n")
        print("----------------------------------------------------------------------")
        #Newpoint = help.findNewPoint(x1,x2,y1,y2,a,b,m)

    # If non of the above conditions are satisfied this condition is executed.
    else:

        # When we have 2 different points,slope is calucluated with the difference in y-Coordinates
        # by the difference in x-Coordinates
        
        print("=>Given points are different")
        m = (y2 - y1) / (x2 - x1)

        #To represent the slope in fraction.
        print("=>Hence the slope is %s"%Fraction(m).limit_denominator())
        print("----------------------------------------------------------------------")
        
        #Function call to finding the new point and return x3,y3 coordinates to the list
        Newpoint = help.findNewPoint(x1,x2,y1,y2,a,b,m)


if __name__ == '__main__':
    main()
