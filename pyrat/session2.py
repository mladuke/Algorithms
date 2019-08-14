
# coding: utf-8

# Welcome to the second Lab session of the Advanced algorithmics and graph theory with Python. In this session you will learn how to create stack and queue structures using lists in python and then use these data structures to create walks on the PyRat Maze.
# 
# The main objectives of this exercise are to:
# * Write functions to follow a shortest walk in a non weighted graph
# * Measure latency of the execution of a code
# 
# The idea here is to show you how to use simpler structures in order to create more advanced ones. All of the structures used here are already available by default with python, but doing them using list manipulation is a very good exercise.

# # List manipulation
# 
# The first thing we want you to know is list manipulation. Lists in python are containers of objects which can be accessed by a numerical index (starting by 0), which can be accessed in reverse order (-1 is the last element of the list).
# 
# The two main methods for list manipulation are append and pop. Append adds an element at the end of the list. Pop removes the element at the specified index. 
# 
# Finally lists have an interesting property, an empty list is treated as False in a if statement

# In[1]:


test_list = list()

print("Appending 1,2,3 to the list")

# Appending to the list
test_list.append(1)
print(test_list)

test_list.append(2)
print(test_list)

test_list.append(3)
print(test_list)

print("Access element 0")
element_zero = test_list[0]
print(element_zero)

print("Access all elements starting by index 1")
element_one_and_after = test_list[1:]
print(element_one_and_after)

print("Removing all elements on the list in the order of middle, last, first")


removed_element = test_list.pop(1)
print(removed_element,test_list)

removed_element = test_list.pop(-1)
print(removed_element,test_list)

removed_element = test_list.pop(0)
print(removed_element,test_list)

print("Appending 3,2,1 to the list")

test_list.append(3)
print(test_list)

test_list.append(2)
print(test_list)

test_list.append(1)
print(test_list)

if test_list:
    print("Non empty lists are considered as true in a if statement")
    
test_list = list()
print("The test list now contains: {}".format(test_list))

if not test_list:
    print("Empty lists are considered as false in a if statement")
    


# # LIFO Stack
# 
# LIFO (Last In, First Out) is a stack where the most recent elements are the first ones to be removed from the stack. In the next cell you can see one of the many possible implementations of LIFO using lists. There are two main functions:
# 
# 1. Push: responsable for inserting a new element on the correct position of the stack
# 2. Pop: responsable for removing the correct element from the stack
# 

# In[2]:


LIFO_list = list()

def LIFO_push(LIFO_list,element):
    LIFO_list.append(element)

def LIFO_pop(LIFO_list):
    return LIFO_list.pop(-1)


# We are going to test LIFO by adding three values (1,2,3) and verifying that when we do a pop operation they come out in the opposite order (3,2,1). We are also going to print the list at the intermediate steps to ensure that everything is working as desired.

# In[3]:


print(LIFO_list)
print("Push 1")
LIFO_push(LIFO_list,1)
print(LIFO_list)
print("Push 2")
LIFO_push(LIFO_list,2)
print(LIFO_list)
print("Push 3")
LIFO_push(LIFO_list,3)
print(LIFO_list)
print("Pop 3")
print(LIFO_pop(LIFO_list),LIFO_list)
print("Pop 2")
print(LIFO_pop(LIFO_list),LIFO_list)
print("Pop 1")
print(LIFO_pop(LIFO_list),LIFO_list)


# Now that you are familiarized with lists and the LIFO stack you can use them to create a Depth-First Search
# 
# # Depth-First Search (DFS)
# 
# Depth-First search is a traversal/search algorithm for trees and graphs that starts at a root vertex and explores as far as possible along each branch before backtracking.   
# 
# ## Exercise A (1pt)
# 
# Complete the DFS function which performs a DFS over a graph using a LIFO stack. It receives the maze map, which is a graph represented in a dictionary, in the same way we used in Lab 1, and a starting position. It should return a list with the order of explored vertices and a dictionary containing the vertices as the keys and their parents as the values. Note that we use a list for keeping track of explored vertices, where a set would be more efficient in practice.

# In[4]:


def add_to_explored_vertices(explored_vertices,vertex):
    explored_vertices.append(vertex)

def is_explored(explored_vertices,vertex):
    return vertex in list(explored_vertices)
    
