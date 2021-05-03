#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This script demonstrates multi inheritance

References:
Classes in Python:
    https://docs.python.org/3/tutorial/classes.html#multiple-inheritance

'''

# Latest version can be found at https://github.com/dakside/pydemo
# @author: Le Tuan Anh <tuananh.ke@gmail.com>
# @license: MIT

class Device():
    def __init__(self, ID, brand, *args, **kwargs):
        print("  Begin Device init")
        print(f"    Set Device.ID to {ID}")
        self.ID = ID
        print(f"    Set Device.brand to {brand}")
        self.brand = brand
        print("  After Device init")

    def __repr__(self):
        return f"Device(ID={repr(self.ID)}, brand={repr(brand)})"
        
    def __str__(self):
        return self.ID


class MusicPlayer(Device):

    def __init__(self, ID, brand, color, *args, **kwargs):
        print("Begin MusicPlayer init")
        Device.__init__(self, ID, brand, *args, **kwargs)
        print(f"Set MusicPlayer.color to {color}")
        self.color = color
        print("After MusicPlayer init")


class Computer(Device):

    def __init__(self, ID, brand, cpu, *args, **kwargs):
        print("Begin Computer init")
        Device.__init__(self, ID, brand, *args, **kwargs)
        print(f"Set Computer.cpu to {cpu}")
        self.cpu = cpu
        print("After Computer init")


class MoviePlayer(Device):

    def __init__(self, ID, brand, disc_format, *args, **kwargs):
        print("Begin MoviePlayer init")
        Device.__init__(self, ID, brand, *args, **kwargs)
        print(f"Set MoviePlayer.disc_format to {disc_format}")
        self.disc_format = disc_format
        print("After MoviePlayer init")


class OrangePC(MusicPlayer, Computer, MoviePlayer):

    def __init__(self, ID, brand, color, cpu, disc_format, series, *args, **kwargs):
        print("Before OrangePC init")
        MusicPlayer.__init__(self, ID, brand, color)
        Computer.__init__(self, ID, brand, cpu)
        MoviePlayer.__init__(self, ID, brand, disc_format)
        print(f"Set OrangePC.series to {series}")
        self.series = series
        print("After OrangePC init")


orange_pro = OrangePC(ID="CheeseNote Pro 1", brand="Orange", color="red", cpu="Outtel", disc_format="DVD", series="CP1")

