from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz
import logging
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
from sklearn.tree 	import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import os.path
from tools import MyState
from baseaction import *


## Strategie aleatoire
class FonceStrategy(Strategy):
    def __init__(self):
        super(FonceStrategy,self).__init__("Fonce")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)

class StaticStrategy(Strategy):
    def __init__(self):
        super(StaticStrategy,self).__init__("Static")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction()
#nosstrat
class StrategyAttaquant(Strategy):
    def __init__(self):
        super(StrategyAttaquant,self).__init__("Attaquant")
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        je=Je(mystate)
        stratje = StratJe(je, mystate)
        
        
        if mystate.my_position != mystate.ball_position() and not mystate.procheduballon(): 
            return je.aller(mystate.ball_position())
        else:
            return je.shoot1(mystate.ball_position().distance(mystate.pos_sonbut()),mystate.pos_sonbut()) 
            
class StrategyDefense(Strategy):
    def __init__(self):
        super(StrategyDefense,self).__init__("Defense")
        
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
        
class StrategyGoal(Strategy):
    def __init__(self):
        super(StrategyGoal,self).__init__("GoalKeeper")
        
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        je=Je(mystate)
        stratje = StratJe(je, mystate)
        
        if mystate.balldanscdg() and not mystate.procheduballon():
            return je.aller(mystate.ball_position())
        if mystate.procheduballon():
            return stratje.degagement()
        if not mystate.balldanscdg() and mystate.danslescages():
            return stratje.meposig() 

class StrategyAttaquantP(Strategy):
    def __init__(self):
        super(StrategyAttaquantP,self).__init__("Polposition")
    def compute_strategy(self,state,id_team,id_player):
        mystate=MyState(state,id_team,id_player)
        je=Je(mystate)
        stratje = StratJe(je, mystate)
        
        if not mystate.ennemiedanscdd:
            return stratje.meposia()
        else:
            return je.shoot1(mystate.ball_position().distance(mystate.pos_sonbut()),mystate.pos_sonbut()) 

#######
## Constructioon des equipes
#######

team1 = SoccerTeam("team1")
strat_j1 = KeyboardStrategy()
strat_j2 = KeyboardStrategy()
strat_j1.add('f',StaticStrategy())
strat_j1.add('d', StrategyDefense())
strat_j1.add('a', StrategyAttaquant())


strat_j2.add('l', StrategyGoal())
strat_j2.add('o', StrategyAttaquant())
strat_j2.add('i', StaticStrategy())

team1.add("Jexp 1",strat_j1)
team1.add("Jexp 2", strat_j2)
team2 = SoccerTeam("team2")
team2.add("rien 1", StrategyAttaquant())
team2.add("rien 2", StrategyDefense())


### Transformation d'un etat en features : state,idt,idp -> R^d
def my_get_features(state,idt,idp):
    """ extraction du vecteur de features d'un etat, ici distance a la balle, distance au but, distance balle but """
    mystate=MyState(state,idt,idp)
    p_pos= state.player_state(idt,idp).position
    f1 = state.ball.position.x
    f2 = state.ball.position.y
    """
     p_pos.distance( Vector2D((2-idt)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.))
    """
    f3 = mystate.ennemieleplusproche().x
    f4 = mystate.ennemieleplusproche().y
    f5 = p_pos.x
    f6 = p_pos.y
    return [f1,f2,f3,f4,f5,f6]


def entrainement(fn):
    simu = Simulation(team1,team2)
    show_simu(simu)
    # recuperation de tous les etats
    training_states = strat_j1.states
    training_states2 = strat_j2.states
    # sauvegarde dans un fichier
    dump_jsonz(training_states,fn)
    dump_jsonz(training_states2,fn)

def apprentissage(fn):
    ### chargement d'un fichier sauvegarder
    states_tuple = load_jsonz(fn)
    ## Apprentissage de l'arbre
    data_train, data_labels = build_apprentissage(states_tuple,my_get_features)
    dt = apprend_arbre(data_train,data_labels,depth=10)
    # Visualisation de l'arbre
    affiche_arbre(dt)
    genere_dot(dt,"test_arbre.dot")
    return dt

def jouer_arbre(dt):
    ####
    # Utilisation de l'arbre
    ###
    dic = {"Fonce":FonceStrategy(),"Static":StaticStrategy(),"Attaquant":StrategyAttaquant(), "Defense":StrategyDefense(), "GoalKeeper": StrategyGoal()
    , "Polposition": StrategyAttaquantP()}
    treeStrat1 = DTreeStrategy(dt,dic,my_get_features)
    treeStrat2 = DTreeStrategy(dt,dic,my_get_features)
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
    
    
