from django.shortcuts import render

from lab_2.views import landing_page_content

# Create your views here.
response = {'author': "Kezia Irene Tesiman"} #TODO Implement yourname
about_me = [" Saya ", " hobi ", " bermain ", " piano "," dan ", " biola "]
def index(request):
    response['content'] = landing_page_content
    html = 'lab_4/lab_4.html'
    #TODO Implement, isilah dengan 6 kata yang mendeskripsikan anda
    response['about_me'] = about_me
    return render(request, html, response)

# Create your views here.
