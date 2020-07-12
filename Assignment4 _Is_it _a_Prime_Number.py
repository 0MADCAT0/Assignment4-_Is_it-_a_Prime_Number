# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:17:49 2020

@author: MADCAT
"""
while True:
    try:
        x = abs(int(input("enter an integer or enter a letter to exit:")))
        if x == 2 :        
            print(f"{x} can divided by only 1 and itself, so it is a prime number") 
        elif x == 0 :
            print ("0 is not a prime number")
        i = 1
        cont = True
        while x != 0 and i != x-1:
            i += 1 
            if x % i == 0:
                print(f"{x} can divided by {i}, so it is not a prime number")
                cont = False 
            elif x == 1:
                print(f"{x} can divided by only itself, so it is not a prime number")
                break
            else :
                if i == x-1 and cont:
                    print(f"{x} can divided by only 1 and itself,\
so it is a prime number")
         # only for num = 2
        
    except ValueError:
        print("güle güle")
        break