from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from rest_framework.decorators import api_view # type: ignore
# Create your views here.

@api_view(['POST'])
def  create_receipes(request):

    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        Receipe.objects.create(
            receipe_image =receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description)

        # return redirect('/receipes/'), 
        return HttpResponse({'status':'success','message':'data created successfully ',"data":context}, status=201)


    # queryset = Receipe.objects.all()
    # context = {'receipes':queryset}
    return render(request, 'receipes.html',context)
    # return HttpResponse({'status':'success','message':'data fetched successfully ',"data":context}, status=200) 

@api_view(['GET'])
def receipe_detail(request):
    id = request.GET.get('id')
    queryset = Receipe.objects.get(id=id)
    context = {'receipe': queryset}
    # return render(request, 'receipe_detail.html', context), 
    return HttpResponse({'status':'success','message':'data fetched successfully ',"data":context}, status=200)

@api_view(['PUT', 'POST'])
def update_receipe(request):
    id = request.GET.get('id')
    queryset = Receipe.objects.get(id=id)

    if request.method == "PUT" or request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
    
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        #return redirect('/receipes/'), 
        return HttpResponse({'status':'success','message':'data updated successfully ',"data":context}, status=200)

    context = {'receipe': queryset}

    return render(request, 'update_receipes.html', context)

@api_view(['DELETE'])
def delete_receipes(request):
    if request.method == "DELETE":
        id = request.GET.get('id')
        queryset = Receipe.objects.get(id=id)
        queryset.delete()
        #return redirect('/receipes/'), 
        return HttpResponse({'status':'success','message':'data deleted successfully ',"data":context}, status=200)