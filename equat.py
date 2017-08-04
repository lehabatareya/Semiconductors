# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 10:52:07 2017

@author: Алексей
"""
import numpy as np
import matplotlib.pyplot as plt

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
    

def fermi_dirac_1d(x):
    """
    UNCHECKED!!!
    Fermi-Dirac integral for the 1d density of states (order -1/2)
    Rational-form approximation from "H. M. Antia, Rational Function Approximations for Fermi–Dirac Integrals,
    Astrophysical Journal Supplement 84 (1993), 101–108"
    Relative error is 10^-12 according to author
    :param x: float, variable
    :return: float, integral value
    """
    if x < 2:
        y = np.exp(x)
        numerator = [1.71446374704454e+7, 3.88148302324068e+7, 3.16743385304962e+7, 1.14587609192151e+7,
                     1.83696370756153e+6, 1.14980998186874e+5, 1.98276889924768e+3, 1.0]
        denominator = [9.67282587452899e+6, 2.87386436731785e+7, 3.26070130734158e+7, 1.77657027846367e+7,
                       4.81648022267831e+6, 6.13709569333207e+5, 3.13595854332114e+4, 4.35061725080755e+2]
        return y * np.polynomial.Polynomial(numerator)(y) / np.polynomial.Polynomial(denominator)(y)
    else:
        y = 1 / x**2
        numerator = [-4.46620341924942e-15, -1.58654991146236e-12, -4.44467627042232e-10, -6.84738791621745e-8,
                     -6.64932238528105e-6, -3.69976170193942e-4, -1.12295393687006e-2, -1.60926102124442e-1,
                     -8.52408612877447e-1, -7.45519953763928e-1, 2.98435207466372, 1.0]
        denominator = [-2.23310170962369e-15, -7.94193282071464e-13, -2.22564376956228e-10, -3.43299431079845e-08,
                       -3.33919612678907e-6, -1.86432212187088e-4, -5.69764436880529e-3, -8.34904593067194e-2,
                       -4.78770844009440e-1, -4.99759250374148e-1, 1.86795964993052, 4.16485970495288e-1]
        return np.sqrt(x) * np.polynomial.Polynomial(numerator)(y) / np.polynomial.Polynomial(denominator)(y)


def fermi_dirac_3d(x):
    """
    Fermi-Dirac integral for the 3d density of states (order 1/2)
    Rational-form approximation from "H. M. Antia, Rational Function Approximations for Fermi–Dirac Integrals,
    Astrophysical Journal Supplement 84 (1993), 101–108"
    Relative error is 10^-12 according to author
    :param x: float, variable
    :return: float, integral value
    """
    if x < 2:
        y = np.exp(x)
        numerator = [5.75834152995465e+6, 1.30964880355883e+7, 1.07608632249013e+7, 3.93536421893014e+6,
                     6.42493233715640e+5, 4.16031909245777e+4, 7.77238678539648e+2, 1.0]
        denominator = [6.49759261942269e+6, 1.70750501625775e+7, 1.69288134856160e+7, 7.95192647756086e+6,
                       1.83167424554505e+6, 1.95155948326832e+5, 8.17922106644547e+3, 9.02129136642157e+1]
        return y * np.polynomial.Polynomial(numerator)(y) / np.polynomial.Polynomial(denominator)(y)
    else:
        y = 1 / x**2
        numerator = [4.85378381173415e-14, 1.64429113030738e-11, 3.76794942277806e-9, 4.69233883900644e-7,
                     3.40679845803144e-5, 1.32212995937796e-3, 2.60768398973913e-2, 2.48653216266227e-1,
                     1.08037861921488, 1.91247528779676, 1.0]
        denominator = [7.28067571760518e-14, 2.45745452167585e-11, 5.62152894375277e-9, 6.96888634549649e-7,
                       5.02360015186394e-5, 1.92040136756592e-3, 3.66887808002874e-2, 3.24095226486468e-1,
                       1.16434871200131, 1.34981244060549, 2.01311836975930e-1, -2.14562434782759e-2]
        return x * np.sqrt(x) * np.polynomial.Polynomial(numerator)(y) / np.polynomial.Polynomial(denominator)(y)


if __name__ == '__main__':
    x = [i*0.01 for i in range(-700, 700)]
    y = [fermi_dirac_3d(i) for i in x]
    z = np.exp(x) * np.sqrt(np.pi) / 2
    plt.plot(x, z)
    plt.plot(x, y)
    plt.yscale('log')
    plt.grid(True)
    plt.axis([-7, 7, 1e-3, 10])
    plt.show()