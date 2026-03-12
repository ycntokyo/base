#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:13:32 2020

@author: yuchangnan
"""


from sympy import *

x= Symbol('x')
#y= sin(x)

#yをxでミブン
#print(diff(y,x))

#y=E**(2*x)

#yをxで積分
#print(integrate(y,x))

#y=E**(2*x)

#print(integrate(y,(x,0,1)))

plot((x**2),(x,-5,5),title='test',xlabel='x',ylabel='x**2')

