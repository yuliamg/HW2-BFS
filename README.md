![BuildStatus](https://github.com/yuliamg/HW2-BFS/workflows/test.yml/badge.svg?event=push)
# Assignment 2
Breadth-first search

## Implementation of a breadth-first search 

* The function **_check_empty_** initializes a graph and raises an error if it is empty. Likewise, the function **_check_node_exists_** ensures that an input node is in the graph, and raises an error if otherwise.
  
* The **_neighbors_** function takes in a node and returns a list of its neighbors.
  
* The **_bfs_** function is the main function for the breadth-first search. Its parameters are an initialized graph, a starting node, and an optional end node. The breadth-first search uses a first in-first out (FIFO) data structure, compatible with a list in Python. The **_queue_** keeps track of nodes to be visited, while the **_visited_** list keeps track of the nodes that have already been seen. A **_parents_** dictionary is initialized, where each key is a node and each value is the parent node. This allows for the bookkeeping of the shortest path from a start node to an end node. If an end node is provided, the function will first ensure it exists. Then, it will add the start node to the queue and visited lists. Then, the algorithm will take the first item of the queue, find its neighbors, evaluate if they are the end node, and add them to the queue and visited lists. It will also keep track of the parent nodes for each node by adding dictionary entries. As long as the queue is not empty, the search will continue, until it finds the end node. Once the end node is found, a path is reconstructed from the **_parents_** dictionary, returning the shortest path from the starting node to the end node. If an end node is not provided, the algorithm will output the full traversal.

## Unit tests

* In **_test_bfs_traversal_**, we ensure that neighbors are returned correctly, the BFS of the _tiny_network.adjlist_ returns 30 nodes, and correctly returns the order of traversal for an example node. Plus, an error is raised if the graph is empty or if a node does not exists in the graph.
  
* In **_test_bfs_**, we test that the shortest path between a start and end node is correct, as determined by the **_networkx shortest_path_** function. Additionally, we test that a node not in the graph will raise an error. 
