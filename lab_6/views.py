from django.shortcuts import render

# Create your views here.
response={}
def index(request):
	html = 'lab_6/lab_6.html'
	response['author'] = "Kezia Irene"
	return render(request, html, response)
