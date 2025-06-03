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
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')    

def index(request):
    return render(request, 'home/index.html')

def success_page(request):
    return render(request, 'home/success_page.html')