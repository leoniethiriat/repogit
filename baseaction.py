# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:21:43 2017

@author: 3407195
"""

from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.utils import Vector2D
from soccersimulator import settings
from tools import MyState 

class Je(object):

    def __init__(self, mystate):
        self.mystate = mystate

        
        
    def aller(self,p):
        return SoccerAction(p-self.mystate.my_position, Vector2D())
    
    def shoot(self,p):
        return SoccerAction(Vector2D(), p-self.mystate.my_position)
        
    def degagement(self):
        return SoccerAction(Vector2D(), Vector2D.create_random(-0.5,0.5)-self.mystate.my_position)
        #champ de defense        
    def estdanscdd(self):
        if self.mystate.idt == 1:
            return self.mystate.ball_position().x<=37.5
        return self.mystate.ball_position().x<=112.5
    #plongeon for the fame
    #def pftf(self):

   
    


class StratJe(object):
    
    
    def __init__(self, je, mystate):
        self.je = je
        self.mystate= mystate
        
        
    #passe au goal
    #def pag(self):
    
    #arrete de suivre la balle! 
    def asb(self):
        if self.mystate.equipierleplusproche == self.mystate.ball_position():
            return self.je.aller(self.mystate.my_position)
    
    
    #passe au plus proche 
    def papp(self):
        
        if self.mystate.my_position != self.mystate.ball_position() and not self.mystate.procheduballon(): 
            return self.je.aller(self.mystate.ball_position())
        else:
            return self.je.shoot(self.mystate.equipierleplusproche)
            
            
        
    #passe offensive 
  # def pao