import sys, subprocess
import random
import time

def clear_screen():
    input('Press Enter to continues...')
    subprocess.run('clear', shell=True)
def counter_down(seconds):
    for i in range(seconds):
        time.sleep(1) 
        print('You have ' + str(10 - i) + ' seconds to change player!!')
def counter_to_shoot():
    for i in range(3):
        time.sleep(1)
        print('Misile launching in ' + str(3 - i) + ' seconds!!')
class BattleShip:

    def __init__(self, score = 0, player_id = ''):
        self.score = score
        self.player_id = player_id
        self.game = []
        self.game_visualization = []
        self.letters_to_numbers = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
        self.number_of_ships = 6
        self.added_ships = {6: True, 5: True, 4: True, 3: True}
        self.option_to_numbers = {1: 6, 2: 5, 3: 4, 4: 3}
        self.ship_figures = {6: '#', 5: '*', 4: '@', 3: '%'}
    
    def print_game(self):
        keys = list(self.letters_to_numbers.keys())
        print(' ' + str(keys))   
        for i in range(10):
                print(str(i + 1) + str(self.game[i]) + '\n')

    def print_game_visualization(self):
        keys = list(self.letters_to_numbers.keys())
        print(' ' + str(keys))   
        for i in range(10):
                print(str(i + 1) + str(self.game_visualization[i]) + '\n')

    def add_ships(self):
        completed = False
        counter_ship5 = 0
        counter_ship4 = 0
        print('{player_name} it\'s your turn!!\n'.format(player_name = self.player_id))
        while not completed:
            if counter_ship5 > 1 and ship_id == 5:
                self.added_ships[ship_id] = False
            if counter_ship4 > 1 and ship_id == 4:
                self.added_ships[ship_id] = False
            verification = True
            used_ships = True
            while used_ships:
                print('Pick a Ship!!\n')
                print('1) 6 Square Ship\nAvailability: ' + str(self.added_ships[6]) + '\n2) 5 Square Ship x 2\nAvailability: ' + str(self.added_ships[5]) + '\n3) 4 Square Ship x 2\nAvailability: ' + str(self.added_ships[4]) + '\n4) 3 Square Ship\nAvailability: ' + str(self.added_ships[3]))
                option_ships = int(input('Answer: '))
                ship_id = self.option_to_numbers[option_ships]
                if self.added_ships[ship_id] == False:
                    print('Ship already in use, try another option!!')
                    clear_screen()
                    used_ships = True
                else:
                    clear_screen()
                    used_ships = False
            self.print_game()
            print('Now, in what position you whant to add the ship??')
            print('1) Horizontal\n2) Vertical')
            horizontal_or_vertical = int(input('Answer: '))
            i = 0
            if horizontal_or_vertical == 1:
                print('In what number you whant your ship??')
                print('1 -- 10')
                y_position = int(input('Answer: ')) - 1
                print('Initial letter of the ship??')
                print('A -- J')
                x_initial_position = self.letters_to_numbers[input('Answer: ').upper()] - 1
                try:
                    for i in range(ship_id):
                        if self.game[y_position][x_initial_position + i] == " ":
                            self.game[y_position][x_initial_position + i] = self.ship_figures[ship_id]
                        else:
                            for z in range(x_initial_position + i - 1, x_initial_position, - 1):
                                self.game[y_position][z] = " "
                            print('There is another ship in that position!!!!')
                            print('Try again!!!')
                            verification = False
                            clear_screen()
                            break
                    if verification == True:
                        if ship_id != 4 and ship_id != 5:
                            self.added_ships[ship_id] = False
                        elif ship_id == 4:
                            counter_ship4 += 1
                        elif ship_id == 5:
                            counter_ship5 += 1
                        clear_screen()
                except IndexError:
                    print('Ship was too large, try again with other position')
                    for z in range(x_initial_position + i - 1, x_initial_position - 1, -1):
                        self.game[y_position][z] = " "
                    clear_screen()
            elif horizontal_or_vertical == 2:
                print('In what number you whant your ship??')
                print('1 -- 10')
                y_initial_position = int(input('Answer: ')) - 1
                print('Initial letter of the ship??')
                print('A -- J')
                x_position = self.letters_to_numbers[input('Answer: ').upper()] - 1
                try:
                    for i in range(ship_id):
                        if self.game[y_initial_position + i][x_position] == " ":
                            self.game[y_initial_position + i][x_position] = self.ship_figures[ship_id]
                        else:
                            for z in range(y_initial_position + i - 1, y_initial_position - 1, -1):
                                self.game[z][x_position] = " "
                            print('There is another ship in that position!!!!')
                            print('Try again!!!')
                            verification = False
                            clear_screen()
                            break
                    if verification == True:
                        if ship_id != 4 and ship_id != 5:
                            self.added_ships[ship_id] = False
                        elif ship_id == 4:
                            counter_ship4 += 1
                        elif ship_id == 5:
                            counter_ship5 += 1
                        clear_screen()
                except IndexError:
                    print('Ship was too large, try again with other position')
                    for z in range(y_initial_position + i - 1, y_initial_position - 1, -1):
                        self.game[z][x_position] = " "
                    clear_screen()
            else:
                print('Invalid Option')
                clear_screen()
            if True not in self.added_ships.values():
                completed = True

