from django.shortcuts import render,HttpResponse

# Create your views here.


def example(request):
    return HttpResponse("welcome")