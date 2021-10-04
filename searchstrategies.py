"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

This module contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles with a single solution
    where the blank is in the center, e.g.:
        123
        4 5
        678
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    searchnode. 
"""

import math
from basicsearch_lib02.searchrep import Node
from basicsearch_lib02.tileboard import TileBoard

class BreadthFirst:
    "BreadthFirst - breadth first search"
    k = 0
    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial searchnode to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return parentnode.depth + 1
    
    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        return 0


class DepthFirst:
    "BreadthFirst - breadth first search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        k = 0
        """"g - cost from initial searchnode to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return 0
    
    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        return searchnode.depth * -1

class Manhattan:
    "BreadthFirst - breadth first search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial searchnode to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return parentnode.depth + 1
    
    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        value = 0
        #These 2 for loops are looping through each row and column to find the displacement of the board.
        for row in range(searchnode.state.boardsize):
            for col in range(searchnode.state.boardsize):
                #If the current placement on the board has a value and isn't none, run the following code.
                if searchnode.state.board[row][col] is not None:
                    
                    current = searchnode.state.board[row][col]
                    currentValue = current - 1
                    
                    expectedColumn = currentValue % searchnode.state.boardsize
                    expectedRow = currentValue // searchnode.state.boardsize

                    displacementColumn = abs(col - expectedColumn)
                    displacementRow = abs(row - expectedRow)

                    #Add both displacements from the Column and Row to value to get h.
                    value = value + displacementColumn + displacementRow
        #return the value
        return value