def DFS(maze_graph, initial_vertex):
    
    # explored vertices list
    explored_vertices = list()
    
    #LIFO stack
    queuing_structure = list()
    
    #Parent Dictionary
    parent_dict = dict()
        
    # push the initial vertex to the queuing_structure
    LIFO_push(queuing_structure, (initial_vertex, None))
    while len(queuing_structure) > 0:  # while queuing_structure is not empty:
        # current_vertex,parent = queuing_structure.pop()
        (current_vertex, parent) = LIFO_pop(queuing_structure)
        # if the current vertex is not explored
        if not is_explored(explored_vertices, current_vertex):
            # add current_vertex to explored vertices
            add_to_explored_vertices(explored_vertices, current_vertex)
            # use parent_dict to map the parent of the current vertex
            parent_dict[current_vertex] = parent
            # for each neighbor of the current vertex in the maze graph:
            for neighbor in maze_graph[current_vertex]:
                # if neighbor is not explored:
                if not is_explored(explored_vertices, neighbor):
                    # push the tuple (neighbor,current_vertex) to the queuing_structure
                    LIFO_push(queuing_structure, (neighbor, current_vertex))
    return explored_vertices, parent_dict


# In[5]:


from operator import itemgetter
#
# AUTOGRADER TEST - DO NOT REMOVE
#


maze_graph = {
    (0,0): {(0,1):1,(1,0):1}, 
    (0,1): {(0,2):1,(0,0):1},
    (1,0): {(1,1):1,(0,0):1},
    (1,1): {(1,2):1,(1,0):1},
    (0,2): {(0,1):1,(1,2):1},
    (1,2): {(0,2):1,(1,1):1}
}
explored_vertices,parent_dict = DFS(maze_graph, (0,0))
print("Explored vertices order: {}".format(explored_vertices))
for vertex,parent in sorted(parent_dict.items(),key=itemgetter(0,0)):
    print("Vertex {} is the parent of vertex {}".format(parent,vertex))


# You should see one of the following:
# 
# ```
# Explored vertices order: [(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1)]
# Vertex None is the parent of vertex (0, 0)
# Vertex (0, 2) is the parent of vertex (0, 1)
# Vertex (1, 2) is the parent of vertex (0, 2)
# Vertex (0, 0) is the parent of vertex (1, 0)
# Vertex (1, 0) is the parent of vertex (1, 1)
# Vertex (1, 1) is the parent of vertex (1, 2)
# ```
# or 
# ```
# Explored vertices order: [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0)]
# Vertex None is the parent of vertex (0, 0)
# Vertex (0, 0) is the parent of vertex (0, 1)
# Vertex (0, 1) is the parent of vertex (0, 2)
# Vertex (1, 1) is the parent of vertex (1, 0)
# Vertex (0, 2) is the parent of vertex (1, 2)
# Vertex (1, 2) is the parent of vertex (1, 1)
# ```

# ## FIFO queue
# 
# FIFO (First In, First Out) is a queue where the oldest elements of the queue are the first ones to be removed. This type of queue has various applications including the Breadth-First search that we will code next.
# 
# ## Exercise B (1pt)
# 
# Based on the LIFO stack that we defined at the start of this session, create the auxiliary functions push and pop for a FIFO (first in first out) queue 

# In[6]:


FIFO_list = list()

def FIFO_push(FIFO_list,element):
    FIFO_list.append(element)

def FIFO_pop(FIFO_list):
    return FIFO_list.pop(0)


# In[7]:


#
# AUTOGRADER TEST - DO NOT REMOVE
#

print(FIFO_list)
print("Push 4")
FIFO_push(FIFO_list,4)
print(FIFO_list)
print("Push 2")
FIFO_push(FIFO_list,2)
print(FIFO_list)
print("Push 3")
FIFO_push(FIFO_list,3)
print(FIFO_list)
print("Pop 4")
print(FIFO_pop(FIFO_list),FIFO_list)
print("Pop 2")
print(FIFO_pop(FIFO_list),FIFO_list)
print("Pop 3")
print(FIFO_pop(FIFO_list),FIFO_list)


# After adding your code and correctly executing the last two cells you should see:
# 
# ```
# []
# Push 4
# [4]
# Push 2
# [4, 2]
# Push 3
# [4, 2, 3]
# Pop 4
# 4 [2, 3]
# Pop 2
# 2 [3]
# Pop 3
# 3 []
# 
# ```

# ## Breadth-first search (BFS)
# 
# Breadth-First search is another traversal/search algorithm for trees and graphs that unlike DFS tries to explore all the vertices at the present "depth" before going deeper in the data structure. 
# 
# ## Exercise C (1pt)
# 
# Complete the BFS function which performs a BFS over a graph using a FIFO queue. As an input it receives the maze map that is a graph represented in a dictionary, in the same way we used in Lab 1 and a starting position. It should return a list with the order of executed vertices and a dictionary containing the vertices as the keys and its parents as the value. You should not visit the same vertex twice.

# In[8]:


