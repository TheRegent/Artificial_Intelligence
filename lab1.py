import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx

def print_hi(N):
    G = nx.grid_2d_graph(N, N)
    pos = dict((n, n) for n in G.nodes())
    labels = dict(((i, j), i + (N - 1 - j) * N) for i, j in G.nodes())
    nx.draw_networkx(G, pos=pos, labels=labels, with_labels=False, node_size=10)
    plt.show()


if __name__ == '__main__':
    print_hi(5)

