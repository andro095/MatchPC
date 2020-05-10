from django.http import HttpResponse

#Funcion vista de la pagina principal
def index(request):
    return HttpResponse("Aqui va la pagina principal")