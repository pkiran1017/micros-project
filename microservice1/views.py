from django.http import HttpResponse

def endpoint1(request):
    return HttpResponse("This is microservice1, endpoint1")
