# -*- coding: utf-8 -*-
"""
Problem 1
Fill in the Line class methods to accept coordinate as a pair of tuples and return the slope and distance of the line.
"""

import math

class Line(object):
  p1, p2


  def __init__(self,coor1,coor2):
    #Initialize instance attributes with tuples (x1,y1)  and (x2,y2)
    p1, p2 = coor1, coor2
    
    
  def distance(self):
    #Calculate the length of the segment (line)
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


  def slope(self):
    #Return the slope of a line going through the ends ( the 'a' in y=ax+b)
    return (p2[1]-p1[1])/(p2[0]-p1[0])

coordinate1 = (3,2) 
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()

"""Problem 2
Fill in the class
"""

class Cylinder(object):


  def __init__(self,height=1,radius=1):
    self.height = height
    self.radius = radius


  def volume(self):
    return math.pi * self.radius**2 * self.height
    

  def surface_area(self):
    return 2*math.pi*self.radius * self.height + math.pi*self.radius**2*2

c = Cylinder(2,3)
c.volume()
c.surface_area()
    #rows = sum(1 for line in open(self.filename)) - 1
    #cols = int(sum(len(line.split(";")) for line in open(self.filename)) / (rows + 1))
    #print(cols)

# !echo "Name;Age;Weight;Height\nJohn;6;25;123\nMary;4;18;98\nJack;8;32;138" > data.txt

"""Problem 3
Write a class that takes a filename as an argument, open it and reads its content into a 2D matrix of values (an array of arrays: [[1,2],[3,4]]). The class should define a special function info() which prints out statistical information about column values in the file. Assume that the first row in the file specifies the column names


HINTS:
For ptint use somtehing similar to: print(f“‘{(123+98+138)/3:^20.2f}’”);
"""

import csv
import numpy as np
import pandas as pd

class DataFile(object):

  def __init__(self, filename='undef'):
    self.filename = filename
    reader = csv.reader(open(self.filename, "rt"), delimiter=';')
    i = list(reader)
    dataframe = pd.DataFrame(i[1:], columns=i[0], dtype=float)
    self.data = dataframe
    self.data.transpose()
    print(self.data)
  
  def info(self):
    print("\tMin\tMax\tAvg")
    with open(self.filename,"r") as f:
      xd = f.readline()
    #print(xd + "\t" + min() + "\t" + max() + avg())
    with open(self.filename, "r") as f:
      lines = f.read().splitlines()
    col_names = lines[0].split(";")
    #print(col_names + "\t" + min(";") + "\t" + max() + avg()) 
    data = []
    for i in range(1,len(lines)):
      new_line = lines[i].split(";")


  def avg(self, colnum=0, colname=''):
    #The column name or colnum can be provided alternatively
    return 1
    

  def min(self, colnum=0, colname=''):
    return 1


  def max(self, colnum=0, colname=''):
    return 1

datafile = DataFile("/content/data.txt")
datafile.info()

"""Problem 4
Write a context manager and example of its usage (just print some result to terminal) which will fetch the data about teachers from ISOD API, and as a variable it should return an ordered by lastname list of teachers. Please investigate on your own, using type function what is return by json.loads(s.text).

You can use the code as a starting point:
"""

import requests
import json

s = requests.get("https://isod.ee.pw.edu.pl/isod-portal/wapi?q=list_teachers&sem2019Z&urlinfo=null&format=JSON&orgunit=ZETiIS")

j = json.loads(s.text)

#all professors with all data
print(sorted(j2['teachers'], key=methodcaller('get','lastname')))

#list containing only surnames
print("Ordered by lastname list of teachers:")
for i in sorted(j2['teachers'], key=methodcaller('get','lastname')):
  print(i['lastname'])
