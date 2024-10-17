'''
Лабораторная работа №3
Значения количества вершин и вероятность появления случайного ребра (n=5, p=0.5)
Вычислить в программе среднюю степень вершины и сравнить её со значением средней степени вершины,
полученной по формуле из материала лекций. (n-1)*p
'''
import networkx as nx
number_of_nodes = 5
random_edge_percent = 0.5
G = nx.erdos_renyi_graph(number_of_nodes, random_edge_percent)
a = 0
for n in G.nodes():
    a = a + G.degree(n)
print(f'Cредняя степень вершины: {float(a) / len(G.nodes())}')
print(
    f'Cредняя степень вершины по формуле из лекций: '
    f'{(number_of_nodes - 1) * random_edge_percent}')