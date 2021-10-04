"""
Class for maintaining explored sets
"""

class Explored(object):
    """
    Maintain an explored set.  Assumes that states are hashable
    (e.g. state is represented by a tuple)
    """

    def __init__(self):
        "__init__() - Create an empty explored set"
        
        self.hash_map = dict()


    def exists(self, state):
        """
        exists(state) - Has this state already been explored?

        :param state:  Hashable problem state
        :return: True if already seen, False otherwise
        """

        #We will try to check if it exists in the hash_map variable. If it exists, return True, and if not, return False.
        try:
            return state in self.hash_map[hash(state)]
        except KeyError:
            return False



    def add(self, state):
        """
        add(state) - Add a given state to the explored set

        :param state:  A problem state that is hashable, e.g. a tuple
        :return: None
        """

        #If the current check isn't already in the hash_map variable, it will add it into the hash_map variable.
        if hash(state) not in self.hash_map.keys():
            self.hash_map[hash(state)] = set()
        self.hash_map[hash(state)].add(state)
