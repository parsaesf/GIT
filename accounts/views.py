
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page from develop")


def profile(request):
    return HttpResponse("profile Page ")


