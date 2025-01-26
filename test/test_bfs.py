# write tests for bfs
import pytest
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    
    #create instace of Graph class
    g = graph.Graph(filename="../data/tiny_network.adjlist")
    
    #test that neighbors are being returned correctly
    assert g.neighbors('Neil Risch') == ['29700475']
    
    #we expect 30 nodes to be traversed
    assert len(g.bfs('Neil Risch')) == 30
    
    #if we start at 'Charles Chiu', we expect the first 6 nodes of the traversal to be: 
    assert g.bfs("Charles Chiu")[:6] == ['Charles Chiu', '33242416','Atul Butte','33765435','31395880','30944313']    
    
    #if we start a node not in the graph, we expect an error to be raised
    with pytest.raises(ValueError):
        g.bfs("Yulia Gutierrez")
        
    #create instace of empty graph
    g_empty = graph.Graph(filename="../data/empty_graph.adjlist")
    
    #assert that an error is raised when the graph is empty
    with pytest.raises(ValueError):
        g_empty.bfs("")
    

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    
    #create graph 
    g = graph.Graph(filename="../data/citation_network.adjlist")
    
    #testing that the shortest path between Luke Gilbert and Joseph Bondy-Denomy is correct using networkx to find the shortest path
    assert g.bfs("Luke Gilbert", "Joseph Bondy-Denomy") == nx.shortest_path(g.graph, "Luke Gilbert", "Joseph Bondy-Denomy")
    
    #testing that the shortest path between Luke Gilbert and a node not in the graph raisees an error 
    with pytest.raises(ValueError):
        g.bfs("Luke Gilbert", "Yulia Gutierrez")
    
    
        
    
        
    
    

    