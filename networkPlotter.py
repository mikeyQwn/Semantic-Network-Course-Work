import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
import random


def plot_sentence_links_array(sentence_links_array):
    G = nx.DiGraph()
    nodes = {}
    for sentence_links in sentence_links_array:
        for link in sentence_links:
            nodes[link.subject] = random.random()
            nodes[link.addition] = random.random()
            G.add_edges_from([(link.subject, link.addition)], label=link.predicate)

    edge_labels = dict(
        [
            (
                (
                    u,
                    v,
                ),
                d["label"],
            )
            for u, v, d in G.edges(data=True)
        ]
    )

    # Specify the edges you want here

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap("jet"), node_size=1500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=50)
    plt.show()
