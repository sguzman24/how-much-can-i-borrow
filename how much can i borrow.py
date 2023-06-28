#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:33:32 2023

@author: sethguzman
"""
def computesPmt(PV, r , n):
        r = r/100
        r = r/12
        Pmt = r * PV/(1-(1+r)**-n)
        return Pmt
    
    
def computesPV(PV, r, n):
        r = r/100
        r = r/12
        PV = (1-(1+r)**(-n)) * PV / r
        return PV
    
import numpy as np

while(True):
    
       choice = int(input('Enter choice 1 for PV, 2 for Pmt -> '))
       if (choice == 1 or choice == 2):
           break
       else: 
            print (f"enter a 1 or 2, you entered {choice}.")
    
    
if choice == 2:
    PV = input('Enter PV: ')
    PV = float(PV)
    print(f"PV = {PV} /n")

    r = input('Enter interest APR: ')
    r = float(r)
    print(f"interest = {r: 0.3f} /n")

    n = int(input('Enter how many months: '))
    print(f"n = {n} per month")

    pmt = computesPmt(PV, r, n)
    pmt = np.round(pmt, 2)
    print(f"The payment is $ {pmt} per month")
        
if choice == 1:
    Pmt = input ('enter Pmt: ')
    Pmt = float (Pmt)
    print (f"Pmt = {Pmt} /n")
    r = input ('enter intrerest APR: ')
    r = float(r)
    print(f"interest = {r: 0.3f} /n")
    n =int(input('number of mobths:'))
    print(f"n = {n} per month")
    PV = computesPV(Pmt, r, n)
    PV = np.round(PV, 2)
    print(f"The payment i can borrow is $ {PV: 0.2f} per month")