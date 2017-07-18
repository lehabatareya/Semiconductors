# -*- coding: utf-8 -*-
"""
Module contains classes and functions to determine the semiconductor 
heterostructures design and materials. Includes database of all materials.

Material database. Contains all the pure and compound semiconductor 
parameters as dictionaries. 
PURESEM - all pure semiconductors (group IV, III-V and others)
BINALLOY - all alloy semiconductors from two components (IV/IV, III-V/III-V)

*****************************************************************
Names for the material parameters in the database:
 
PURESEM:
lat - lattice constant (at 300 K) [nm]
lat_temp -  lattice constant temperature coefficient [nm/K]
    
VBen - energy of the top of the valence band [eV]
BGGen, BGLen, BGXen - T = 0 K band gap for Gamma (L,X) CB minimum [eV]
BGGa, BGLa, BGXa - alpha Vashni parameter for Gamma (L, X) CB minimum [eV/K]
BGGb, BGLb, BGXb - beta Varshni parameter for Gamma (L, X) CB minimum [K]
VBSO - band gap for the spin-orbit splitting [eV]

CBGdeg, CBLdeg, CBXdeg - degeneracy of the Gamma-CB minimum (including spin)

CBGmass - (mx,my,mz) effective mass in Gamma CB minimum for 3 principal axes
CBLmass --//-- for L-CB minimum
CBXmass --//-- for X-CB minimum
Lutting - (g1, g2, g3) - Luttinger parameters for the valence band

BINALLOY:
sem - (sem1, sem2) - names of 2 semiconductors from PURESEM for the alloy

*****************************************************************
Also you can overwrite some of the default database parameters for pure 
or alloy semiconductors. Use parameter 'overwrite' when assigning materials.
overwrite is a dictionary with keys from PURESEM, BINALLOY. Also overwrite
can contain some additional parameters to adjust band structure:
EnShift - shifts all the bands in semiconductor by the same energy [eV]

To adjust band parameters for pure semiconductors with overwrite:
Use keys from PURESEM dictionary to adjust some material parameters
Use EnShift to adjust band offsets

To adjust band parameters for alloy semiconductors:
Use 'overwrite1' and 'overwrite2' to adjust some parameters for pure component
semiconductors
Use 'overwrite' with keys from BINALLOY to adjust bowing
EnShift - shifts all the bands in semiconductor by the same energy [eV]
Also you can assign some parameters manually with 'overwrite' (in this case 
these parameters are included in the model manually and default parameters are
not used):

VB - assigns valence band position [eV]
BGG, BGL, BGX - assigns band gaps for the Gamma (L,X) bands
    
****************************************************************
@author: Alexey Klochkov

References:
    Band parameters:
    [1] I. Vurgaftman, J. R. Meyer, and L. R. Ram-Mohan
    Band parameters for III–V compound semiconductors and their alloys
    J. Appl. Phys. 89, 5815 (2001); doi: 10.1063/1.1368156
    
    Band offsets for valence bands:
    [2] Su-Huai Wei and Alex Zunger
    Calculated natural band offsets of all II–VI and III–V semiconductors:
    Chemical trends and the role of cation d orbitals
    Appl. Phys. Lett. 72, 2011 (1998); doi: 10.1063/1.121249
"""

import matplotlib.pyplot as plt

import equat

PURESEM = {
           'GaAs' : {'lat': 5.65325, 'lat_temp': 3.88e-5,
                     'VBen': 1.46, 'VBSO': 0.341,
                     'BGGen': 1.519, 'BGGa': 0.5405e-3, 'BGGb': 204.0,
                     'BGLen': 1.815, 'BGLa': 0.605e-3, 'BGLb': 204.0,
                     'BGXen': 1.981, 'BGXa': 0.46e-3, 'BGXb': 204.0,
                     'CBGdeg': 2, 'CBLdeg' : 8, 'CBXdeg': 6,
                     'CBGmass': (0.067, 0.067, 0.067), 
                     'CBLmass': (1.9, 0.0754, 0.0754),
                     'CBXmass': (1.3, 0.23, 0.23),
                     'Lutting': (6.98, 2.06, 2.93)
                     }, 
           'AlAs' : {'lat': 5.6611, 'lat_temp': 2.9e-5,
                     'VBen': 0.95, 'VBSO': 0.28,
                     'BGGen': 3.099, 'BGGa': 0.885e-3, 'BGGb': 530.0,
                     'BGLen': 2.46, 'BGLa': 0.605e-3, 'BGLb': 204.0,
                     'BGXen': 2.24, 'BGXa': 0.7e-3, 'BGXb': 530.0,
                     'CBGdeg': 2, 'CBLdeg' : 8, 'CBXdeg': 6,
                     'CBGmass': (0.15, 0.15, 0.15), 
                     'CBLmass': (1.32, 0.15, 0.15),
                     'CBXmass': (0.97, 0.22, 0.22),
                     'Lutting': (3.76, 0.82, 1.42)
                     }
           }

BINALLOY = {
          'AlGaAs':{'sem': ('AlAs', 'GaAs'), 
                    'VBbow' : 0.0, 'BGGbow' : 0.0, 
                    'BGLbow' : 0.0, 'BGXbow' : 0.0,
                    }
          }

