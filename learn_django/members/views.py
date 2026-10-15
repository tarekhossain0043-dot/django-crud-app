from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from .models import Member
from .serializers import MemberSerializer

class MemberListCreateAPIView (ListCreateAPIView) : 
     queryset = Member.object.all() # get all data from database
    serializer_class = MemberSerializer