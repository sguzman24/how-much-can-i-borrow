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

def computesN(Pmt, PV, r):
    r = r/12 # converts to a % per month
    r = r/100 # coverts APR to a decimal
    # given Pmt, PV, r, we compute n
    n = - np.log (1-PV*r/Pmt) / np.log(1+r)
    n = round(n,1)
    return n
    
    


while(True):
    
       choice = int(input('Enter choice 1 for PV, 2 for Pmt , 3 for months in debt -> '))
       if (choice == 1 or choice == 2 or choice == 3):
           break
       else: 
            print (f"enter a 1 , 2, or 3 you entered {choice}.")
    
    
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
    
if choice == 3:
    Pmt = input ("enter Pmt:")
    Pmt = float (Pmt)
    print (f"Pmt = {Pmt} /n")
    PV = input("enter PV:")
    PV = float(PV)
    print(f"PV = {PV} /n")
    r = input("enter interest APR:")
    r = float(r)
    print(f"interest = {r: 0.3f} /n")
    MonthsMakingPayment = computesN(Pmt,PV,r)
    MonthsMakingPayment = np.round(MonthsMakingPayment, 2)
    print(f"{MonthsMakingPayment}")
               
        
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