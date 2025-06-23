from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Customer
from .serializers import CustomerS
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
def regcustomer(request):
    data=request.data 
    serializer = CustomerS(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def logincustomer(request):
#     data=request.data
#     print(data)
#     try:
#         user = Customer.objects.get(email=data['username'])
#     except:
#         return Response({'error':"Invalid Credentials"},status=400)

#     if (data['password'] == user.password):
#         return Response({'message':'Login Successful'})
#     else:
#         return Response({'error':"Invalid Credentials"},status=400)


@api_view(['POST'])
def login_with_jwt(request):
    data = request.data
    try:
        user = Customer.objects.get(email=data['username'])
    except Customer.DoesNotExist:
        return Response({'error': "Invalid Credentials"}, status=400)

    if check_password(data['password'], user.password):
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': "Login Successful"
        })
    else:
        return Response({'error': "Invalid Credentials"}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_dashboard(request):
    return Response({'message': f'Welcome {request.user.fullname}'})
