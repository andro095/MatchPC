from neo4j import GraphDatabase

#Clase principal

class Graph_manager:
    #Inicialización
    def __init__(self):
        #Conexion y configuracion de python para neo4j
        uri             = "bolt://localhost:7687"
        userName        = "neo4j"
        password        = "123"
        self.db = GraphDatabase.driver(uri, auth=(userName, password), encrypted=False)
        
    #Setter y Getter   
    def get_graph(self):
        return self.db
        
    def set_graph(self, db):
        self.db = db
        
    #Recomendar computadora a usuario
    def recommend(self):
        with self.db.session() as session:
            record = session.run("MATCH (p:PC),(u:User) WHERE (u)-[:Ambito]->({Ambito:'Diseño Gráfico'}) AND (u)-[:Nivel]->({Level:'Profesional'}) AND (u)-[:PC]->(p) return p")
            for line in record:
                print("La computadora que se adecua a su ambito y nivel profesional es:")
                print (line["p"])
            
    def add_User(self):
        g.generate_id
        with self.db.session() as session:
            record = session.run("CREATE (a:User { ID: 'User021' }) WITH a "
"MATCH (a:User),(b:Ambito) WHERE a.ID = 'User021' AND b.Ambito = 'Diseño Gráfico' " 
"CREATE (a)-[r:Ambito]->(b) WITH a MATCH (a:User), (b:Nivel) WHERE a.ID = 'User019' AND b.Level = 'Profesional' "
"CREATE (a)-[r:Nivel]->(b) "
"WITH a, b MATCH (a:User),(b:PC)WHERE a.ID = 'User021' AND b.modelo = 'Alienware Razer' CREATE (a)-[r:PC]->(b)")
            print("Usuario añadido con exito")
    
    def generate_id(self):
        with db.session() as session:
             record = session.run("MATCH (u:User) return COUNT(u)")
            
g = Graph_manager()
g.add_User()
g.recommend()