#from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
#from soccersimulator.utils import Vector2D
#from soccersimulator import settings
#from tools import MyState
#from baseaction import Je, StratJe
from __init__ import get_team

simu = Simulation(get_team(1),get_team(2))
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
