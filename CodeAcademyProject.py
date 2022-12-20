import sys, subprocess
import random

def clear_screen():
    input('Press Enter to continues...')
    subprocess.run('clear', shell=True)

class BattleShip:

    game = []
    letters_to_numbers = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
    number_of_ships = 6
    added_ships = {6: True, 5: True, 4: True, 3: True}
    option_to_numbers = {1: 6, 2: 5, 3: 4, 4: 3}

    def __init__(self, score = 0, turn = False, kills = 0, last_hit = False):
        self.score = score
        self.turn = turn 
        self.kills = kills
        self.last_hit = last_hit
    
    def print_game(self):
        keys = list(self.letters_to_numbers.keys())
        print(' ' + str(keys))   
        for i in range(10):
                print(str(i + 1) + str(self.game[i]) + '\n')

    def add_ships(self):
        completed = False
        counter_ship5 = 0
        counter_ship4 = 0
        while not completed:
            used_ships = True
            while used_ships:
                print('Pick a Ship!!')
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
                print('1 - 10')
                y_position = int(input('Answer: ')) - 1
                print('Initial letter of the ship??')
                x_initial_position = self.letters_to_numbers[input('Answer: ').upper()] - 1
                try:
                    for i in range(ship_id):
                        if self.game[y_position][x_initial_position + i] == " ":
                            self.game[y_position][x_initial_position + i] = '#'
                        else:
                            for z in range(x_initial_position + i - 1, x_initial_position, -1):
                                self.game[y_position][z] = " "
                            print('There is another ship in that position!!!!')
                            print('Try again!!!')
                            clear_screen()
                            break
                    if ship_id != 4 and ship_id != 5:
                        self.added_ships[ship_id] = False
                    elif ship_id == 4:
                        if counter_ship4 >= 1:
                            self.added_ships[ship_id] = False
                        else:
                            counter_ship4 += 1
                    elif ship_id == 5:
                        if counter_ship5 >= 1:
                            self.added_ships[ship_id] = False
                        else:
                            counter_ship5 += 1
                    clear_screen()
                except IndexError:
                    print('Ship was too large, try again with other position')
                    for z in range(x_initial_position + i - 1, x_initial_position - 1, -1):
                        self.game[y_position][z] = " "
                    clear_screen()
            elif horizontal_or_vertical == 2:
                print('In what letter you want your ship??')
                x_position = self.letters_to_numbers[input('Answer: ').upper()] - 1
                print('Initial position of the ship??')
                y_initial_position = int(input('Answer: ')) - 1
                try:
                    for i in range(ship_id):
                        if self.game[y_initial_position + i][x_position] == " ":
                            self.game[y_initial_position + i][x_position] = "#"
                        else:
                            for z in range(y_initial_position + i - 1, y_initial_position - 1, -1):
                                self.game[z][x_position] = " "
                            print('There is another ship in that position!!!!')
                            print('Try again!!!')
                            clear_screen()
                            break
                    if ship_id != 4 and ship_id != 5:
                        self.added_ships[ship_id] = False
                    elif ship_id == 4:
                        if counter_ship4 > 1:
                            self.added_ships[ship_id] = False
                        else:
                            counter_ship4 += 1
                    elif ship_id == 5:
                        if counter_ship5 > 1:
                            self.added_ships[ship_id] = False
                        else:
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

for i in range(10):
    player1.game.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    player2.game.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])

menu1 = True

while menu1:
    print('Main Menu\n\nPress\n\n1) Start Game\n2) More About\n3) Exit')

    option_menu = int(input('Answer: '))

    if option_menu == 1:
            clear_screen()
            keys = list(BattleShip.letters_to_numbers.keys())
            print(' ' + str(keys))              
            for i in range(10):
                print(str(i + 1) + str(BattleShip.game[1]) + '\n')
            print('Now, it\'s time to add some ships to the battlefield!!')
            print()
            print('First, Player 1!!')
            player1.add_ships()
            player1.print_game()
            print('Now Player2!!')
            player2.add_ships()
            player2.print_game()
    elif option_menu == 2:
        clear_screen()
        print('Somenthing 2.....')

    else:
        menu1 = False
