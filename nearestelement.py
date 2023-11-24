# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 23:07:37 2023

@author: shubh
Finding the closest numbers to a given number in a sorted array
"""
lst=[1,2,3,4,5,12]
ele=int(input())
for i in range(len(lst)):
    min=abs(ele-lst[0])
    diff=abs(lst[i]-ele)
    if(diff<min):
        min=lst[i]
    else:
        continue
print(min)
        

