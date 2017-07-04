# -*- coding: utf-8 -*-
"""
Interaction between Python and Nextnano3 simulation program
"""

import numpy as np


def load_wave_func(folder):
    """Function is responsible for reading and loading into the program
    of simulation results from Nextnano program output files.
    Loads Wavefunctions"""
    filename = folder + '\sg_1band1\cb001_qc001_sg001_deg001_neu_cmplx.dat'

    print(filename)

