from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'protoWiki11\index.html')

def AstelPage(request):
    return render(request, 'protoWiki11\AstelPage.html')

def FirePotPage(request):
    return render(request, 'protoWiki11\FirePotPage.html')

def MelinasPage(request):
    return render(request, 'protoWiki11\MelinasPage.html')

def WeaponPage(request):
    return render(request, 'protoWiki11\WeaponPage.html')



def header(request):
    return render(request, '\includes\header.html')