from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the catalog page.")  # Simple response para probar

