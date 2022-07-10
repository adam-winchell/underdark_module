import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

G = nx.Graph()
G.add_edge("Elder Brain","Juiblex",color='b')
G.add_edge("Elder Brain","Orcus",color='r')
G.add_edge("Juiblex","Zuggtmoy",color='r')
G.add_edge("Graz'zt","Orcus",color='r')
G.add_edge("Graz'zt","Zuggtmoy",color='b')
G.add_edge("Wyrm Shadow Dragon", "Elder Brain",color='r')
G.add_edge("Wyrm Shadow Dragon","Graz'zt",color='r')
G.add_edge("Wyrm Shadow Dragon","Zuggtmoy",color='r')
G.add_edge("Wyrm Shadow Dragon","Juiblex",color='r')
G.add_edge("Wyrm Shadow Dragon","Orcus",color='r')

colors = nx.get_edge_attributes(G,'color').values()


if __name__ == "__main__":
    nx.draw(G, edge_color=colors, with_labels=True, node_color="black")

    red_patch = mpatches.Patch(color='red', label='Enemies')
    blue_patch = mpatches.Patch(color='blue', label='Allies')
    plt.legend(handles=[red_patch, blue_patch])
    
    plt.show()

