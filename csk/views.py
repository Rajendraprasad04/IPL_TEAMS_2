from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h2>MS Dhoni is the captain of CSk</h2>')
def vicecaptain(request):
    return HttpResponse('<h1>Raina is vice captain of CSK Team</h1>')
