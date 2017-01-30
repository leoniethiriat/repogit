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
        
        #print(state.step)
        if state.step%4 == 0:
            return je.shoot(mystate.pos_sonbut())
        if state.step%3 == 0:
            tourchoisis = state.step
            while state.step != tourchoisis+30:
                return stratje.asb()
        if mystate.my_position != mystate.ball_position() and not mystate.procheduballon(): 
            return je.aller(mystate.ball_position())
        else:
            return je.shoot(mystate.pos_sonbut())
            

class StrategyDefense(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        je=Je(mystate)
        stratje = StratJe(je, mystate)
        
        
        if mystate.estdanscdd():
            return stratje.papp()
        
        
class StrategyGoal(Strategy):
    def __init__(self):
        Strategy.__init__(self,"GoalKeeper")
        
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        je=Je(mystate)
        
        if mystate.my_position != mystate.pos_monbut() and not mystate.danslescages():
            return je.aller(mystate.pos_monbut()) 
        #if mystate.prochedugoal() :
         #   return je.aller(mystate.())
    
## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",StrategyAttaquant()) #Strategie attaquant
team2.add("Ted",StrategyDefense())   #Strategie aleatoire
team1.add("Kerry", StrategyGoal())
team2.add("Fred", StrategyGoal())
team1.add("Saitaroro", StrategyDefense())
team2.add("Leonie", StrategyAttaquant())
team1.add("Saaroro", StrategyDefense())
team2.add("Leoie", StrategyAttaquant())

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
