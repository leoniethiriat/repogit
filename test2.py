from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
from soccersimulator import settings


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
        if(id_team==1):
            return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)-state.player_state(id_team,id_player).position)
        
        else:
            return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,Vector2D(0,settings.GAME_HEIGHT/2)-state.player_state(id_team,id_player).position)

class StrategyDefense(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,Vector2D.create_random(-0.5,0.5))
    
## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",StrategyAttaquant()) #Strategie attaquant
team2.add("Paul",StrategyDefense())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
