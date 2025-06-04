from django.shortcuts import render

def home(request):
    contact = [{
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
    return render(request, 'base.html', context = {'context' : contact})


def contact(request):
    context = {'page' : 'About'}
    return render(request, 'home/contact.html', context)

def about(request):
    context = {'page' : 'About'}
    return render(request, 'home/about.html', context)    

def index(request):
    context = {'page' : 'About'}
    return render(request, 'home/index.html', context)

def success_page(request):
    context = {'page' : 'About'}
    return render(request, 'home/success_page.html', context)