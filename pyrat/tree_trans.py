def traversal(start_vertex, graph):
    # This unified algorithm takes a graph, a start_vertex part of this graph,
    # and performs graph traversal using a queuing structure.
    # The algorithm returns the list of explored_vertices, and a
    # routing table to navigate the graph.

    # First we create either a LIFO a FIFO
    queuing_structure = new_queuing_structure()
    # Add the starting vertex with NULL as parent
    queuing_structure.push(start_vertex, NULL)
    # Initialize the outputs
    explored_vertices = []
    routing_table = {}
    while queuing_structure is not empty:

        # This will return the next vertex
        # to be examined,and the choice of queuing structure will
        # change the resulting order.

        (current_vertex, parent) = queuing_structure.pop()

        # Tests whether the current vertex is
        # in the list of explored vertices
        if not (current_vertex in explored_vertices):
            # Mark the current_vertex as explored
            explored_vertices.push(current_vertex)

            # Update the routing table accordingly
            routing_table[current_vertex] = parent

            # Examine neighbors of the current vertex
            for neighbor in graph[current_vertex]:
                # We push all unexplored neighbors to the queue
                if neighbor not in explored_vertices:
                    queuing_structure.push(neighbor, current_vertex)

    return explored_vertices, routing_table
