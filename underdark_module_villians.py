import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("Elder Brain","Juiblex",color='b')
G.add_edge("Juiblex","Zuggtmoy",color='r')
G.add_edge("Graz'zt","Orcus",color='r')
G.add_edge("Graz'zt","Zuggtmoy",color='b')
G.add_edge("Wyrm Shadow Dragon", "Elder Brain",color='r')
G.add_edge("Wyrm Shadow Dragon","Orcus",color='r')

colors = nx.get_edge_attributes(G,'color').values()

# pos = nx.circular_layout(G)

if __name__ == "__main__":
    nx.draw(G, edge_color=colors, with_labels=True)
    plt.legend(loc="upper left")
    plt.show()

