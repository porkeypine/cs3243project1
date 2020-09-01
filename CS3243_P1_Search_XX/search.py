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
    from util import Stack
    print("Type of problem", problem)
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # [((5, 4), 'South', 1), ((4, 5), 'West', 1)] for initial state.

    # Perform DFS in a iterative process
    # Explored set of values

    explored = set() # Explored States of the Pacman graph
    stack = Stack()
    # Store current position and state and previous actions
    # Start State is in Explored Set by default.
    stack.push([problem.getStartState(),[]])
    while not stack.isEmpty():
        # represents current state of agent
        state, actions = stack.pop()

        if problem.isGoalState(state):
            return actions
        # When a element is poped from the stack, it is known to be first explored
        explored.add(state)
        for nxt_state, action, _ in problem.getSuccessors(state):
            # Prune new states that have already been explored
            if nxt_state in explored:
                continue
            elif problem.isGoalState(nxt_state):
                return actions + [action]
            else:
                stack.push([nxt_state, actions + [action]])

    # If problem is known to be unsolvable return a empty action set.
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    print("Type of problem", problem)
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # [((5, 4), 'South', 1), ((4, 5), 'West', 1)] for initial state.

    # Perform DFS in a iterative process
    # Explored set of values

    explored = set() # Explored States of the Pacman graph
    queue = Queue()
    # Store current position and state and previous actions
    # Start State is in Explored Set by default.
    queue.push([problem.getStartState(),[]])
    while not queue.isEmpty():
        # represents current state of agent
        state, actions = queue.pop()

        if problem.isGoalState(state):
            return actions
        # When a element is poped from the stack, it is known to be first explored
        explored.add(state)
        for nxt_state, action, _ in problem.getSuccessors(state):
            # Prune new states that have already been explored
            if nxt_state in explored:
                continue
            elif problem.isGoalState(nxt_state):
                return actions + [action]
            else:
                queue.push([nxt_state, actions + [action]])

    # If problem is known to be unsolvable return a empty action set.
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import Queue
    print("Type of problem", problem)
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # [((5, 4), 'South', 1), ((4, 5), 'West', 1)] for initial state.

    # Perform DFS in a iterative process
    # Explored set of values

    explored = {} # Explored States of the Pacman graph
    queue = Queue()
    # Store current position and state and previous actions
    # Start State is in Explored Set by default.
    queue.push([problem.getStartState(),[]])
    while not queue.isEmpty():
        # represents current state of agent
        state, actions = queue.pop()
        # Only case if the start state is the goal
        if problem.isGoalState(state):
            print('Hello')
            return actions
        # When a element is poped from the stack, it is known to be first explored
        # explored.put(state)
        for nxt_state, action, _ in problem.getSuccessors(state):
            # Prune new states that have already been explored
            if nxt_state in explored:
                continue
            # if state is a goal state, return actions directly
            elif problem.isGoalState(nxt_state):
                print("returned directly")
                return actions + [action]
            else:
                queue.push([nxt_state, actions + [action]])

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
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST

    return [s, s, w, s, w, w, s, w]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
