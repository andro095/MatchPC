from neo4j import GraphDatabase

#Clase principal

class Graph_manager:
    #Inicialización
    def __init__(self):
        #Conexion y configuracion de python para neo4j
        uri             = "bolt://localhost:7687"
        userName        = "neo4j"
        password        = "Lisp1234"
        self.db = GraphDatabase.driver(uri, auth=(userName, password), encrypted=False)
        
    #Setter y Getter   
    def get_graph(self):
        return self.db
        
    def set_graph(self, db):
        self.db = db
        
    #Recomendar computadora a usuario
    def recommend(self, ambito, nivel):
        with self.db.session() as session:
            record = session.run("MATCH (p:PC),(u:User) WHERE (u)-[:Ambito]->({Ambito:'%s'}) AND (u)-[:Nivel]->({Level:'%s'}) AND (u)-[:PC]->(p) RETURN p, COUNT(p)"%(ambito,nivel))
            results = []
            for line in record:
                results.append((dict(line["p"]), line["COUNT(p)"]))
                
            return sorted(results, key=lambda kv: kv[1], reverse=True)
            
    def add_User(self, ambito, nivel, pc):
        new_id = self.generate_id()
        with self.db.session() as session:
            session.run("CREATE (a:User { ID: '%s' }) "%(new_id))
            session.run("MATCH (a:User),(b:Ambito) WHERE a.ID = '%s' AND b.Ambito = '%s' CREATE (a)-[r:Ambito]->(b)"%(new_id, ambito))
            session.run("MATCH (a:User),(b:Nivel) WHERE a.ID = '%s' AND b.Level = '%s' CREATE (a)-[r:Nivel]->(b)"%(new_id,nivel))
            session.run("MATCH (a:User),(b:PC) WHERE a.ID = '%s' AND b.modelo = '%s' CREATE (a)-[r:PC]->(b)"%(new_id,pc))
            print("Usuario añadido con exito")
    
    def generate_id(self):
        with self.db.session() as session:
            record = session.run("MATCH (u:User) return COUNT(u)")
            for r in record:
                return "User0"+str(r['COUNT(u)']+1)
            
            
#g = Graph_manager()
#g.add_User("Mecanica","Profesional","DELL G3")
#print(g.recommend("Mecanica","Profesional"))
