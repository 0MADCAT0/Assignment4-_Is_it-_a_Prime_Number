# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:17:49 2020

@author: MADCAT
"""


x = int(input("enter an integer:"))

i = 1

while i != x-1:
   i += 1 
   if x % i == 0:
       print(f"{x} can divided by {i}, so it is not a prime number")

   elif x ==1:
        print(f"{x} can divided by only itself, so it is a prime number")
        break
   elif i == x-1 and x % (x-1) != 0 :
       print(f"{x} can divided by only 1 and itself, so it is a prime number")
    