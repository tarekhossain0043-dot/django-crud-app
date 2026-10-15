# Serializers for convert to json formate
from rest_framework import serializer
from .models import Member

class memberSerializer(serializers,modelSerializers) :
     class Meta:
          model = Member,
          field = ['id','name','role','joined_at'] #this field are show in API