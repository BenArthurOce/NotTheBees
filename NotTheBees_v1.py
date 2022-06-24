import random

# CLASS - FRUIT
#==========================================
class Fruit:
    def __init__(self):
        self.display = self._makeDisplay()      # Randomises a letter. Used when printed to terminal
        self.isToxic = False                    # Won't eliminate player if obtained

    def _makeDisplay(self) -> str:
        option_list = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG']
        return str(random.sample(option_list, 1))


# CLASS - BEHIVE
#==========================================
class Beehive:
    def __init__(self):
        self.display = self._makeDisplay()      # Stores a "#". Used when printed to terminal
        self.isToxic = True                     # Will eliminate a player if obtained

    def _makeDisplay(self) -> str:
        option_list = ['##']
        return str(random.sample(option_list, 1))


#CLASS - EMPTY
#==========================================
class Empty:
    def __init__(self):
        self.display = self._makeDisplay()
        self.isToxic = False

    def _makeDisplay(self) -> str:
        option_list = ['--']
        return str(random.sample(option_list, 1))


#CLASS - PLAYER
#==========================================
class Player:
    def __init__(self, playerNumber):
        self.num = playerNumber
        self.inGame = True
        self.display = self._makeDisplay()


    def _makeDisplay(self):
        string = (
        '              \n'
        '  ==========  \n'
        '  │ PLAYER │  \n'
        '  │   {}   │  \n'
        '  ==========  \n'
        '              \n'
        ).format(
            format(self.num, ' <2')
        ).splitlines()
        return string



# CLASS - GAME
#==========================================
class Game:
    def __init__(self):
        self. numItems = 50
        self.players = []
        self.conveyor = [0 for a in range(self.numItems)]   # creates a list of empty items in preperation to build
        self._buildPlayers()
        self._buildConveyor()


    # Create 4 players and re-arrange them
    #==================================
    def _buildPlayers(self):
        self.players.append(Player(1))
        self.players.append(Player(2))
        self.players.append(Player(3))
        self.players.append(Player(4))

        # randomise order of players
        random.shuffle(self.players)


    # Fill the Converyor List with Fruit Objects, and Insert Behives
    #==================================
    def _buildConveyor(self):

        # fill the conveyor with fruit
        for each_element in range(self.numItems):
            self.conveyor[each_element] = Fruit()

        # for the moment, put a beehive in 10th, 20th, 30th, 40th position
        self.conveyor.insert(10,Beehive())
        self.conveyor.insert(20,Beehive())
        self.conveyor.insert(30,Beehive())
        self.conveyor.insert(40,Beehive())


    # Get list of Fruit Names in the converyor
    #==================================
    def _getFruitNames(self) -> list():
        return [a.display for a in self.conveyor]


    # Remove Fruit from front of list, add empty object in the back
    #==================================
    def _removeFromList(self, num:int):
        b = len(self.conveyor)                  # items in list
        for a in range(num):
            self.conveyor.pop(0)                # removes first element in list
            self.conveyor.insert(b, Empty())    # puts a new element in the back of list, to keep len() the same


    # Print Game Board
    #===============================
    def _printGameBoard(self):
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
        ).format(*self._getFruitNames())
        print(game_board)


    # Print Players
    #===============================
    def _printPlayerList(self):
        new_map = map(lambda x: x.display, MainGame.players)
        for lines in zip(*new_map):
            print(*lines)


    # Remove player in front from game
    #==================================
    def _eleminatePlayer(self):
        self.players.pop(0)

    # Move front player to the back
    #==================================
    def _rotatePlayers(self):
        self.players = self.players[1:len(self.players)] + list(self.players[0:1])

    # Return a list of fruit objects based on user request
    #==================================
    def _getFruitsRequested(self, num:int) -> list:
        return list(self.conveyor[0:num])

    # Get a list of True/False. Do any contain "True"?
    #==================================
    def _didPlayerGetToxic(self, fruits_requested:int) -> bool:
        return any(a.isToxic == True for a in fruits_requested)



MainGame = Game()



while True:

    # print game board
    MainGame._printGameBoard()
    MainGame._printPlayerList()

    # ask for player input and prepare as an int
    display_string = 'Player {0} - How many fruits? '.format(MainGame.players[0].num)
    user_inputted = input(display_string)
    user_inputted = int(user_inputted)

    # remove the fruits/behives from the converyor and store in player_fruits
    player_fruits = MainGame._getFruitsRequested(user_inputted)
    MainGame._removeFromList(user_inputted)

    # if any of the fruits (Behives) have attribute "isToxic" as True, eliminate the player
    if  MainGame._didPlayerGetToxic(player_fruits) == True:
        MainGame._eleminatePlayer()
    else:
        # if the player got no behives, put them to the back of the queue
        MainGame._rotatePlayers()








