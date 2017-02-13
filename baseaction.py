
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.utils import Vector2D
from soccersimulator import settings
from tools import MyState 
import math

class Je(object):

    def __init__(self, mystate):
        self.mystate = mystate

    def exp(self, x):
        return 5*(1-math.exp(-2*x))
        
    def puissance(self, x):
        return 5*x**2
        
    def aller(self,p):
        return SoccerAction(p-self.mystate.my_position, Vector2D())
    
    def shoot1(self,Uballgoal,p):
        return SoccerAction(Vector2D(), self.exp(Uballgoal)*(p-self.mystate.my_position))
        
    def shoot2(self,Uballgoal,p):
        return SoccerAction(Vector2D(),self.puissance(Uballgoal)*(p-self.mystate.my_position.normalize()))
    
    def acceleration(self, p, c):
        return SoccerAction(c*(p-self.mystate.my_position), Vector2D()) 
    
    #plongeon for the fame
    #def pftf(self):

   
    


class StratJe(object):
    
    
    def __init__(self, je, mystate):
        self.je = je
        self.mystate= mystate
        
    #degagement posi    
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

    #atk action
    def interception(self):
        return self.je.aller(self.mystate.ball_position()+self.mystate.ball_speed()*20) 
            
    #def action
    def degagement(self):
        return self.je.shoot(self.mystate.pos_sonbut())
    
    
    #mepositionne
    def meposig(self):
        return self.je.aller(self.mystate.pos_monbut())
    def meposid(self):
        pos = Vector2D(self.mystate.cdd(),self.mystate.my_position.y)
        return self.je.aller(pos)
            
            
        
    #passe offensive 
  # def pao