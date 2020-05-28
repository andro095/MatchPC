from neo4j import GraphDatabase

#Clase principal
class Graph_manager:
    #Inicialización
    db = None
    def __init__(self):
        #Conexion y configuracion de python para neo4j
        uri             = "bolt://localhost:7687"
        userName        = "neo4j"
        password        = "123"
        db = GraphDatabase.driver(uri, auth=("neo4j", "Lisp1234"), encrypted=False)
        print("simon")
        
     #Setter y Getter   
    def get_graph(self):
        return self.graph
        
    def set_graph(self, g):
        self.graph = g
        
    def get_user(self):
        return self.user
    
    def set_user(self, u):
        self.user = u
        
    
        
    #Recomendar computadora a usuario
    def recommend(self, user, ambito, nivel, pc):
        N=input("Ingrese Nivel\t")
        A=input("Ingrese ambito de trabajo\t")
        
        with db.session() as session:
            for record in session.run("MATCH (usuario:user)-[:Nivel|:Ambito|:PC]->(r)"
                             "WHERE usuario.user = $user "
                             "RETURN r.pc", ambito=A, nivel=N, pc = pc):
                print(record["r.pc"])
            
    
    def add_User(self, user, ambito, nivel, pc):
        N=input("Ingrese Nivel\t")
        A=input("Ingrese ambito de trabajo\t")
        
        tipo=input("Ingrese tipo de computadora")
        marca=input("Ingrese marca de computadora")
        modelo=input("Ingrese modelo de computadora")
        cpu=input("Ingrese cpu de computadora")
        tipoRam=input("Ingrese tipo de RAM")
        capacidadRam=input("Ingrese capacidad de RAM")
        graficaMarca=input("Ingrese marca de la tarjeta grafica")
        graficaModelo=input("Ingrese modelo de la tarjeta grafica")
        
        
        
        with db.session() as session:
            for record in session.run("CREATE (User{id:id}), Ambito({ambito:A}, Nivel({nivel:N},"
                                      "PC({tipo:tipo, marca:marca, modelo:modelo, cpu=cpu, tipoRam:tipoRam,"
                                      "capacidadRam:capacidadRam, graficaMarca:graficaMarca, graficaModelo:graficaModelo})))"):
                id=id, ambito=A, nivel=N, tipo=tipo, marca=marca, modelo=modelo, cpu=cpu, tipoRam=tipoRam, capacidadRam=capacidadRam, graficaMarca=graficaMarca, graficaModelo=graficaModelo        
    
    def generate_id(self):
        with db.session() as session:
            for record in session.run("MATCH (Usuario:user)"
                             "WHERE a.id = $id"
                             "RETURN r.id", id=id):
                print(record["r.id"])
                id += 1
                
manager = Graph_manager()
Graph_manager.add_User(1,2,3,4,5)

        
        
    
        
            
            
        
    



