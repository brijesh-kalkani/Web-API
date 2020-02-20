from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# imporst.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerializers

from rest_framework import generics

# from django_filters.rest_framework import DjangoFilterBackend

class PersonView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    # filter_backends = (DjangoFilterBackend,SearchFilter)





# class PersonView(APIView):
#
#     def get(self,request):
#         data = Person.objects.all()
#         print("=======",data)
#         serializer = PersonSerializers(data,many=True)
#         return Response(serializer.data)
#
#     def post(self,request,format=None):
#         try:
#             serializer = PersonSerializers(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.data, status=status.HTTP_400_OK)
#
#         except Exception as e:
#             return Response(serializer.data, status=status.HTTP_400_OK)








# global data
# data = ["brijesh"]
#
# class Youtube(APIView):
#     """docstring forYoutube."""
#
#     def get(self,requests,format = None):
#         return Response({"Message":data})
#
#     def post(self,requests,format = None):
#
#         Mydata = self.request.data
#
#         Name = Mydata.get("Name",None)
#
#         data.append(Name)
#
#
#         return Response({
#             "Response":200,
#             "Data":Name,
#             "message":"Item was Addes to Database"
#             })
