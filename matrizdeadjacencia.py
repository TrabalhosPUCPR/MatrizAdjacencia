import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#pode incluir uma lista de vertices (nodes)
Graf = (["a", "b", "c", "d", "e", "f"])
G.add_nodes_from(Graf)

#matriz de adjacencia
matriz_a = [
(0,	1,	1,	1,	0,	1),
(1,	0,	0,	0,	1,	0),
(1,	0,	0,	0,	1,	0),
(1,	0,	0,	0,	0,	1),
(0,	1,	1,	0,	0,	1),
(1,	0,	0,	1,	1,	0)

]

arestas = []
for y in range(len(matriz_a)): #vai pega a quantidade de linhas, y igual a linha atual
    for x in range(len(matriz_a[y])): #vai pega a quantidade de valores dentro da linha y, x igual a posicao atual
        if matriz_a[y][x] == 1: #vai verificar se o valor na linha y na posicao x e 1
            arestas.append((Graf[y], Graf[x])) #se sim vai inserir as letras para criar as arestas

G.add_edges_from(arestas)
print("Vertices do grafo: ")
print(G.nodes())
print("Arestas do grafo: ")
print(G.edges())

nx.draw(G, with_labels=True)
plt.show()

#plt.savefig("grafo1.png") # salvar como png