from django.shortcuts import render

# Create your views here.

finchs = [
    {'name': 'Pheobe', 'breed': 'House finch', 'description': 'Kind of annoying', 'age': 4},
    {'name': 'Sasha', 'breed': 'Hawfinch', 'description': 'Actually annoying', 'age': 1},
    {'name': 'Jamie', 'breed': 'Brambling', 'description': 'The sweetest', 'age': 2},
    {'name': 'Julie', 'breed': 'Atlantic canary', 'description': 'Super rude', 'age': 3},
]

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def finchs_index(request):
    return render(request, 'finchs/index.html', {
        'finchs': finchs
    })