#Importación de librerias
import networkx as nx
import matplotlib.pyplot as plt

#Links para la realización del codigo
#Based from: https://www.python-course.eu/networkx.php
#Based from: https://stackoverflow.com/questions/27030473/how-to-set-colors-for-nodes-in-networkx
#Based from: https://stackoverflow.com/questions/47094949/labeling-edges-in-networkx

#Creacón del grafo
G=nx.Graph()

#Lista de nodos: Niveles                                       Ambito   
G.add_nodes_from(["Universidad", "Diversificado","Profesional", "Diseño Gráfico", "Ing. Industrial"])
G.add_nodes_from(["User001", "User002", "User003", "User004", "User005"])
G.add_nodes_from(["AlienWare", "HP Pavillion", "MAC", "Dell Inspiron", "Intel Celeron"])

#Relaciones de usuarios y campos.(Usuario:PC       Usuario:Niveles         Usuario:Ambito)
G.add_edges_from([['User001','AlienWare'], ("User001","Universidad"), ("User001","Diseño Gráfico")])
G.add_edges_from([("User002","HP Pavillion"),("User002","Profesional"), ("User002","Diseño Gráfico")])
G.add_edges_from([("User003","MAC"),("User003","Universidad"), ("User003","Ing. Industrial")])
G.add_edges_from([("User004","HP Pavillion"),("User004","Diversificado"), ("User004","Diseño Gráfico")])
G.add_edges_from([("User005", "Intel Celeron"), ("User005", "Diversificado"), ("User005", "Profesional")])

#Adquirir puntos donde se va a gráficar el grafo
pos = nx.spring_layout(G)

#Dibujar figura
plt.figure()

#Atributos para el grafo(Color de relaciones, nodos, entre otros)
nx.draw(G,pos,edge_color='black',width=1,linewidths=1,\
node_size=500,node_color='red',alpha=0.5,\
labels={node:node for node in G.nodes()})

#Presentacion de los nodos y relaciones del grafo
print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

#Muestra del grafo con labels en las relaciones y nodos
nx.draw_networkx_edge_labels(G,pos,edge_labels={('User001','AlienWare'):'PC',('User001','Universidad'):'Nivel', ('User001','Diseño Gráfico'):'Ambito',\
                                                ('User002','HP Pavillion'):'PC',('User002','Profesional'):'Nivel', ('User002','Diseño Gráfico'):'Ambito',\
                                                ('User003','MAC'):'PC',('User003','Universidad'):'Nivel', ('User003','Ing. Industrial'):'Ambito',\
                                                ('User004','HP Pavillion'):'PC',('User004','Diversificado'):'Nivel', ('User004','Diseño Gráfico'):'Ambito',\
                                                ('User005','Intel Celeron'):'PC',('User005','Diversificado'):'Nivel', ('User005','Profesional'):'Ambito',})

#plt.savefig("simple_path.png") #Sirve para guarda la imagen del grafo
plt.axis('off')#No hay punto de referencia
plt.show() #Mostar grafo