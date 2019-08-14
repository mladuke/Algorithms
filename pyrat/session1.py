
# coding: utf-8

# Welcome to the first lab session of the MOOC "Advanced algorithmics and graph theory with Python".
# 
# Throughout the labs, you will program an AI to play a game in a maze where two players, a rat and a python, compete for grabbing pieces of cheese before their opponent. This game is called PyRat.
# 
# In this first lab you will learn how to navigate on the PyRat Maze.
# 
# The main objective of this exercise is to:
# * Write basic functions in Python to manipulate graphs (choose the appropriate data-structure, iterate on neighbors...)
# 
# To achieve this objective you will have to add code in order to complete several functions. Everytime you see `YOUR CODE HERE` you will have to insert your code so that the function implements the specification correctly.
# 
# For example, in the following cell you are going to see the get_position_above function, which is already completed for you. This function takes a vertex which is tuple of coordinates (x,y) and returns the position above those coordinates. 
# 
# <img src="axis_example.png" height="400px" width="400px">
# 
# In PyRat, we index cells of the maze with tuples (x,y), where x refers to the horizontal axis and y refers to the vertical axis. So, the position (0,0) is the bottom left corner, while (width - 1, height - 1) is the top right corner. This means that increasing the value of the x coordinate, we are going to move right, while decreasing the value moves to the left. In the same way, increasing the value of the y coordinate you are going to move up, while decreasing the value moves down.
# 
# Note that in practice it is not possible to move left if x is 0, or to move right if x is width - 1. Similarly it is not possible to move down if y is 0, or to move up if y is height - 1. Nevertheless, we will ignore this for the moment. Also, we consider a maze with no wall to begin with.

# In[1]:


# Function get_position_above
# inputs: original_position which is a couple of ints
# outputs: coordinates of the position above original_position
def get_position_above(original_position):
    """
    Given a position (x,y) returns the position above the original position, defined as (x,y+1)
    """
    (x,y) = original_position
    return (x,y+1)

# Tests:
initial_position = 4,8
print("Our initial position is {}".format(initial_position))
position_above = get_position_above(initial_position)
print("The position above ours is {}".format(position_above))


# After executing the cell above you should see:
# ```
# Our initial position is (4, 8)
# The position above ours is (4, 9)
# ```
# 
# as the output.

# # Exercise A (3pt)
# 
# Now it is your turn. Code the remaining three directions:
# 
# 1. get_position_below
# 2. get_position_right
# 3. get_position_left

# In[2]:


def get_position_below(original_position):
    """
    Given a position (x,y) returns the position below the original position, defined as (x,y-1)
    """
    (x,y) = original_position
    return(x,y-1)
    
def get_position_right(original_position):
    """
    Given a position (x,y) returns the position to the right of the original position, defined as (x+1,y)
    """
    (x,y) = original_position
    return(x+1,y)

def get_position_left(original_position):
    """
    Given a position (x,y) returns the position to the left of the original position, defined as (x-1,y)
    """
    (x,y) = original_position
    return(x-1,y)
    
print("Our initial position is {}".format(initial_position))


# In[3]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###
position_below = get_position_below(initial_position)
print("The position directly below ours is {}".format(position_below))


# In[4]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###
position_right = get_position_right(initial_position)
print("The position directly to the right of ours is {}".format(position_right))


# In[5]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###
position_left = get_position_left(initial_position)
print("The position directly to the left of ours is {}".format(position_left))


# After adding your code and correctly executing the four cells above you should see:
# ```
# Our initial position is (4, 8)
# 
# The position directly below ours is (4, 7)
# 
# The position directly to the right of ours is (5, 8)
# 
# The position directly to the left of ours is (3, 8)
# ```
# 
# as the output.

# # Exercise B (1pt)
# 
# Another useful function to navigate on a maze is to be able to recognize if two positions (cells) are adjacent, which means that the first one is above, below, left or right of the other one. Complete the function are_adjacent to return True if two nodes are adjacent and False if not.

# In[6]:


def are_adjacent(position1,position2):
    """
    Given two positions (x1,y1) and (x2,y2) returns True if they are adjacent and False if not
    """   
    state1 = position1==get_position_below(position2)
    state2 = position1==get_position_above(position2)
    state3 = position1==get_position_left(position2)
    state4 = position1==get_position_right(position2)
    return (state1 or state2 or state3 or state4)
    


# In[7]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###
position2 = (4,7)
position3 = (5,8)
print("Are positions {} and {} adjacent? {}.".format(position2,position3,are_adjacent(position2,position3)))
print("Are positions {} and {} adjacent? {}.".format(initial_position,position3,are_adjacent(initial_position,position3)))
print("Are positions {} and {} adjacent? {}.".format(position2,initial_position,are_adjacent(position2,initial_position)))


# After adding your code and correctly executing the two cells above you should see:
# ```
# Are positions (4, 7) and (5, 8) neighbors? False.
# Are positions (4, 8) and (5, 8) neighbors? True.
# Are positions (4, 7) and (4, 8) neighbors? True.
# ```
# 
# as the output.

# # Exercise C (1pt)
# 
# When we add walls to a maze, it is important to know where the walls are to avoid trying to move through them.
# 
# Given a maze (graph dictionary), a starting position (x,y) and a move, complete the possible_move function, which returns True if it is possible to do the move and False if it is not possible.
# 
# The graph dictionary definition can be read as 
# ```
# maze_graph = {
#     (position now): [(connected position 1,cost of moving to connected position 1),(connected position 2,cost of moving to connected position 2)...]
# }
# ```
# 
# For example, consider the following graph
# 
# ```
# maze_graph = {
#     (0,0): {(1,0):1},
#     (1,0): {(0,0):1,(1,1):1},
#     (1,1): {(1,0):1}
# }
# ```
# 
# This would lead to the following maze:
# 
# <img src="graphexample.png" height="200px" width="200px">
# 
# To define a move we have four variables (MOVE_RIGHT, MOVE_LEFT, MOVE_UP, MOVE_DOWN), these are the same variables that you will have to use when you create your AI for the pyrat game. They are encoded as one character representing the direction
# ```
# MOVE_RIGHT = "R"
# MOVE_LEFT = "L"
# MOVE_UP = "U"
# MOVE_DOWN = "D"
# ```

