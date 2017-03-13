from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz
import logging
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
from sklearn.tree 	import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import os.path
from tools import MyState
from baseaction import *
from arbrematrice import *

team2 = SoccerTeam("team2")
team2.add("rien 1", StrategyAttaquant())
team2.add("rien 2", StrategyDefense())

def jouer_arbre(dt):
    ####
    # Utilisation de l'arbre
    ###
    dicmatrice = {"Fonce":FonceStrategy(),"Static":StaticStrategy(),"Attaquant":StrategyAttaquant(), "Defense":StrategyDefense(), "GoalKeeper": StrategyGoal()}
    treeStrat1 = DTreeStrategy(dt,dicmatrice,my_get_features)
    treeStrat2 = DTreeStrategy(dt,dicmatrice,my_get_features)
    team3 = SoccerTeam("Arbre Team")
    team3.add("Joueur 1",treeStrat1)
    team3.add("Joueur 2",treeStrat2)
    simu = Simulation(team2,team3)
    show_simu(simu)
    
if __name__=="__main__":
    fn = "test_states.jz"
    if not os.path.isfile(fn): 
        entrainement(fn)
    dt = apprentissage(fn)
    jouer_arbre(dt)