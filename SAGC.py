#!/usr/bin/python3

# This is a program that i've thought for help me in Analytic Geometry
# it is not perfect, cuz i'm newbie about programming, but i'm trying :D
# by @jeffersonraimon, 2021

from math import pow, sqrt

print("------------------------------------------------------------------------------")
print("                   SIMPLE ANALYTIC GEOMETRY CALCULATOR (SAGC)      ")
print("                         @jeffersonraimon | 2021    ")
print("------------------------------------------------------------------------------")

print("Select the option: ")
print("")
print("Distance of two coordinates in the Cartesian Plane [1]: ")
print("")
print("Medium point between two coordinates [2]: ")
print("")
print("The circumference between two coordinates [3]: ")
print("")
print("------------------------------------------------------------------------------")
option = int(input("Type your option: "))

if option == 1:

    print('')
    print("    Lets find the distance of two coordinates in the Cartesian Plane!!!")
    print('')

    x1 = int(input("Type the X from point A: "))
    y1 = int(input("Type the Y from point A: "))

    print("---------------------------------------")

    x2 = int(input("Type the X from point B: "))
    y2 = int(input("Type the Y from point B: "))

    d = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

    print(f'The distance is {d:0.2f}')

if option == 2:
    print('')
    print("    Lets find the medium point between two coordinates in the Cartesian Plane!!!")
    print('')

    x1 = int(input("Type the X from point A: "))
    y1 = int(input("Type the Y from point A: "))

    print("---------------------------------------")

    x2 = int(input("Type the X from point B: "))
    y2 = int(input("Type the Y from point B: "))

    mPX = (x1 + x2) / 2  # medium point X
    mPY = (y1 + y2) / 2  # medium point Y

    print(f'The medium point is {mPX:0.2f}, {mPY:0.2f}')