def BFS(maze_graph, initial_vertex) :
    
    # explored vertices list
    explored_vertices = list()
    
    #LIFO stack
    queuing_structure = list()
    
    #Parent Dictionary
    parent_dict = dict()
        

    # push the initial vertex to the queuing_structure
    FIFO_push(queuing_structure, (initial_vertex, None))
    while len(queuing_structure) > 0:  # while queuing_structure is not empty:
        # current_vertex,parent = queuing_structure.pop()
        (current_vertex, parent) = FIFO_pop(queuing_structure)
        # if the current vertex is not explored
        if not is_explored(explored_vertices, current_vertex):
            # add current_vertex to explored vertices
            add_to_explored_vertices(explored_vertices, current_vertex)
            # use parent_dict to map the parent of the current vertex
            parent_dict[current_vertex] = parent
            # for each neighbor of the current vertex in the maze graph:
            for neighbor in maze_graph[current_vertex]:
                # if neighbor is not explored:
                if not is_explored(explored_vertices, neighbor):
                    # push the tuple (neighbor,current_vertex) to the queuing_structure
                    FIFO_push(queuing_structure, (neighbor, current_vertex))
    return explored_vertices, parent_dict


# In[9]:


#
# AUTOGRADER TEST - DO NOT REMOVE
#

maze_graph = {
    (0,0): {(0,1):1,(1,0):1}, 
    (0,1): {(0,2):1,(0,0):1},
    (1,0): {(1,1):1,(0,0):1},
    (1,1): {(1,2):1,(1,0):1},
    (0,2): {(0,1):1,(1,2):1},
    (1,2): {(0,2):1,(1,1):1}
}

explored_vertices,parent_dict = BFS(maze_graph, (0,0))
print("explored vertices order: {}".format(explored_vertices))
for vertex,parent in sorted(parent_dict.items(),key=itemgetter(0,0)):
    print("vertex {} is the parent of vertex {}".format(parent,vertex))


# After correctly adding your code and executing the two last cells you should see one of the following:
# 
# ```
# explored vertices order: [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (1, 2)]
# vertex None is the parent of vertex (0, 0)
# vertex (0, 0) is the parent of vertex (0, 1)
# vertex (0, 1) is the parent of vertex (0, 2)
# vertex (0, 0) is the parent of vertex (1, 0)
# vertex (1, 0) is the parent of vertex (1, 1)
# vertex (0, 2) is the parent of vertex (1, 2)
# ```
# 
# ```
# explored vertices order: [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)]
# vertex None is the parent of vertex (0, 0)
# vertex (0, 0) is the parent of vertex (0, 1)
# vertex (0, 1) is the parent of vertex (0, 2)
# vertex (0, 0) is the parent of vertex (1, 0)
# vertex (1, 0) is the parent of vertex (1, 1)
# vertex (1, 1) is the parent of vertex (1, 2)
# ```
# 

# ## Exercise D (1pt)
# 
# Using the parent_dictionary generated by running one of the searches, complete the function create_walk_from_parents, which receives the parent dictionary as input, an initial vertex and an target vertex. It returns a list which contains a walk between two points. 

# In[10]:


def create_walk_from_parents(parent_dict,initial_vertex,target_vertex):
    walk = list()
    walk.append(target_vertex)
    while(initial_vertex != target_vertex):
        key = parent_dict[target_vertex]
        walk.append(key)
        target_vertex = key
    walk.reverse()
    if walk != []:
        del walk[0]
    return walk


# In[11]:


#
# AUTOGRADER TEST - DO NOT REMOVE
#

initial_vertex = (0,0)
target_vertex = (0,0)
explored_vertices,parent_dict = DFS(maze_graph,initial_vertex)
route = create_walk_from_parents(parent_dict,initial_vertex,target_vertex)
print("The route to go from vertex {} to {} is: {}".format(initial_vertex,target_vertex,route))


initial_vertex = (0,0)
target_vertex = (0,2)
explored_vertices,parent_dict = DFS(maze_graph,initial_vertex)
route = create_walk_from_parents(parent_dict,initial_vertex,target_vertex)
print("The route to go from vertex {} to {} is: {}".format(initial_vertex,target_vertex,route))


# After correctly adding your code and executing the two last cells you should see one of the following:
# 
# ```
# The route to go from vertex (0, 0) to (0, 0) is: []
# The route to go from vertex (0, 0) to (0, 2) is: [(1, 0), (1, 1), (1, 2), (0, 2)]
# 
# or
# 
# The route to go from vertex (0, 0) to (0, 0) is: []
# The route to go from vertex (0, 0) to (0, 2) is: [(0, 1), (0, 2)]
# ```

