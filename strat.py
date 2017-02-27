from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
from soccersimulator import settings
from tools import MyState
from baseaction import Je, StratJe

## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-0.5,0.5))

class StrategyAttaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        je=Je(mystate)
        stratje = StratJe(je, mystate)
        
        
        if mystate.my_position != mystate.ball_position() and not mystate.procheduballon(): 
            return stratje.interception()
        else:
            return je.shoot1(mystate.ball_position().distance(mystate.pos_sonbut()),mystate.pos_sonbut()) #+ je.acceleration(mystate.ball_position(),500)
        #return stratje.interception() #+ je.shoot(mystate.post_sonbut())
            
class StrategyDefense(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        je=Je(mystate)
        stratje = StratJe(je, mystate)
           
        if mystate.my_position != mystate.ball_position() and not mystate.procheduballon() and mystate.balldanscdd():
            return stratje.interception()
        if mystate.procheduballon():
            return stratje.papp()
        if not mystate.balldanscdd():
            return stratje.meposid()
            
class StrategyDefense2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        je=Je(mystate)
        stratje = StratJe(je, mystate)
           
        if mystate.my_position != mystate.ball_position() and mystate.my_position.distance(mystate.ball_position())<(settings.PLAYER_RADIUS+settings.BALL_RADIUS)*10:
            return stratje.interception() + stratje.meposid()
        if mystate.procheduballon():
            return stratje.papp() 
        if not mystate.my_position.distance(mystate.ball_position())<(settings.PLAYER_RADIUS+settings.BALL_RADIUS)*5:
            return stratje.meposid()
        
class StrategyGoal(Strategy):
    def __init__(self):
        Strategy.__init__(self,"GoalKeeper")
        
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        je=Je(mystate)
        stratje = StratJe(je, mystate)
        
        if mystate.my_position != mystate.pos_monbut() and not mystate.danslescages():
            return stratje.meposig() 
        #if mystate.prochedugoal() :
         #   return je.aller(mystate.())
    