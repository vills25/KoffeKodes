from django.shortcuts import render

# Create your views here.

def receipes(request):

    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipes_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        print(receipes_name)
        print(receipe_description)
        print(receipe_image)

        return render(request, 'receipes.html')