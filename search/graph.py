import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
    
    #function to check if a graph is empty (and raise and error if so)
    def check_empty(self): 
        if len(self.graph.nodes()) == 0:
            raise ValueError()
    
    #function to check if a node exists in the graph (and raise an error if not)
    def check_node_exists(self, node):
        if node not in self.graph.nodes():
            raise ValueError()
    
    #function to return the neighbors of a node 
    def neighbors(self, node):
        """
        Function to return the neighbors of a node
        """
        neighbors = self.graph.neighbors(node)
        return list(neighbors) #returns as a list
        
                
    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        
        #initialize the queue and visited lists
        queue = []
        visited = []
        parent = {start: None} #initalize parents dictionary to keep track of the parents of each node

                
        #check if the graph is empty
        self.check_empty()
        
        #check if the start node exists
        self.check_node_exists(start) 

        #append the start node to the queue
        queue.append(start)
        visited.append(start)
        
        #breadth first search for when the end node is speficied 
        if end is not None:
            self.check_node_exists(end) #check if the end node exists 
    
            while len(queue) != 0: #as long as the queue is not empty 
        
                v = queue.pop(0) #get the first node in the queue
                N = self.neighbors(v) #get the neighbors of the current node
                
                for w in N: #iterate through the neighbors 
                    if w not in visited:
                        visited.append(w) #then append it to the visited list
                        queue.append(w) #and append it to the queue
                        parent[w] = v #keeping track of parent node - v is the parent of w
                        
                        if w == end: #if the neighbor is the end node, then break (no need to search through any of the other neighbors) 
                            break
                        
                if end in visited: #if the end node is in the visited list, then break the loop (because we stop the search)
                    break
    
            if end not in visited: #if the end node is not in the visited list even after searching through all the connected nodes, then returns None
                return None
        
            else:  #otherwise (used chatgpt to help with this part)
                path = [] #initialize an empty list
                while end is not None: #as long as the end node is not None 
                    path.append(end) #then append the end node to the path
                    end = parent[end] #the set end node is the parent of the current end node, and will continue to loop until the end node is None
                return path[::-1] #path will return the path in reverse order (end-->start), so we reverse it to get the correct order (start --> end)
            
        #breadth first search for when the end node is not specified
        else: 
            while len(queue) != 0: #as long as the queue is not empty
                v = queue.pop(0) #get the first node in the queue
                N = self.neighbors(v) #get the neighbors of the current node
                    
                for w in N: #for each neighbor
                    if w not in visited: #if the neighbor has not been visited
                        queue.append(w) #append it to the queue
                        visited.append(w) #and append it to the visited list
        
            return visited #return the visited list, because will contain the path of traversal
            
            
    
        
        
        
        
        
        
        
        
        
        
        
        




