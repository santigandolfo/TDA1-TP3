from commands.city import City
from commands.metropolis import Metropolis
from commands.general_commands import get_metropolis

def fifty_rounds_winner(round, harvest1, harvest2, imperium1, imperium2, routes):
    winner = None
    if round < 50:
        return winner
    else:
        if harvest1>harvest2:
            winner = 1
        elif harvest2>harvest1:
            winner = 2
        else:
            if len(imperium1)>len(imperium2):
                winner = 1
            elif len(imperium2)>len(imperium2):
                winner = 2
            else:
                if sum(imperium1.values())>sum(imperium2.values()):
                    winner = 1
                elif sum(imperium2.values())>sum(imperium1.values()):
                    winner = 2
    return winner


def metropolis_is_disconnected(metropoles, routes, imperium, player):
    metropolis = get_metropolis(metropoles, player)
    for origin, destinations in routes.items():
        if origin in imperium and metropolis in destinations:
                return False
    return True

def disconection_winner(metropoles, routes, imperium1, imperium2):
    winner = None
    if metropolis_is_disconnected(metropoles, routes, imperium1, 1):
        winner = 2
    elif metropolis_is_disconnected(metropoles, routes, imperium2, 2):
        winner = 1
    return winner

def harvest_winner(harvest1, harvest2):
    winner = None
    if harvest1 >= 100 or harvest2>= 100:
        if harvest1>harvest2:
            winner = 1
        else:
            winner = 2
    return winner

def winner(round, metropoles, routes, imperium1, harvest1, imperium2, harvest2):
        winner = None
        game_harvest_winner = harvest_winner(harvest1, harvest2)
        if game_harvest_winner:
            winner = game_harvest_winner
        else:
            game_disconection_winner = disconection_winner(metropoles, routes, imperium1, imperium2)
            if game_disconection_winner:
                winner = game_disconection_winner
            else:
                winner = fifty_rounds_winner(round, harvest1, harvest2, imperium1, imperium2, routes)
        return winner
