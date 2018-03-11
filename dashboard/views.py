from django.shortcuts import render

# Create your views here.

response ={}
def index(request):    
    response['author'] = "Kezia Irene Tesiman"
    html = 'dashboard/dashboard.html'
    return render(request, html, response)

