'''
driver for graph search problem

I promise that the attached assignment is my own work. I recognize that should this not be the case, 
I will be subject to penalties as outlined in the course syllabus. James Lee
'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.timer import Timer
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections


def driver():
    timer = Timer()
    # result dictionary will contain the result for all strategies
    tableData = {'BreadthFirstSearch': {'PlanLen': [], '# of Nodes': [], 'Elapsed Time': []},
               'DepthFirstSearch': {'PlanLen': [], '# of Nodes': [], 'Elapsed Time': []},
               'Manhattan': {'PlanLen': [], '# of Nodes': [], 'Elapsed Time': []}}

    #This is where i linked the class methods from searchStrategies for each search algorithm
    algoType = {'BreadthFirstSearch': BreadthFirst, 'DepthFirstSearch': DepthFirst, 'Manhattan': Manhattan}

    #This for loop essentially creates a certain amount of Puzzle cases (In this case, 31 puzzles).
    for puzzleNum in range(31):

        #This for loop will create our 3 by 3 tile and then print out styling code that I put in.
        for i in range(3, 4):
            problem = NPuzzle(i * i - 1)
            print('_______________________________\n')
            #Print out the problem number for easy use and interaction
            print(f'       Problem Number {puzzleNum + 1}')
            #Printing the Initial/Starting state 
            print('Starting(Initial) State\n', problem.initial)
            #Printing the goal state. I can't seem to ever get anything inside this so I'm not sure if this is an error.
            print('Goal States', problem.goals)
            print('_______________________________\n')

            #In the case of this for loop, it will be testing each search algorithm in the algorithm list I made named algoType.
            for searchAlgo in algoType:
                #I have assigned the g and h methods to the one that it is currently using for a specific algorithm.
                problem.g = algoType[searchAlgo].g
                problem.h = algoType[searchAlgo].h

                #Tester Print Statements.
                #print(problem.g)
                #print(problem.h)
                #print(algoType[searchAlgo].g)
                #print(algoType[searchAlgo].g)

                #So we will be using graph_search to start the search based on the current algorithm type we are using. 
                moves, exploredNodes, time = graph_search(problem, verbose=False) #Set this verbose value to True if you want to see each step.

                #In here we are just inputting in our data that we are collecting while the search algorithm was running and place them in the correct place.
                tableData[searchAlgo]['PlanLen'].append(len(moves))
                tableData[searchAlgo]['# of Nodes'].append(exploredNodes)
                tableData[searchAlgo]['Elapsed Time'].append(time)

                #These 2 print statements are mainly to give an easier time to grade. Can take out if not needed.
                print(f'Finished {searchAlgo}...')
            print(f'Finished Problem {puzzleNum + 1}!')

    #This shows total time that it took for all trials to run, then goes on to print each statements data.
    print(f'\nTotal time to run all trials: {timer.elapsed()}\n')
    print('\n~~~~~~~~~~~~~~~~~~~Specific Algo Table Data~~~~~~~~~~~~~~~~~~~~~\n')

    #This for loop will loop through each data value type for each search algorithm and display the values that are in there accordingly.
    for searchAlg in tableData:
        items = tableData[searchAlg]
        print(f'        {searchAlg} Data Table \n')
        for item_searchAlgo in items:
            print(f'{item_searchAlgo}: ')
            print(f'    -Mean: {mean(items[item_searchAlgo])}')
            print(f'    -STDev: {stdev(items[item_searchAlgo])}')
        print('____________________________________________________')



# To do:  Run driver() if this is the entry module
if __name__ == "__main__":
    driver()