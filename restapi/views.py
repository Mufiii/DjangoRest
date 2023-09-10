from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import *
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
import json

# # Create your views here.

def person_detail(request,pk):
    stu = Person.objects.get(id=pk)
    print(stu)
    serializer = PersonSerializer(stu) #  converting the stu object into a native python
    # json_data = JSONRenderer().render(serializer.data) # TO JSON  
    # return HttpResponse(json_data , content_type='application/json')
    return JsonResponse(serializer.data)

    
def person_list(request):
    stu = Person.objects.all()
    serializer = PersonSerializer(stu, many=True) #  converting the stu object into a native python
    # json_data = JSONRenderer().render(serializer.data)  
    # return HttpResponse(json_data , content_type='application/json')
    return JsonResponse(serializer.data , safe=False)
    
    # safe
    
    # the safe parameter is used to control how the response handles non-dictionary objects when converting them to JSON.
