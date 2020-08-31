#TEST
#python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
#DFS
#python pacman.py -l tinyMaze -p SearchAgent
#python pacman.py -l mediumMaze -p SearchAgent
#python pacman.py -l bigMaze -z .5 -p SearchAgent
#BFS
#python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs --frameTime 0
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5 --frameTime 0
# UCS
#python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
#python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
#python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
# A Star algorithm
#python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

#Formulate a Search problem
#python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
#python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
#python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
