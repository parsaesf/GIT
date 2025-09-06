from django.shortcuts import render,HttpResponse



def home():
    return HttpResponse("this is home")

