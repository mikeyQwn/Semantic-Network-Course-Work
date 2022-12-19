import networkx as nx
import matplotlib.pyplot as plt
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

    pos = nx.circular_layout(G)
    nx.draw_networkx(
        G, pos, node_size=3000, alpha=0.9, arrowsize=25, node_color="green"
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.axis("off")
    plt.show()
