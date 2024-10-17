'''
Лабораторная работа №2
Необходимо получить центральность для семи узлов с ростом в центре списка значений и опусканием на краях
'''
import networkx as nx
number_of_nodes = 7
G = nx.path_graph(number_of_nodes)
G.add_edge(2, 4)
G.add_edge(3, 1)
G.add_edge(3, 5)
G.add_edge(4, 5)
G.add_edge(5, 6)
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print(f'c({n}) = {centrality[n]:.4f}')