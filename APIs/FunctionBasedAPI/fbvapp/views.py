from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item


# Get all items
@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    data = {
        'result':serializer.data
    }

    return Response({'status':'success','message':'data fetched successfully ',"data":data},status=200)

# Get single item by Enter its ID.
@api_view(['POST'])
def item_detail(request):
    try:
        pk = request.data.get('id')
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'},status= 404)

    serializer = ItemSerializer(item)

    data = {
        'result':serializer.data
    }

    return Response({'status':'success','message':'data fetched successfully',"data":data},status=201)

# Create a new item
@api_view(['POST'])
def item_create(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status':'success','message':'data created successfull',"data":serializer.data },status=201)
    return Response(serializer.errors, status=400)

# Update an existing item
@api_view(['PUT'])
def item_update(request):
    try:
        pk = request.data.get('id')
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'},status= 404)
    
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status':'success','message':'data Updated successfully', 'Updated data': serializer.data},status=200)
    return Response(serializer.errors,status= 400)

# Delete an item
@api_view(['DELETE'])
def item_delete(request ):
    try:
        pk = request.data.get('id')
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'},status= 404)

    item.delete()
    return Response({'status':'success','message':'data Deleted!!'},status=204)

# # upload image
# @api_view(['POST'])
# def item_upload_image(request):
#     try: 
#         pk = request.data.get('id')
#         item = Item.objects.get(id=pk)
#     except Item.DoesNotExist:
#         return Response({'error': 'Item not found'}, status=404)

#     serializer = ItemSerializer(item, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status': 'success', 'message': 'Image uploaded successfully', 'data': serializer.data}, status=200)
#     return Response(serializer.errors, status=400)
