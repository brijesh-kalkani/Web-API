from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# imporst.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# sys.path.append("/Users/sierra/Courses/WebAPI/FirstAPI")
from .models import Person
# from .serializer import PersonSerializers

# import PersonSerializerrs
# import Person

# class PersonView(APIView):
#
#     def get(self,request):
#         data = Person.objects.all()
#         serializer = PersonSerializers(data,many=True)
#         return Response(serializer.data)








global data
data = ["brijesh"]

class Youtube(APIView):
    """docstring forYoutube."""

    def get(self,requests,format = None):
        return Response({"Message":data})

    def post(self,requests,format = None):

        Mydata = self.request.data

        Name = Mydata.get("Name",None)

        data.append(Name)


        return Response({
            "Response":200,
            "Data":Name,
            "message":"Item was Addes to Database"
            })
