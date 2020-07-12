# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:17:49 2020

@author: MADCAT
"""


x = int(input("enter an integer:"))

i = 1
cont = True
while i != x:
   i += 1 
   if x-1 % i == 0:
       print(f"{x} can divided by {i}, so it is not a prime number")
       cont = False 
   elif x == 1:
        print(f"{x} can divided by only itself, so it is a prime number")
        break
   else :
       if i == x-1 and cont:
           print(f"{x} can divided by only 1 and itself, so it is a prime number")
    
