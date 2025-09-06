# accounts/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page from develop")

