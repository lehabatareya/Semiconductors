# -*- coding: utf-8 -*-
"""
Interaction between Python and Nextnano3 simulation program
"""

import numpy as np
import matplotlib as plt


def read_data(file_name):
    """
    Function reads the Nextnano output file and returns ndarray of data
    :param file_name: String adress of the Nextnano output file
    :return: ndarray of data in float format
    """
    with open(file_name) as data:
        data.readline()     # neglect first line of file, just names of columns
        return_data = []
        for line in data:
            number_list = []        # list of numbers in one string of file
            number = ''
            for letter in line:     # divide line into numbers
                if not letter.isspace():
                    number += letter
                else:
                    if number:
                        number_list.append(number)
                        number = ''
            return_data.append(number_list)
        return np.array(return_data, dtype=np.float64)


def load_el_wave_func2(folder, subband_ind):
    """
    Loads squared electron wavefunction for given subband index from the simulation results of Nextnano
    :param folder: String adress of the Nextnano simulation folder
    :param subband_ind: Int number of electron subband index, starting from 1
    :return: ndarray, first column - coordinates, second column - squared wave function in [1/nm] units
    """
    file_name = folder + '\sg_1band1\cb001_qc001_sg001_deg001_neu.dat'
    all_data = read_data(file_name)
    return all_data[:, (0, subband_ind)]


def load_el_mass(folder):
    """
    Loads electron effective mass profile from the simulation results of Nextnano
    :param folder:  String adress of the Nextnano simulation folder
    :return: ndarray, first column - coordinates, second column - effective mass in elementary charge units
    """
    file_name = folder + '\material_parameters\cb-masses.dat'
    all_data = read_data(file_name)
    return all_data[:, (0, 1)]
