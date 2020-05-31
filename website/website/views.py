from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from neo4j import GraphDatabase
import os

#Funcion vista de la pagina principal
def index(request):
    return render(request, "index.html", {})
    #return HttpResponse("Aqui va la pagina principal")

def about(request):
    return render(request, "about.html", {})

def match(request):
    context = {
        'query': False,
    }
    
    return render(request, "match.html", context)

def aportar(request):
    return render(request, "aportar.html", {})

def match_query(request):
    db = Graph_manager()
    r = db.recommend(request.GET["txtAmbito"],request.GET["txtNivel"])
    context = {
        'query': True,
        'request': r,
        'size': len(r),
        'img_name': 'notFound.png'
    }
    '''
    if(len(r) > 0):
        IMG_URL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/media/compu_img/"
        if(os.path.isfile(IMG_URL+context['request'][0]+".png")):
            context['img_name'] = context['request']+".png"
        elif(os.path.isfile(IMG_URL+context['request']+".jpg")):
            context['img_name'] = context['request']+".jpg"
    '''
    return render(request, "match.html", context)

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