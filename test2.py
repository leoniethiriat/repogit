from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
from soccersimulator import settings
from tools import MyState

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
        
        if mystate.my_position() != mystate.ball_position() and not mystate.procheduballon(): 
            return mystate.aller(mystate.ball_position())
        else:
            return mystate.shoot(mystate.pos_sonbut())


class StrategyDefense(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        idt, idx = mystate.ennemieleplusproche()
        if state.player_state(idt,idx).position.x > 75:
            return mystate.aller(state.player_state(idt,idx).position)
            
class StrategyGoal(Strategy):
    def __init__(self):
        Strategy.__init__(self,"GoalKeeper")
        
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        
       # if mystate.my_position != mystate.pos_monbut() and not mystate.danslescages():
        #    return mystate.aller(mystate.pos_monbut()) 
        if mystate.prochedugoal() :
            return mystate.aller(mystate.ball_position())
    
## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",StrategyAttaquant()) #Strategie attaquant
team2.add("Paul",StrategyDefense())   #Strategie aleatoire
team1.add("Kerry", StrategyGoal())
team2.add("Fred", StrategyGoal())

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
