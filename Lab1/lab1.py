import matplotlib.pyplot as plt
import networkx as nx
import random

def ways_draw(delete, N=5):
    exeption = (N-1)**2

    if delete > exeption:
        print("Ви ввели число більше допустимого! Граф не буде зв\'язвним.")
    else:
        G = nx.grid_2d_graph(N, N)
        pos = dict((n, n) for n in G.nodes())
        nx.draw_networkx(G, pos=pos, with_labels=False, node_size=300, node_color="PaleGreen")
        plt.show()

        while delete > 0:
            edges = list(G.edges)
            chosen_edge = random.choice(edges)
            G.remove_edge(chosen_edge[0], chosen_edge[1])

            if nx.is_connected(G):
                delete -= 1
            else:
                G.add_edge(chosen_edge[0], chosen_edge[1])
        nx.draw_networkx(G, pos=pos, with_labels=False, node_size=300, node_color="PaleGreen")
        plt.show()

if __name__ == '__main__':
    N = int(input("Введіть розмірність матриці: "))
    delete = int(input("Введіть кількість ребер на видалення: "))
    ways_draw(delete, N)