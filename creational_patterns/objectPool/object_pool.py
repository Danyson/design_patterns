from abc import ABC, abstractmethod

''' abstract game class '''
class Game(ABC):
    @abstractmethod
    def get_name(self): # name getter method
        pass

''' abstract instance holder class '''
class InstanceHolder(ABC):
    @abstractmethod
    def get_instance(self): # instance getter method
        pass

''' abstract object pool class '''
class ObjectPool(ABC):
    @abstractmethod
    def acquire(self): # acquires an object from pool
        pass
    @abstractmethod
    def release(self, player): # releases an object back to pool
        pass


class Player:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__teamId = None
        self.__gameName = None
        self.__gameRoom = None
    def setter(self, teamId, game):
        if(teamId!=None):
            self.__teamId = teamId
            self.__gameName = game.get_name()
            self.__gameRoom = game
        else:
            self.__teamId = teamId
            self.__gameName = None
            self.__gameRoom = None
    def getter(self, choice):
        if(choice == 'id'):
            return self.__id
        if(choice == 'name'):
            return self.__name
        if(choice == 'teamId'):
            return self.__teamId
        if(choice == 'gameName'):
            return self.__gameName
        if(choice == 'gameRoom'):
            return self.__gameRoom

    def __repr__(self):
        return str({'id' : self.__id,
                    'name' : self.__name,
                    'game name' : self.__gameName,
                    'team id' : self.__teamId,
                    'game room' : self.__gameRoom })

class BattleRoyale(Game):
    def __init__(self, gameName):
        self.__gameName = gameName
    def get_name(self):
        return self.__gameName

class GameInstanceHolder(InstanceHolder):
    def __init__(self, gameInstance):
        self.__instance = gameInstance
    def get_instance(self):
        return self.__instance

class BattleRoyaleObjectPool(ObjectPool): # object pool class

    def __init__(self, size, game):
        self.battleRoyaleObjectPool = [game.get_instance() for _ in range(size)]

    def acquire(self):
        if self.battleRoyaleObjectPool:
            return self.battleRoyaleObjectPool.pop()
        else:
            self.battleRoyaleObjectPool.append(game.get_instance())
            return self.battleRoyaleObjectPool.pop()

    def release(self, player):
        self.battleRoyaleObjectPool.append(player.getter(choice='gameRoom'))
        player.setter( teamId = None, game = player )

def test_no_of_instance(battleRoyaleObjectPool):
    return battleRoyaleObjectPool.count(battleRoyaleObjectPool[0])




''' create new battle royale game '''
battleRoyalegameOne = GameInstanceHolder(BattleRoyale(gameName = 'game one'))
playerLimit = 100

'''get 100 instance of battleRoyalegameOne in our
   BattleRoyaleObjectPool'''
battleRoyaleObjectPoolOne = BattleRoyaleObjectPool(playerLimit,
                                                   battleRoyalegameOne)

''' create playerOne & give one of the 100 battleRoyalegameOne
    instance to playerOne'''
print(f'''when object pool is created there are {test_no_of_instance(battleRoyaleObjectPoolOne.battleRoyaleObjectPool)} instances of battle Royale game One''')
print()
playerOne = Player(id = 1, name = 'playerOne')
playerOne.setter(teamId = 1, game = battleRoyaleObjectPoolOne.acquire())
print(playerOne)
print()
''' checking if playerOne game instance and
    object pool instances of battleRoyalegameOne are same '''
assert(playerOne.gameRoom == gameInstance
       for gameInstance in battleRoyaleObjectPoolOne.battleRoyaleObjectPool)
print(f'''when one object from object pool is given to player one there are {test_no_of_instance(battleRoyaleObjectPoolOne.battleRoyaleObjectPool)} instances of battle Royale game One in object pool''')
print()
''' create playerTwo &  give one of the 100 battleRoyalegameOne
    instance to playerTwo '''
playerTwo = Player(id = 2, name = 'playerTwo')
playerTwo.setter(teamId = 1, game = battleRoyaleObjectPoolOne.acquire())
print(playerTwo)
print()
print(f'''when another one object from object pool is given to player two there are {test_no_of_instance(battleRoyaleObjectPoolOne.battleRoyaleObjectPool)} instances of battle Royale game One in object pool''')
print()
''' when the playerOne exits the game, release the instance back to game room
 (object pool) '''
battleRoyaleObjectPoolOne.release(playerOne)

''' checking if playerTwo game instance and
    object pool instances of battleRoyalegameOne are same '''
assert(playerTwo.gameRoom == gameInstance
       for gameInstance in battleRoyaleObjectPoolOne.battleRoyaleObjectPool)
print(f'''when one object is released from player one to object pool there are {test_no_of_instance(battleRoyaleObjectPoolOne.battleRoyaleObjectPool)} instances of battle Royale game One in object pool''')
print()
''' when the playerTwo exits the game, release the instance back to game room
 (object pool) '''
battleRoyaleObjectPoolOne.release(playerTwo)
print(f'''when another one object released from player two to object pool there are {test_no_of_instance(battleRoyaleObjectPoolOne.battleRoyaleObjectPool)} instances of battle Royale game One in object pool''')
print()
print(playerOne)
print()
print(playerTwo)
