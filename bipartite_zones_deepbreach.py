import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


G = nx.Graph()

G.add_nodes_from(["Sands of Inferno", 
"Boreal Mire of Necrosis", 
"The Great Sharay", 
"Xorn Slaver",
"Bizarre Bazaar"], bipartite=0)

G.add_nodes_from(["Djinni of Steam", 
"Oleg Smivivsen"], bipartite=1, )

G.add_edges_from([
("Sands of Inferno","Djinni of Steam"),
("Boreal Mire of Necrosis","Djinni of Steam"),
("The Great Sharay","Djinni of Steam"),
("Xorn Slaver","Djinni of Steam"),
("Bizarre Bazaar", "Oleg Smivivsen")
])


colors = nx.get_edge_attributes(G,'color').values()

l, r = nx.bipartite.sets(G)
pos = {}

# Update position for node from each group
pos.update((node, (1, index)) for index, node in enumerate(l))
pos.update((node, (2, index)) for index, node in enumerate(r))

# pos = nx.circular_layout(G)

if __name__ == "__main__":
    nx.draw(G, pos, with_labels=True)

    red_patch = mpatches.Patch(color='red', label='Zones')
    blue_patch = mpatches.Patch(color='blue', label='Deepbreach')
    plt.legend(handles=[red_patch, blue_patch])

    plt.show()