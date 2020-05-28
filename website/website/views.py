from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

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

def match_query(request):
    context = {
        'query': True,
        'modelo': 'Alienware Area 51',
        'tipo': 'Laptop',
        'marca': 'Alienware',
        'cpu': 'Intel core i5',
        'tipo_ram': 'DDR4',
        'capacidad_ram': '8 GB',
        'gpu_marca': 'Nvidia',
        'gpu_modelo': 'RTX 1080',
        'img_name': 'notFound'
    }
    try:
        with open("/media/compu_img/"+context['modelo']+".png") as img:
            if img:
                context['img_name'] = context['modelo']
    except:
        context['img_name'] = 'notFound'
    
    return render(request, "match.html", context)