# ## Exercise E (1pt)
# 
# Using the walk generated by the create_walk_from_parents function, complete the function walk_to_route, which receives the walk as input and a vertex and returns a list of movements using the get_direction function

# In[12]:


from utils import get_position_above,get_position_left,get_position_below,get_position_right
from utils import MOVE_UP,MOVE_DOWN,MOVE_LEFT,MOVE_RIGHT

def get_direction(initial_vertex,target_vertex):
    if get_position_above(initial_vertex) == target_vertex:
        return MOVE_UP
    elif get_position_below(initial_vertex) == target_vertex:
        return MOVE_DOWN
    elif get_position_left(initial_vertex) == target_vertex:
        return MOVE_LEFT
    elif get_position_right(initial_vertex) == target_vertex:
        return MOVE_RIGHT
    else:
        raise Exception("vertices are not connected")

def walk_to_route(walk,initial_vertex):
    steps = []
    for direction in walk:
        steps.append(get_direction(initial_vertex,direction))
        initial_vertex = direction
    return steps
                    


# In[13]:


#
# AUTOGRADER TEST - DO NOT REMOVE
#


walk = [(0, 1), (1, 1), (2, 1)]
print("The route to walk {} is {}".format(walk,walk_to_route(walk,(0,0))))


# After correctly adding your code and executing the two last cells you should see:
# 
# ```
# The route to walk [(0, 1), (1, 1), (2, 1)] is ['U', 'R', 'R']
# ```

# ## Exercise F (1pt)
# 
# Using the BFS search and all of the auxiliary functions that we implemented in this notebook, 
# complete the function A_to_B which receives a initial vertex A and a target vertex B and returns 
# the list of movements that should be done.

# In[14]:


def A_to_B(maze_graph,initial_vertex,target_vertex):
    explored_vertices, parent_dict = BFS(maze_graph, initial_vertex)
    route = create_walk_from_parents(parent_dict,initial_vertex,target_vertex)
    return walk_to_route(route,initial_vertex)

    


# In[15]:


#
# AUTOGRADER TEST - DO NOT REMOVE
#

a = (0,0)
b = (1,2)
print("The route from {} to {} is {}".format(a,b,A_to_B(maze_graph,a,b)))
print("The route from {} to {} is {}".format(b,a,A_to_B(maze_graph,b,a)))


# After correctly adding your code and executing the two last cells you should see one of the following:
# 
# ```
# The route from (0, 0) to (1, 2) is ['U', 'U', 'R']
# or
# The route from (0, 0) to (1, 2) is ['R', 'U', 'U']
# ```
# 
# and also one of the following
# 
# ```
# The route from (1, 2) to (0, 0) is ['L', 'D', 'D']
# or
# The route from (1, 2) to (0, 0) is ['D', 'D', 'L']
# ```
# 

# # Extra
# 
# Now that you have created the A_to_B function, we can use it to search cheeses in the PyRat maze, execute the cells below to see an example of how to do it. You can then add your own cells and try it by yourself!

# The first thing is to start the display

# In[16]:


import pyrat
pyrat.start_display()


# Now we define the starting point and the target point. The target point will be represented by a cheese and your player will be represented by the rat.

# In[17]:


starting_vertex = (2,2)
target_vertex = (4,4)


# Finally we can create a turn function using the A_to_B function and run a game to see our agent moving in the direction of the cheese. 

# In[18]:


def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):    
    return A_to_B(maze_graph=mazeMap,initial_vertex=playerLocation,target_vertex=piecesOfCheese[0])[0]


game = pyrat.Game(turn_1=turn,player1_start=starting_vertex,cheeses_start=[target_vertex])
game.play_match()
pyrat.display_game(game)


# This is not the most optimal way to use the function A_to_B, because it is called once for every turn. 
# 
# Considering that it is possible to specify a function called preprocessing as preprocess_1 in the creation of the game and that this function will then be executed only at the beginning of a match, do you think it is possible to do it in a way that you only call the A_to_B function once? 

# In[21]:


def preprocessing(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese, timeAllowed):
    global moveList
    moveList = A_to_B(maze_graph=mazeMap,initial_vertex=playerLocation,target_vertex=piecesOfCheese[0])
    
    
def new_turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):    
    global moveList
    if moveList != []:
        return moveList.pop(0)
    else:
        preprocessing(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese, timeAllowed)
        return moveList.pop(0)


# In[22]:


game = pyrat.Game(preprocess_1=preprocessing,turn_1=new_turn,player1_start=starting_vertex,cheeses_start=[target_vertex])
game.play_match();
#Uncomment the next line after correctly adding the code for preprocessing and new_turn
pyrat.display_game(game)


# In[ ]:





# In[ ]:





# In[ ]:



