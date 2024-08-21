from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>Rohit Sharma is captain of MI</h1>')
def vicecaptain(request):
    return render(request,'vc.html')
