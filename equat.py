# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 10:52:07 2017

@author: Алексей
"""

def varshni(temp, eg, a, b):
    """
    Varshni equation for the temperature-dependent band gap
    
    temp - absolute temperature [K]
    eg - band gap T = 0 K [eV]
    a - alpha constant [eV/K]
    b - beta constant [K]
    
    returns energy [eV]
    """
    
    return (eg - a * temp**2 / (temp + b))
    
    