from django.shortcuts import render

# Enter your name here
mhs_name = 'Kezia Irene' # TODO Implement this

# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age' : calculate_age(1998)}
    return render(request, 'index.html', response)
	


# TODO Implement this to complete last checklist
def calculate_age(birth_year):
    return 2017 - birth_year
