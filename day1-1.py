# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:06:49 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x=100
y=100
z=100

mc.player.getTilePos(x,y,z)
