# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:37:00 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x=100.1
y=100.1
z=100.1

mc.player.setPos(x,y,z)
