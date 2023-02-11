from django.shortcuts import render
from rest_framework import generics
# from .backend import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth
import jwt
from django.conf import settings
from .serializers import MenuItemSerializer, BookingSerializer
from .models import MenuItem, Booking
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'index.html')

class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer
    # permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    def post(self, request):
        serializer = MenuItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status= status.HTTP_201_CREATED)
        return Response(data= serializer.errors, status=status.HTTP_403_BAD_REQUEST)
    def get(self, request):
        menu = MenuItem.objects.all()
        serializer = self.serializer_class(menu, many=True)
        return Response(serializer.data)

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = MenuItemSerializer
    def get(self, request, id):
        menu = get_object_or_404(MenuItem, id=id)
        serializer = MenuItemSerializer(menu)
        return Response(serializer.data)
    def delete(self, request, id):
        menu = get_object_or_404(MenuItem, id=id)
        menu.delete()
        return Response({"message": "Menu Item deleted"}, status=status.HTTP_202_ACCEPTED)
    def put(self, request, id):
        menu = get_object_or_404(MenuItem, id=id)
        serializer = MenuItemSerializer(data=menu)
        if serializer.is_valid():
            return Response(data = serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class BookingView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = self.serializer_class(bookings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status= status.HTTP_201_CREATED)
        return Response(data= serializer.errors, status=status.HTTP_403_BAD_REQUEST)
# from .serializers import UserSerializer, LoginSerializer


# class RegisterView(GenericAPIView):
#     serializer_class = UserSerializer

#     def post(self, request):
#         serializer = UserSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data = serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# class LoginView(GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
#         data = request.data
#         username = data.get('username', '')
#         password = data.get('password', '')
#         user = auth.authenticate(username=username, password=password)

#         if user:
            
#             auth_token = jwt.encode(
#                 {'username': user.username}, settings.JWT_SECRET_KEY)
#             serializer = UserSerializer(user)

#             data = {'user': serializer.data, 'token': auth_token}

#             return Response(data, status=status.HTTP_200_OK)
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)