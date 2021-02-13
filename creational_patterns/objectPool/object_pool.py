class BattleRoyale: # singleton class
   __instance__ = None

   def __init__(self):
       if BattleRoyale.__instance__ is None:
           BattleRoyale.__instance__ = self
       else:
           raise Exception( 'cant create new Battle Royale instance' )

   @staticmethod
   def get_instance(): # returns the instance of current class
       if not BattleRoyale.__instance__:
           BattleRoyale()
       return BattleRoyale.__instance__

class BattleRoyaleObjectPool: # object pool class

    def __init__(self, size):
        self.battleRoyaleObjectPool = [BattleRoyale.get_instance() for _ in range(size)]

    def acquire(self):
        if self.battleRoyaleObjectPool:
            return self.battleRoyaleObjectPool.pop()
        else:
            self.battleRoyaleObjectPool.append(BattleRoyale.get_instance())
            return self.battleRoyaleObjectPool.pop()

    def release(self, player):
        player.setting = 0 # instance setting property
        self.battleRoyaleObjectPool.append(player)

class Player:
    gameRoom = None
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return str({'id' : self.id,
                    'name' : self.name,
                    'game room' : self.gameRoom })


'''get 100 instance of single Battle Royale game in our BattleRoyaleObjectPool'''
playerLimit = 100
battleRoyaleObjectPool = BattleRoyaleObjectPool(playerLimit)
for battleRoyaleInstance in battleRoyaleObjectPool.battleRoyaleObjectPool:
    print(battleRoyaleInstance)
''' give one of the 100 single Battle Royale game instance to playerOne '''
playerOne = Player(id = 1, name = 'playerOne')
playerOne.gameRoom = battleRoyaleObjectPool.acquire()
print(playerOne)
''' when the player exits the game, release the instance back to game room
 (object pool) '''
battleRoyaleObjectPool.release(playerOne.gameRoom)
