from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world111111")

def yeki(request):
    return HttpResponse("yeki")