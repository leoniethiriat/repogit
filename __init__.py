from strat import StrategyAttaquant, StrategyDefense, StrategyGoal
from soccersimulator.mdpsoccer import SoccerTeam



def get_team(numba):
    s = SoccerTeam(name="leoniro1")
    if numba == 1:
        s.add("totti", StrategyAttaquant())
        
    if numba == 2:
        s.add("totti",StrategyAttaquant())
        s.add("maldini", StrategyDefense())
    if numba == 4:
        s.add("totti",StrategyAttaquant())  
        s.add("buffon", StrategyGoal())
        s.add("delpiero", StrategyAttaquant())
        s.add("maldini", StrategyDefense())
    return s
    
        
            
