from django.shortcuts import render

finches = [
    {'name': 'Birdie', 'breed': 'house', 'description': 'black and red', 'age': 2},
  {'name': 'Tweetie', 'breed': 'purple', 'description': 'aggressive and bold', 'age': 5},
  {'name': 'Flapper', 'breed': 'gouldian', 'description': 'protective and loving', 'age': 3},
]

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })