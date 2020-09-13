# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST

    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    from util import Stack,Counter

    explored = Counter() # Explored States of the Pacman graph
    frontier = Stack()
    # Store current position / state and previous actions
    # Start State is in Explored Set by default.
    frontier.push([problem.getStartState(),[]])
    while not frontier.isEmpty():
        # represents current state of agent
        state, actions = frontier.pop()
        if problem.isGoalState(state):
            return actions
        if not explored[state]:
            # When a element is popped from the frontier, it is known to be first explored
            explored[state] = 1
            for nxt_state, action, _ in problem.getSuccessors(state):
                # Prune new states that have already been explored
                if explored[nxt_state] != 0:
                    continue
                else:
                    frontier.push([nxt_state, actions + [action]])

    # If problem is known to be unsolvable return a empty action set.
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue, Counter
    explored = Counter() # Explored States of the Pacman graph
    frontier = Queue()
    # Store current position and state and previous actions
    # Start State is in Explored Set by default.
    frontier.push([problem.getStartState(),[]])
    while not frontier.isEmpty():
        # represents current state of agent
        state, actions = frontier.pop()
        if explored[state] == 1:
            continue
        if problem.isGoalState(state):
            return actions
        # When an element is popped from the stack, it is known to be first explored
        explored[state] = 1
        for nxt_state, action, _ in problem.getSuccessors(state):
            # Prune new states that have already been explored
            if explored[nxt_state] == 1: #if nxt_state in explored:
                continue
            else:
                frontier.push([nxt_state, actions + [action]])

    # If problem is known to be unsolvable return a empty action set.
    return []

def uniformCostSearch(problem):
    '''
    # Hui Ling's solution: not currently working
    from util import PriorityQueue

    explored = set() # Explored States of the Pacman graph
    frontier = PriorityQueue()

    startState = problem.getStartState()
    # Dictionary for storing g hat u of each state, i.e. min path cost of reaching u found so far
    minPathCosts = {startState: 0}
    # Dictionary for storing actions corresponding to each state
    actionsDict = {startState: []}
    # Frontier is a priority queue sorted by minPathCost
    frontier.push(startState, 0)

    while not frontier.isEmpty():
        # represents current state of agent
        state = frontier.pop()
        if problem.isGoalState(state):
            return actionsDict[state]
        # When an element is popped from the stack, it is known to be first explored
        explored.add(state)
        for nxt_state, action, cost in problem.getSuccessors(state):
            # Prune new states that have already been explored
            if nxt_state in explored:
                continue
            else:
                if nxt_state in minPathCosts:
                    gHatV = minPathCosts[nxt_state] 
                    gHatV = min(gHatV, minPathCosts[state] + cost)
                    frontier.update(nxt_state, gHatV)
                    actionsDict[nxt_state] = actionsDict[state] + [action]
                else:
                    gHatV = minPathCosts[state] + cost
                    minPathCosts[nxt_state] = gHatV
                    frontier.push(nxt_state, gHatV)
                    actionsDict[nxt_state] = actionsDict[state] + [action]
                    
    # If problem is known to be unsolvable return a empty action set.
    return []
    '''

    # Search the node of least total cost first.
    from util import PriorityQueue,Counter
    # Keys: Explored States of the Pacman graph, Values: Minimum Cost of the State path
    explored = Counter()
    # X: Node, Y: Current Path Cost -- Not Necessary
    # relaxation = lambda x, y: explored[x]
    priorityQueue = PriorityQueue()
    # Store current position and state and previous actions
    # Start State is in Explored Set by default.
    # Data Structure List Stores: Curr node, Predecessors, Cost to reach node
    startNode = problem.getStartState()
    priorityQueue.push([startNode, [], 0],0)
    while not priorityQueue.isEmpty():
        # represents current state of agent
        state, actions, cost = priorityQueue.pop()
        if problem.isGoalState(state):
            return actions
        # When a element is poped from the Priority Queue,
        # it is known to be of true cost from source to the node
        if not explored[state]:
            # + 1 as the cost is said to be 0 for initial which causes implementation issues
            explored[state] = cost + 1
            for nxt_state, action, nextCost in problem.getSuccessors(state):
                # Prune new states that have already been known to have SP
                if not explored[nxt_state]:
                    priorityQueue.update([nxt_state, actions + [action],
                                          cost+nextCost], cost+nextCost)

    # If problem is known to be unsolvable return a empty action set.
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0 

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue,Counter
    # print("Type of problem", problem)
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # [((5, 4), 'South', 1), ((4, 5), 'West', 1)] for initial state.
    # Keys: Explored States of the Pacman graph, Values: Minimum Cost of the State path
    explored = Counter()
    # X: Node, Y: Current Path Cost -- Not Necessary
    # lambda to calculate estimated Global Cost of A*
    estGlobalCost = lambda state, c : c + heuristic(state,problem)
    priorityQueue = PriorityQueue()
    # Store current position and state and previous actions
    # Start State is in Explored Set by default.
    # Data Structure List Stores: Curr node, Predecessors, Cost to reach node
    priorityQueue.push([problem.getStartState(), [], 0], 0)
    while not priorityQueue.isEmpty():
        # represents current state of agent
        state, actions, cost = priorityQueue.pop()

        if problem.isGoalState(state):
            return actions
        # When a element is poped from the Priority Queue,
        # it is known to be of true cost from source to the node
        if not explored[state]:
            # + 1 as the cost is said to be 0 for initial which causes implementation issues
            explored[state] = cost + 1
            for nxt_state, action, nextCost in problem.getSuccessors(state):
                # Prune new states that have already been known to have SP
                if not explored[nxt_state]:
                    priorityQueue.update([nxt_state, actions + [action],cost + nextCost],
                                         estGlobalCost(nxt_state,cost + nextCost))
    # If problem is known to be unsolvable return a empty action set.
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
