# -*- coding: utf-8 -*-
"""
This file contains physical constants for the simulations of semiconductor properties in semiconductors module
and coefficients to transform units of measurements
"""

# Physical constants
M0 = 9.10938356e-31     # electron rest mass (kilograms)
H2pi = 6.626070040e-34  # Planck constant (J s) * 2 pi
H = 1.0545718e-34       # Planck constant (J s)
E = 1.6021766208e-19    # Electron charge (Coulomb)
K = 1.38064852e-23      # Bolzman constant (J / K)

# Units transformation coefficients
# To transform: multiplicate quantity value and transformation coefficient
ev_to_j = E         # Energy units eV to Joule
j_to_ev = 1/E       # Energy nits Joule to eV
ev_to_temp = E / K  # Energy units eV to Kelvin
temp_to_ev = K / E  # Energy units Kelvin to eV

if __name__ == '__main__':
    print(300*temp_to_ev)
