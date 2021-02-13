class Singleton:
   __instance__ = None

   def __init__(self):
       if Singleton.__instance__ is None:
           Singleton.__instance__ = self
       else:
           raise Exception( 'cant create new instance' )

   @staticmethod
   def get_instance(): # returns the instance of current class
       if not Singleton.__instance__:
           Singleton()
       return Singleton.__instance__

instance_one = Singleton.get_instance()
instance_two = Singleton.get_instance()
assert( instance_one == instance_two )
print( instance_one == instance_two )