class mater_pure():
    """
    Contains all the material parameters for pure semiconductors (not compound)
    """
    
    def __init__(self, matname, overwrite = {}):
        """
        Loads semiconductor parameters from the semiconductor database
        for the given semiconductor name
        
        matname - name of the semiconductor from the PURESEM dictionary
        overwrite - dictionary with parameters which overwrites default 
        material parameters from the database. All bands can be shifted 
        with the EnShift key in overwrite
        """
        self.name = matname         # default material parameters
        self.param = overwrite      # overwrite default parameters
    
    def VBH(self):
        """Returns heavy hole valence band energy position"""
        return (self.param.get('VBen', PURESEM[self.name].get('VBen')) + 
                self.param.get('EnShift', 0.0)
                )
        
    def VBL(self):
        """Returns light hole valence band energy position"""
        return (self.param.get('VBen', PURESEM[self.name].get('VBen')) + 
                self.param.get('EnShift', 0.0)
                )
        
    def VBSO(self):
        """Returns energy position  of the spin-orbit splitted valence band"""
        return (self.param.get('VBen', PURESEM[self.name].get('VBen')) -
                self.param.get('VBSO', PURESEM[self.name].get('VBSO')) + 
                self.param.get('EnShift', 0.0)
                )
        
    def BGG(self, temp = 300.0):
        """Returns band gap for the Gamma conduction band to valence band"""
        
        eg = equat.varshni(temp, 
                           self.param.get('BGGen', PURESEM[self.name].get('BGGen')),
                           self.param.get('BGGa', PURESEM[self.name].get('BGGa')),
                           self.param.get('BGGb', PURESEM[self.name].get('BGGb')),
                           )
        return eg
    
    def BGL(self, temp = 300.0):
        """Returns band gap for the L conduction band to valence band"""
        
        eg = equat.varshni(temp, 
                           self.param.get('BGLen', PURESEM[self.name].get('BGLen')),
                           self.param.get('BGLa', PURESEM[self.name].get('BGLa')),
                           self.param.get('BGLb', PURESEM[self.name].get('BGLb')),
                           )
        return eg
        
    def BGX(self, temp = 300.0):
        """Returns band gap for the X conduction band to valence band"""
        
        eg = equat.varshni(temp, 
                           self.param.get('BGXen', PURESEM[self.name].get('BGXen')),
                           self.param.get('BGXa', PURESEM[self.name].get('BGXa')),
                           self.param.get('BGXb', PURESEM[self.name].get('BGXb')),
                           )
        return eg
        
    def CBG(self, temp = 300.0):
        """Returns Gamma conduction band position"""
        
        return (self.VBH() + self.BGG())
        
    def CBL(self, temp = 300.0):
        """Returns L conduction band position"""
        
        return (self.VBH() + self.BGL())
        
    def CBX(self, temp = 300.0):
        """Returns X conduction band position"""
        
        return (self.VBH() + self.BGX())
        
    def mg(self):
        """Returns Gamma conduction band mass (without nonparabolicity)
        currently the (100) mass is returned 
        To add: orientation dependent mass tensor"""
        
        return self.param.get('CBGmass', PURESEM[self.name].get('CBGmass'))[0]
    
class mater_alloy_double():
    """
    Contains all the material parameters for alloy semiconductors consisting of
    two pure semiconductors
    """
    
    def __init__(self, matname, overwrite = {}, ovrwrt1 = {}, ovrwrt2 = {}):
        """
        Loads semiconductor parameters from the semiconductor database
        for the given semiconductor name from BINALLOY
        
        matname - name of the semiconductor from the BINALLOY dictionary
        overwrite - dictionary with parameters which overwrites default 
        ovrwrt1, ovrwrt2 - dictionaries with parameters which overwrite default
        parameters for component semiconductors 1 and 2
        """
        self.name = matname
        self.mat1 = mater_pure(BINALLOY[self.name]['sem'][0], ovrwrt1)
        self.mat2 = mater_pure(BINALLOY[self.name]['sem'][1], ovrwrt2)
        self.param = overwrite
        
    def VBH(self, x):
        """Returns heavy hole valence band energy position for the alloy with
        the given content"""
        
        mean_VB = (x * self.mat1.VBH() + (1 - x) * self.mat2.VBH() -
                   x * (1 - x) * self.param.get('VBbow', BINALLOY[self.name].get('VBbow', 0.0))
                   )
                   
        return (self.param.get('VBen', mean_VB) + 
                self.param.get('EnShift', 0.0)
                )
    
    def CBG(self, x):
        """Returns Gamma CB energy position for the alloy with the given x"""
        
        mean_CBG = (x * self.mat1.CBG() + (1 - x) * self.mat2.CBG() -
                   x * (1 - x) * self.param.get('VBbow', BINALLOY[self.name].get('VBbow', 0.0))
                   )
    
AlGaAs = mater_alloy_double('AlGaAs', {'EnShift': 0.0})
print(AlGaAs.VBH(0.3))
xes = [i*0.1 for i in range(11)]
vb = [AlGaAs.VBH(x) for x in xes]
plt.plot(xes, vb)

