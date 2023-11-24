from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')
        
class BescDataSirializer(serializers.ModelSerializer):
    class Meta:
        model = BesicData
        fields = ['title','from_date','to_date','about']
        
class OrganizersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizers
        fields = ['id','name','get_img','face_link','x_link','web_site','phone']
        
class ShepherdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shepherds
        fields = ['id','name','get_img','face_link','x_link','web_site','type']
        
class ScheduleSirializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id','title','descripe','from_time','to_time','day']
        
class SpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = ['id','name','get_img','type']