player1 = BattleShip()
player2 = BattleShip()
player1.player_id = 'PLAYER 1'
player2.player_id = 'PLAYER 2'

for i in range(10):
    player1.game.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    player1.game_visualization.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    player2.game.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    player2.game_visualization.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])

menu1 = True

while menu1:
    print('\nMain Menu\n\nPress\n\n1) Multiplayer Game\n2) Instructions\n3) Exit')
    option_menu = int(input('Answer: '))
    clear_screen()
    if option_menu == 1:
        print('Your are playing in 2 Player Mode!!')
        print('Now, it\'s time to add some ships to the battlefield!!')
        clear_screen()
        player1.add_ships()
        counter_down(10)
        player2.add_ships()
        print('Let\'s start war!!!')
        print('Let\'s decide who goes first')
        turn = random.randint(1, 2)
        turn_player1 = False
        turn_player2 = False
        if turn == 1:
            print([player1.player_id + ' goes first!!'])
            turn_player1 = True
        else:
            print([player2.player_id + ' goes first!!'])
            turn_player2 = True
        while player1.score < 27 and player2.score < 27:
            while turn_player1 == True and turn_player2 == False:
                print(player1.player_id)
                print('Here it is the map!!')
                player1.print_game_visualization()
                print('Let\'s set a target!!')
                print('Give me the coordinates to take a shot!!')
                x_coordinate = player1.letters_to_numbers[input('Give me a Letter\nA -- Z\nAnswer: ').upper()] - 1
                y_coordinate = int(input('Give me a Number\n1 -- 10\nAnswer: ')) - 1
                if player2.game[y_coordinate][x_coordinate] == " ":
                    counter_to_shoot()
                    print('We failed that shoot!!')
                    print('Good luck next time!!')
                    player1.game_visualization[y_coordinate][x_coordinate] = 'O'
                    player2.game[y_coordinate][x_coordinate] = 'O'
                    turn_player1 = False
                    turn_player2 = True
                elif player2.game[y_coordinate][x_coordinate] == 'X' or player2.game[y_coordinate][x_coordinate] == 'O':
                    print('You already took a shot to that spot!!')
                else:
                    player2.game[y_coordinate][x_coordinate] = 'X'
                    player1.game_visualization[y_coordinate][x_coordinate] = 'X'
                    counter_to_shoot()
                    print('Nice shot!!')
                    print('We hitted a target!!')
                    player1.score += 1
                    clear_screen()
                    counter_down(10)
                    turn_player1 = False
                    turn_player2 = True
            while turn_player1 == False and turn_player2 == True:
                print(player2.player_id)
                print('Here it is the map!!')
                player2.print_game_visualization()
                print('Let\'s set a target!!')
                print('Give me the coordinates to take a shot!!')
                x_coordinate = player2.letters_to_numbers[input('Give me a Letter\nA -- Z\nAnswer: ').upper()] - 1
                y_coordinate = int(input('Give me a Number\n1 -- 10\nAnswer: ')) - 1
                if player1.game[y_coordinate][x_coordinate] == " ":
                    counter_to_shoot()
                    print('We failed that shoot!!')
                    print('Good luck next time!!')
                    player2.game_visualization[y_coordinate][x_coordinate] = 'O'
                    player1.game[y_coordinate][x_coordinate] = 'O'
                    turn_player2 = False
                    turn_player1 = True
                elif player1.game[y_coordinate][x_coordinate] == 'X' or player1.game[y_coordinate][x_coordinate] == 'O':
                    print('You already took a shot to that spot!!')
                else:
                    player1.game[y_coordinate][x_coordinate] = 'X'
                    player2.game_visualization[y_coordinate][x_coordinate] = 'X'
                    counter_to_shoot()
                    print('Nice shot!!')
                    print('We hitted a target!!')
                    player2.score += 1
                    clear_screen()
                    counter_down(10)
                    turn_player2 = False
                    turn_player1 = True
        if player1.score >= 27:
            print(player1.player_id + " wins!!")
            menu1 = False
        else:
            print(player2.player_id + " wins!!")
            menu1 = False
    elif option_menu == 2:
        print("""
        The object of Battleship is to try and sink all of the other player's before they sink all of your ships. 
        All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  
        The other player also tries to hit your ships by calling out coordinates.  Neither you nor the other player can see the other's board so you must try to guess where they are.  
        Each board in the physical game has two grids:  the lower (horizontal) section for the player's ships and the upper part (vertical during play) for recording the player's guesses.
        """)
        print()
        clear_screen()
    else:
        menu1 = False
