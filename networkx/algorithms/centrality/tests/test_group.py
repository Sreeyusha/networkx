"""
    Tests for Group Centrality Measures
"""


from nose.tools import *
import networkx as nx


class TestGroupBetweennessCentrality:

    def test_group_betweenness_single_node(self):
        """
            Group betweenness centrality for single node group
        """
        G = nx.path_graph(5)
        C = [1]
        b = nx.group_betweenness_centrality(G, C,
                                            weight=None, normalized=False)
        b_answer = 3.0
        assert_equal(b, b_answer)

    def test_group_betweenness_normalized(self):
        """
            Group betweenness centrality for group with more than
            1 node and normalized
        """
        G = nx.path_graph(5)
        C = [1, 3]
        b = nx.group_betweenness_centrality(G, C,
                                            weight=None, normalized=True)
        b_answer = 1.0
        assert_equal(b, b_answer)

    def test_group_betweenness_value_zero(self):
        """
            Group betweenness centrality value of 0
        """
        G = nx.cycle_graph(6)
        C = [0, 1, 5]
        b = nx.group_betweenness_centrality(G, C, weight=None)
        b_answer = 0.0
        assert_equal(b, b_answer)

    def test_group_betweenness_disconnected_graph(self):
        """
            Group betweenness centrality in a disconnected graph
        """
        G = nx.path_graph(5)
        G.remove_edge(0, 1)
        C = [1]
        b = nx.group_betweenness_centrality(G, C, weight=None)
        b_answer = 0.0
        assert_equal(b, b_answer)

    @raises(nx.NodeNotFound)
    def test_group_betweenness_node_not_in_graph(self):
        """
            Node(s) in C not in graph, raises NodeNotFound exception
        """
        b = nx.group_betweenness_centrality(nx.path_graph(5), [6, 7, 8])


class TestGroupClosenessCentrality:

    def test_group_closeness_single_node(self):
        """
            Group closeness centrality for a single node group
        """
        G = nx.path_graph(5)
        c = nx.group_closeness_centrality(G, [1])
        c_answer = nx.closeness_centrality(G, 1)
        assert_equal(c, c_answer)

    def test_group_closeness_disconnected(self):
        """
            Group closeness centrality for a disconnected graph
        """
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4])
        c = nx.group_closeness_centrality(G, [1, 2])
        c_answer = 0
        assert_equal(c, c_answer)

    def test_group_closeness_multiple_node(self):
        """
            Group closeness centrality for a group with more than
            1 node
        """
        G = nx.path_graph(4)
        c = nx.group_closeness_centrality(G, [1, 2])
        c_answer = 1
        assert_equal(c, c_answer)

    @raises(nx.NodeNotFound)
    def test_group_closeness_node_not_in_graph(self):
        """
            Node(s) in S not in graph, raises NodeNotFound exception
        """
        c = nx.group_closeness_centrality(nx.path_graph(5), [6, 7, 8])


class TestGroupDegreeCentrality:

    def test_group_degree_centrality_single_node(self):
        """
            Group degree centrality for a single node group
        """
        G = nx.path_graph(4)
        d = nx.group_degree_centrality(G, [1])
        d_answer = nx.degree_centrality(G)[1]
        assert_equal(d, d_answer)

    def test_group_degree_centrality_multiple_node(self):
        """
            Group degree centrality for group with more than
            1 node
        """
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
        G.add_edges_from([(1, 2), (1, 3), (1, 6), (1, 7), (1, 8),
                          (2, 3), (2, 4), (2, 5)])
        d = nx.group_degree_centrality(G, [1, 2])
        d_answer = 1
        assert_equal(d, d_answer)

    def test_group_in_degree_centrality(self):
        """
            Group in-degree centrality in a DiGraph
        """
        G = nx.DiGraph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
        G.add_edges_from([(1, 2), (1, 3), (1, 6), (1, 7), (1, 8),
                          (2, 3), (2, 4), (2, 5)])
        d = nx.group_in_degree_centrality(G, [1, 2])
        d_answer = 0
        assert_equal(d, d_answer)

    def test_group_out_degree_centrality(self):
        """
            Group out-degree centrality in a DiGraph
        """
        G = nx.DiGraph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
        G.add_edges_from([(1, 2), (1, 3), (1, 6), (1, 7), (1, 8),
                          (2, 3), (2, 4), (2, 5)])
        d = nx.group_out_degree_centrality(G, [1, 2])
        d_answer = 1
        assert_equal(d, d_answer)

    @raises(nx.NetworkXError)
    def test_group_degree_centrality_node_not_in_graph(self):
        """
            Node(s) in S not in graph, raises NetworkXError
        """
        b = nx.group_degree_centrality(nx.path_graph(5), [6, 7, 8])