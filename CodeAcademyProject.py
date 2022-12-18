import os
import random

class BattleShip:
    
    def __init__(self, score = 0, turn = False, kills = 0, last_hit = False):
        self.score = score
        self.turn = turn 
        self.kills = kills
        self.last_hit = last_hit
    

player1 = BattleShip()
player2 = BattleShip()

menu1 = True

while menu1:
    print('Main Menu\n Press\n1) Start Game\n2) More About\n3) Exit')
    option_menu = int(input())
    if option_menu == 1:
        print('Something...')
    elif option_menu == 2:
        print('Somenthing 2.....')
    else:
        menu1 = False
