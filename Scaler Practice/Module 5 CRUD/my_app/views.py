from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer
from .serializers import CustomerSerializer

# Create a new item
@api_view(['POST'])
def customer_create(request):
    print(request.data)
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data created',"data":serializer.data },status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_customers(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)

    data = {
        'result' : serializer.data
    }
    return Response({'message':'data fetched',"data":data},status=200)  

@api_view(['POST'])
def get_one_customer(request):
    try:
        pk = request.data.get('id')
        customer = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status = 400)
        
    serializer = CustomerSerializer(customer)
    data = {
        'result':serializer.data
    }
    return Response({'message':'data fetched',"data":data},status=201)
    

@api_view(['PUT', 'PATCH'])
def update_customer(request):
    pk = request.data.get('id')
    customer = Customer.objects.get(id=pk)
    
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "customer updated !","data": serializer.data})
    return Response({"error": serializer.errors}, status=400)


@api_view(['DELETE'])
def delete_customer(request):
    pk = request.data.get('id')
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return Response({"message": "customer deleted!"}, status=204)