# In[11]:


maze_graph = {
    (0,0): {(1,0):1},
    (1,0): {(0,0):1,(1,1):1},
    (1,1): {(1,0):1}
}

MOVE_RIGHT = "R"
MOVE_LEFT = "L"
MOVE_UP = "U"
MOVE_DOWN = "D"


# In[15]:


def possible_move(maze_graph,initial_position,move):
    # Example to check if moving up is possible
    if move == MOVE_UP:
        if get_position_above(initial_position) in maze_graph[initial_position].keys():
            return True
        else:
            return False
    elif move == MOVE_DOWN:
        if get_position_below(initial_position) in maze_graph[initial_position].keys():
            return True
        else:
            return False
    elif move == MOVE_RIGHT:
        if get_position_right(initial_position) in maze_graph[initial_position].keys():
            return True
        else:
            return False
    elif move == MOVE_LEFT:
        if get_position_left(initial_position) in maze_graph[initial_position].keys():
            return True
        else:
            return False
    else:
        raise ValueError("Invalid or unimplemented move")


# In[16]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


result1 = possible_move(maze_graph,(1,0),MOVE_UP)
result2 = possible_move(maze_graph,(0,0),MOVE_UP)
print("Testing move up, first is {} and second is {}".format(result1,result2))

result1 = possible_move(maze_graph,(1,0),MOVE_LEFT)
result2 = possible_move(maze_graph,(0,0),MOVE_LEFT)
print("Testing move left, first is {} and second is {}".format(result1,result2))

result1 = possible_move(maze_graph,(0,0),MOVE_RIGHT)
result2 = possible_move(maze_graph,(1,0),MOVE_RIGHT)
print("Testing move right, first is {} and second is {}".format(result1,result2))

result1 = possible_move(maze_graph,(1,1),MOVE_DOWN)
result2 = possible_move(maze_graph,(0,0),MOVE_DOWN)
print("Testing move down, first is {} and second is {}".format(result1,result2))



# After adding your code and correctly executing the cell above you should see:
# ```
# Testing move up, first is True and second is False
# Testing move left, first is True and second is False
# Testing move right, first is True and second is False
# Testing move down, first is True and second is False
# ```
# 
# as the output.

# # Exercise D (1pt)
# 
# Now that you get the basics about manipulating the maze and moving aronud, let us explain how an AI actually works.
# 
# An AI for PyRat is made of three functions in python, preprocessing, turn and postprocessing. For the most part of this course you are only going to use the turn function.
# 
# Preprocessing and postprocessing are functions that we do not need for now. It will be of use in more advanced labs to perform intensive computations once and for all.
# 
# The function turn is what we will concentrate on for now. Each time the game wants to know the decision move of your AI, the function turn will be called. The function turn has many parameters that are pretty simple to understand:
# * the map of the maze (mazeMap), which follows the same structure as in the previous example,
# * the width (mazeWidth) and the height (mazeHeight)of the maze, which are integers,
# * your player location (playerLocation) and the location of the opponent (opponentLocation) which are couples of integers,
# * your score (playerScore) and that of the opponent (opponentScore) which are integers, initially 0,
# * the locations of the pieces of cheese in the maze (piecesOfCheese) which we ignore for now,
# * the number of milliseconds you have to take your decision (timeAllowed) which is an integer.
# 
# The turn function should return one of MOVE_RIGHT, MOVE_LEFT, MOVE_UP or MOVE_DOWN. Any other output would be considered a will to stay still.
# 
# As a first trivial example, code a turn function that always go right.

# In[17]:


MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'
def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):    
      return(MOVE_RIGHT)


# The first thing we have to do is initialize the display of the pyrat game. Every game that we want to display in this lesson will be shown in the cell bellow.

# In[18]:


import pyrat
pyrat.start_display()


# Now let's test the function turn on PyRat. We will first start by defining a small maze (7x1) with only one piece of cheese and without walls or mud. We will also initialize the display.

# In[19]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###
pyrat.density = 0
pyrat.mud_density = 0
pyrat.width = 7
pyrat.height = 1
pyrat.pieces = 1
pyrat.random_seed = 5
game = pyrat.Game(turn_1=turn)
game.play_match()
pyrat.display_game(game)


# # Exercise E (1pt)
# 
# Now let us try something a bit more elaborate.
# 
# Code a turn function that plays at random: it selects any move at random with probability 1/4 at each turn.
# 
# It will be capable of always finding all the cheeses on the maze, but it may take a while. Use the function random.choice which performs a random choice over a list. The list MOVES contains all the possible moves.

# In[20]:


MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'
MOVES = [MOVE_DOWN,MOVE_LEFT,MOVE_RIGHT,MOVE_UP]
import random

def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):    
    return(random.choice(MOVES))


# In[21]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###
pyrat.density = 0
pyrat.mud_density = 0
pyrat.width = 3
pyrat.height = 5
pyrat.pieces = 1
pyrat.random_seed = 8
game = pyrat.Game(turn_1=turn)
game.play_match()
pyrat.display_game(game)


# Do not forget to submit your results before exiting!