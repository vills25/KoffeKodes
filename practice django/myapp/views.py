from django.shortcuts import render

def home(request):
    context = [{
        'name': 'Vishal',
        'age': 17},
        {
        'name': 'Rakshit',
        'age': 18
    },
    {
        'name': 'Viraj',
        'age': 26
    },
    {
        'name': 'Akash',
        'age': 15
    }
        
        ]
    return render(request, 'home.html', context = {'context' : context})
