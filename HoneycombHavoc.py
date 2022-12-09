import random
from random import sample


# CLASS - SLOT
#==========================================
class Slot:
    def __init__(self, position, name, is_toxic):
        self.position = position
        self.name = name
        self.is_toxic = is_toxic
        self.display_name = self.MakeDisplay()      # Returns [XX](fruit), [##](bees), [--](Empty)


    def MakeDisplay(self) -> str:
        match self.name:
            case "Fruit":
                return random.choice(['[AA]', '[BB]', '[CC]', '[DD]', '[EE]', '[FF]', '[GG]'])
            case "Beehive":
                return "[##]"
            case "Empty":
                return "[--]"


# CLASS - CONVEYOR  
#==========================================
class Conveyor:
    def __init__(self):
        self.number_of_slots = 50
        self.fruit_list = [0 for a in range(self.number_of_slots)]   # creates a list of empty items in preperation to build
        self.BuildConveyor()


    # Fill the Converyor List with Fruit Objects, and Insert Behives
    #==================================
    def BuildConveyor(self):

        # fill the conveyor with fruits and behives
        beehive_positions = []
        beehive_positions.append(random.randint(8, 15)) # Beehive 1
        beehive_positions.append(random.randint(19, 25)) # Beehive 2
        beehive_positions.append(random.randint(29, 35)) # Beehive 3
        beehive_positions.append(random.randint(39, 45)) # Beehive 4

        for each_element in range(self.number_of_slots):
            if each_element <= 8:
                self.fruit_list[each_element] = Slot(   position    =each_element,
                                                        name        ="Fruit",
                                                        is_toxic    =False)

            if each_element in beehive_positions:
                self.fruit_list[each_element] = Slot(   position    =each_element,
                                                        name        ="Beehive",
                                                        is_toxic    =True)               
            else:
                self.fruit_list[each_element] = Slot(   position    =each_element,
                                                        name        ="Fruit",
                                                        is_toxic    =False)


    # Remove Fruit from front of list, add empty object in the back
    #==================================
    def RemoveFromList(self, number_removed:int):
        b = len(self.fruit_list)
        for a in range(number_removed):

            # removes first element in list
            self.fruit_list.pop(0)                

            # puts a new element in the back of list, to keep len() the same
            self.fruit_list.insert(b, Slot( position    =b,
                                            name        ="Empty",
                                            is_toxic    =False)) 
   
    # Print Game Board
    #===============================
    def PrintGameBoard(self):
        game_board = (
        '                                                                    \n'
        '    {42:0}  {43:0}  {44:0}  {45:0}  {46:0}  {47:0}  {48:0}  {49:0}  \n'
        '    {41:0}                                                          \n'
        '    {40:0}                                                          \n'
        '    {39:0}  {38:0}  {37:0}  {36:0}  {35:0}  {34:0}  {33:0}  {32:0}  \n'
        '                                                            {31:0}  \n'
        '                                                            {30:0}  \n'
        '    {22:0}  {23:0}  {24:0}  {25:0}  {26:0}  {27:0}  {28:0}  {29:0}  \n'
        '    {21:0}                                                          \n'
        '    {20:0}                                                          \n'
        '    {19:0}  {18:0}  {17:0}  {16:0}  {15:0}  {14:0}  {13:0}  {12:0}  \n'
        '                                                            {11:0}  \n'
        '                                                            {10:0}  \n'
        '    {02:0}  {03:0}  {04:0}  {05:0}  {06:0}  {07:0}  {08:0}  {09:0}  \n'
        '    {01:0}                                                          \n'
        '    {00:0}                                                          \n'
        ).format(*[a.display_name for a in self.fruit_list])
        print(game_board)



#CLASS - PLAYER
#==========================================
class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.display = self.MakeDisplay()

    def MakeDisplay(self):
        string = (
        '              \n'
        '  ==========  \n'
        '  │ PLAYER │  \n'
        '  │   {}   │  \n'
        '  ==========  \n'
        '              \n'
        ).format(
            format(self.player_number, ' <2')
        ).splitlines()
        return string


# CLASS - GAME
#==========================================
class Game:
    def __init__(self):
        self.is_game_ongoing = True
        self.player_list = []
        self.Conveyor = Conveyor()
        self.BuildPlayerList()

    # Create 4 players and re-arrange them
    #==================================
    def BuildPlayerList(self):
        self.player_list.append(Player(1))
        self.player_list.append(Player(2))
        self.player_list.append(Player(3))
        self.player_list.append(Player(4))

        # randomise order of players
        random.shuffle(self.player_list)

    # Print Players
    #===============================
    def PrintPlayerList(self):
        new_map = map(lambda x: x.display, NewGame.player_list)
        for lines in zip(*new_map):
            print(*lines)

    # Remove player in front from game
    #==================================
    def EliminatePlayer(self):
        self.player_list.pop(0)

    # Move front player to the back
    #==================================
    def RotatePlayers(self):
        self.player_list = self.player_list[1:len(self.player_list)] + list(self.player_list[0:1])

    # Return a list of fruit objects based on user request
    #==================================
    def GetFruitsRequested(self, num:int) -> list:
        return list(self.Conveyor.fruit_list[0:num])

    # Get a list of True/False. Do any contain "True"?
    #==================================
    def DidPlayerGetToxic(self, fruits_requested) -> bool:
        return any(a.is_toxic == True for a in fruits_requested)


    # Restrict to only 1 or 2 items
    #==================================
    def RestrictUserInput(self, user_can_only_type, input_message):
        list_upper_case = [each_string.upper() for each_string in user_can_only_type]
        while True:
            try:
                user_input = input(input_message + ": ")
                if str(user_input).upper() in list_upper_case:
                    return user_input
                raise ValueError()
            except ValueError:
                print("    Error: You are required to enter one of the following: {}".format(user_can_only_type))
                print("    Please try again\n")



    # Elimination Message
    #==================================
    def PlayerEliminatedMessage(self, player_eliminated):
         player_eliminated_message = (
        '                               \n'            
        '                               \n'
        '  ################             \n'
        '  │   PLAYER {}  │             \n'
        '  │ GOT BEHIVED! │             \n'
        '  ################             \n'
        '                               \n'         
        '  input any key to continue... \n'       
         ).format(
            format(player_eliminated.player_number, ' <2')
        )

         input(player_eliminated_message)


    # End Game
    #==================================
    def EndGame(self, winning_player):
        self.is_game_ongoing = False
        game_finish_message = (
        '                     \n'            
        '                     \n'
        '  =================  \n'
        '  │  GAME FINISH  │  \n'
        '  │ PLAYER {} WON │  \n'
        '  =================  \n'
        '                     \n'
         ).format(
            format(winning_player.player_number, ' <2')
        )

        input(game_finish_message)



# MAIN CODE
#==========================================
NewGame = Game()
while NewGame.is_game_ongoing == True:

    NewGame.Conveyor.PrintGameBoard()
    NewGame.PrintPlayerList()

    # first in line is current player
    current_player = NewGame.player_list[0]

    # ask current player how many fruits/slots they want to remove
    user_inputted_int = int(NewGame.RestrictUserInput(
                                ["1","2"],
                                'Player {0} - How many fruits? '.format(current_player.player_number)))


    # remove the fruits/behives from the converyor and store in player_fruits
    player_fruits = NewGame.GetFruitsRequested(user_inputted_int)
    NewGame.Conveyor.RemoveFromList(user_inputted_int)    

    # if any of the fruits (Behives) have attribute "isToxic" as True, eliminate the player. If not, put them to back of queue
    if NewGame.DidPlayerGetToxic(player_fruits) == True:
        NewGame.PlayerEliminatedMessage(current_player)
        NewGame.EliminatePlayer()
    else:
        NewGame.RotatePlayers()

    # check to see if game ended. Game ends when one player remains
    if len(NewGame.player_list) == 1:
        NewGame.EndGame(NewGame.player_list[0])

