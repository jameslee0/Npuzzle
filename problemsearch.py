'''
problemsearch - Functions for seaarching.
'''

from collections import deque
from typing import Deque
from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.timer import Timer
from basicsearch_lib02.tileboard import TileBoard
from explored import Explored
    
"""graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored, elapsed_s) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    elapsed_s is the elapsed wall clock time performing the search
    """
       
def graph_search(problem, verbose=False, debug=False):
      #Set Timer
      timer = Timer()
      #I am creating a variable frontier as a PriorityQueue to store all the current states
      frontier = PriorityQueue()
      #I am creating a variable exploredStates a hashtable to store all explored states
      exploredStates = Explored()
      #This will initialize the frontier with the first Node
      frontier.append(Node(problem, problem.initial))

      
      #I am using a while loop in order for the code to keep running until a solution is found.
      while frontier.__len__() != 0:

            #This will pop a node from the frontier.
            node = frontier.pop()

            if debug:
                  print('The node that was just popped is: ', str(node))
            #print(node)
            #print(frontier.__len__())


            if problem.goal_test(node.state):
                  #Instantiate variables nodeSolvePath and actions to save our node.path() for printing and our actions for more information.
                  nodeSolvePath = node.path()
                  actions = node.solution()
                  
                  # If verbose is True, display all moves that happened.
                  if verbose:
                        #Formatted to print out how many moves it took, and which moves it took and the path that occurred.
                        print(f'Solution in {len(actions)} moves')
                        for i in range(len(actions)):
                              print(f'Move {i + 1} - {actions[i]}')
                              print(nodeSolvePath[i + 1].state, end='\n\n')

                  #The function will return a tuple containing a solution path, the amount of nodes explored, and the time is took in secs.
                  return nodeSolvePath, len(exploredStates.hash_map), timer.elapsed_s()

            else:
                  # Explore the children of current node that we are at.
                  for child in node.expand(problem):

                        child_tuple = child.state.state_tuple()

                        #If the child hasn't been explored yet, we will then load it into frontier and explore the set. 
                        if not exploredStates.exists(child_tuple):
                              exploredStates.add(child_tuple)
                              frontier.append(child)

      # If no solution found, return None
      return None