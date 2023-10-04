from django.shortcuts import render

# Create your views here.
# things/views.py
def home(request):
    return render(request, 'home.html')
