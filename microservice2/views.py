from django.http import HttpResponse

def endpoint2(request):
    return HttpResponse("This is microservice2, endpoint2")
