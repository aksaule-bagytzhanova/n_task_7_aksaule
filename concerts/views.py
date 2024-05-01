from django.shortcuts import render

# Create your views here. 
def home(request):
    return render(request, 'templates/main.html')

def details(request):
    return render(request, 'templates/main.html')